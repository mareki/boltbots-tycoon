--!strict
-- Persisted CTX-FACTORY values only. Runtime cycles, plots and request caches are never stored.
local Config = require(script.Parent.GameConfig)
local Schema = {}
Schema.fields = {"cash", "completed", "lifetimeEarned", "unlockedScout", "unlockedOrbit", "level", "selectedDesign"}
local function integer(v: any, max: number): boolean
    return type(v)=="number" and v==v and v>=0 and v<=max and v==math.floor(v)
end
function Schema.copyData(profile: any): any
    local data = {}
    for _,key in ipairs(Schema.fields) do data[key]=profile[key] end
    return data
end
function Schema.validData(data: any): boolean
    return type(data)=="table" and integer(data.cash,Config.maxCash)
        and integer(data.completed,Config.maxCash) and integer(data.lifetimeEarned,Config.maxCash)
        and data.cash<=data.lifetimeEarned and type(data.unlockedScout)=="boolean"
        and type(data.unlockedOrbit)=="boolean" and (data.level==1 or data.level==2)
        and data.unlockedOrbit==(data.level==2)
        and (data.selectedDesign=="scout" or data.selectedDesign=="orbit" and data.unlockedOrbit)
end
function Schema.decode(raw: any): (any, string)
    if raw==nil then
        return {schemaVersion=2,revision=0,data={cash=0,completed=0,lifetimeEarned=0,
            unlockedScout=false,unlockedOrbit=false,level=1,selectedDesign="scout"}},"new"
    end
    if type(raw)~="table" or (raw.schemaVersion~=1 and raw.schemaVersion~=2) then return nil,"unsupported_schema" end
    if not integer(raw.revision,9_000_000_000) or type(raw.data)~="table" then return nil,"invalid_profile" end
    local data=Schema.copyData(raw.data)
    if raw.schemaVersion==1 then data.unlockedOrbit=data.level==2 end
    if not Schema.validData(data) then return nil,"invalid_profile" end
    local lease=raw.session
    if lease~=nil and (type(lease)~="table" or type(lease.token)~="string" or #lease.token==0
        or not integer(lease.expiresAt,9_000_000_000)) then return nil,"invalid_profile" end
    if raw.lastWriteId~=nil and type(raw.lastWriteId)~="string" then return nil,"invalid_profile" end
    return {schemaVersion=2,revision=raw.revision,data=data,
        session=if lease then {token=lease.token,expiresAt=lease.expiresAt} else nil,
        lastWriteId=raw.lastWriteId}, if raw.schemaVersion==1 then "migrated" else "loaded"
end
return table.freeze(Schema)
