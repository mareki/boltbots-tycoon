--!strict
-- The production adapter uses Roblox UpdateAsync. Injected clock/store permit exact CLI fault tests.
local Schema = require(game:GetService("ReplicatedStorage").Shared.ProfileSchema)
local ProfileStore = {}
ProfileStore.leaseSeconds=90
ProfileStore.saveInterval=30
ProfileStore.safetySeconds=5

function ProfileStore.new(store: any, clock: () -> number, guid: () -> string): any
    local adapter={}
    function adapter.open(handle: any): (boolean, string, any)
        local reason="store_error"
        local ok,value=pcall(function()
            return store:UpdateAsync(handle.key,function(raw)
                local record,code=Schema.decode(raw)
                if not record then reason=code;return nil end
                local now=clock()
                if record.session and record.session.token~=handle.token and record.session.expiresAt>now then
                    reason="session_locked";return nil
                end
                record.session={token=handle.token,expiresAt=now+ProfileStore.leaseSeconds}
                reason=code
                return record
            end)
        end)
        if not ok then return false,"store_error",nil end
        if not value or not value.session or value.session.token~=handle.token or value.session.expiresAt<=clock()+ProfileStore.safetySeconds then
            return false,if value then "lease_lost" else reason,nil
        end
        handle.revision=value.revision;handle.expiresAt=value.session.expiresAt
        return true,reason,Schema.copyData(value.data)
    end
    function adapter.handle(key: string): any
        return {key=key,token=guid(),revision=0,expiresAt=0,pending=nil}
    end
    function adapter.save(handle: any, profile: any, release: boolean): (boolean, string)
        if not handle.pending then
            if not Schema.validData(profile) then return false,"invalid_profile" end
            handle.pending={id=guid(),revision=handle.revision,data=Schema.copyData(profile),release=release}
        end
        local write=handle.pending
        local reason="store_error"
        local ok,value=pcall(function()
            return store:UpdateAsync(handle.key,function(raw)
                if raw==nil then reason="lease_lost";return nil end
                local record,code=Schema.decode(raw)
                if not record then reason=code;return nil end
                local now=clock()
                if write.release and record.lastWriteId==write.id and record.session==nil then return record end
                if not record.session or record.session.token~=handle.token or record.session.expiresAt<=now then
                    reason="lease_lost";return nil
                end
                if record.lastWriteId==write.id then
                    -- Retry of an ambiguously acknowledged write, still owned and unexpired.
                    record.session.expiresAt=now+ProfileStore.leaseSeconds
                    return record
                end
                if record.revision~=write.revision then reason="revision_conflict";return nil end
                record.data=Schema.copyData(write.data);record.revision+=1;record.lastWriteId=write.id
                record.session=if write.release then nil else {token=handle.token,expiresAt=now+ProfileStore.leaseSeconds}
                return record
            end)
        end)
        if not ok then return false,"store_error" end
        if not value or value.lastWriteId~=write.id then return false,reason end
        if not write.release and (not value.session or value.session.token~=handle.token
            or value.session.expiresAt<=clock()+ProfileStore.safetySeconds) then return false,"lease_lost" end
        handle.revision=value.revision;handle.expiresAt=if value.session then value.session.expiresAt else 0
        handle.pending=nil
        return true,if write.release then "released" else "saved"
    end
    return adapter
end
return table.freeze(ProfileStore)
