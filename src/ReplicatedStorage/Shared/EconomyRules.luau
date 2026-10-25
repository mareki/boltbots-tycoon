--!strict
-- CTX-FACTORY. Pure transitions; animation and client messages cannot award cash.
local Config = require(script.Parent.GameConfig)
local Rules = {}

type Cycle = { id: number, designId: string, startedAt: number, completesAt: number }
export type Profile = {
    active: boolean,
    cash: number,
    completed: number,
    lifetimeEarned: number,
    unlockedScout: boolean,
    unlockedOrbit: boolean,
    level: number,
    selectedDesign: string,
    highestRequest: number,
    requests: {[string]: any},
    requestOrder: {string},
    stateVersion: number,
    lastCycleId: number,
    lastCompletedCycleId: number,
    cycle: Cycle?,
}

local function finite(value: number): boolean
    return value == value and math.abs(value) < math.huge
end
local function amount(value: number): boolean
    return finite(value) and value >= 0 and value <= Config.maxCash and value == math.floor(value)
end

function Rules.newProfile(): Profile
    return {
        active = true, cash = Config.starterCash, completed = 0, lifetimeEarned = 0,
        unlockedScout = false, unlockedOrbit = false, level = 1, selectedDesign = "scout",
        highestRequest = 0, requests = {}, requestOrder = {}, stateVersion = 1, lastCycleId = 0,
        lastCompletedCycleId = 0, cycle = nil,
    }
end

function Rules.cycleSeconds(profile: Profile): number
    return if profile.level == 2 then Config.upgradedCycleSeconds else Config.baseCycleSeconds
end

function Rules.beginCycle(profile: Profile, now: number): (boolean, string)
    if not profile.active then return false, "inactive" end
    if profile.cycle then return false, "already_running" end
    if not finite(now) or now < 0 or not finite(Rules.cycleSeconds(profile)) or Rules.cycleSeconds(profile) <= 0 then
        return false, "invalid_time"
    end
    if not amount(profile.cash) or profile.cash > Config.maxCash - Config.creditsPerRobot
        or not amount(profile.lifetimeEarned) or profile.lifetimeEarned > Config.maxCash - Config.creditsPerRobot then
        return false, "cash_limit"
    end
    profile.lastCycleId += 1
    profile.cycle = { id = profile.lastCycleId, designId = profile.selectedDesign,
        startedAt = now, completesAt = now + Rules.cycleSeconds(profile) }
    return true, "started"
end

function Rules.completeCycle(profile: Profile, cycleId: number, now: number): (boolean, string)
    if not profile.active then return false, "inactive" end
    if not finite(cycleId) or cycleId ~= math.floor(cycleId) or cycleId <= profile.lastCompletedCycleId then
        return false, "duplicate_or_invalid"
    end
    local cycle = profile.cycle
    if not cycle or cycleId ~= cycle.id or (cycle.designId ~= "scout" and cycle.designId ~= "orbit") then
        return false, "unknown_cycle"
    end
    if not finite(now) or now < cycle.completesAt then return false, "not_due" end
    if not amount(profile.cash) or profile.cash > Config.maxCash - Config.creditsPerRobot
        or not amount(profile.lifetimeEarned) or profile.lifetimeEarned > Config.maxCash - Config.creditsPerRobot then
        return false, "cash_limit"
    end
    -- One non-yielding transition commits output, cash and the design right together.
    profile.cash += Config.creditsPerRobot
    profile.lifetimeEarned += Config.creditsPerRobot
    profile.completed += 1
    if cycle.designId == "scout" then profile.unlockedScout = true end
    profile.lastCompletedCycleId = cycleId
    profile.cycle = nil
    profile.stateVersion += 1
    return true, "completed"
end

-- Bounded response cache plus a monotonic request watermark prevents replay after eviction.
-- Request ids are positive decimal strings, scoped to this active session (persistence: B3).
function Rules.command(profile: Profile, kind: string, payload: any): any
    local function answer(ok: boolean, code: string)
        local responseId = if type(payload) == "table" and type(payload.requestId) == "string" and #payload.requestId <= 10 then payload.requestId else nil
        return {requestId = responseId,
            ok = ok, code = code, stateVersion = profile.stateVersion}
    end
    if not profile.active then return answer(false, "inactive") end
    if type(payload) ~= "table" or (kind ~= "upgrade" and kind ~= "select") then return answer(false, "invalid_request") end
    local allowed = if kind == "upgrade" then {requestId=true,machineId=true,expectedLevel=true,catalogVersion=true}
        else {requestId=true,designId=true}
    for key in pairs(payload) do if not allowed[key] then return answer(false, "invalid_request") end end
    local id = payload.requestId
    if type(id) ~= "string" or #id > 10 or not string.match(id, "^[1-9]%d*$") then return answer(false, "invalid_request") end
    local sequence = tonumber(id)
    if not sequence or not finite(sequence) or sequence > 9_000_000_000 then return answer(false, "invalid_request") end
    local cached = profile.requests[id]
    if cached then return cached end
    if sequence <= profile.highestRequest then return answer(false, "stale_request") end
    local ok, code = false, "invalid_request"
    if kind == "upgrade" then
        if payload.machineId ~= "starter" then code = "forbidden"
        elseif payload.catalogVersion ~= Config.catalogVersion or payload.expectedLevel ~= profile.level then code = "stale_state"
        elseif profile.level >= 2 then code = "level_limit"
        elseif not amount(profile.cash) or not amount(Config.firstUpgradePrice) then code = "invalid_amount"
        elseif profile.cash < Config.firstUpgradePrice then code = "funds"
        else
            -- Cash, level and design entitlement commit together, without a yield.
            profile.cash -= Config.firstUpgradePrice
            profile.level = 2
            profile.unlockedOrbit = true
            profile.stateVersion += 1
            ok, code = true, "upgraded"
        end
    else
        if payload.designId ~= "scout" and payload.designId ~= "orbit" then code = "unknown_design"
        elseif payload.designId == "orbit" and not profile.unlockedOrbit then code = "locked"
        else
            -- The already running cycle is immutable; beginCycle consumes this selection later.
            if profile.selectedDesign ~= payload.designId then
                profile.selectedDesign = payload.designId
                profile.stateVersion += 1
            end
            ok, code = true, "selected"
        end
    end
    local result = answer(ok, code)
    profile.highestRequest = sequence
    profile.requests[id] = result
    table.insert(profile.requestOrder, id)
    if #profile.requestOrder > 32 then
        local oldest = table.remove(profile.requestOrder, 1)
        if oldest then profile.requests[oldest] = nil end
    end
    return result
end

function Rules.stop(profile: Profile)
    profile.active = false
    profile.cycle = nil
end

return table.freeze(Rules)
