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
        unlockedScout = false, stateVersion = 1, lastCycleId = 0,
        lastCompletedCycleId = 0, cycle = nil,
    }
end

function Rules.beginCycle(profile: Profile, now: number): (boolean, string)
    if not profile.active then return false, "inactive" end
    if profile.cycle then return false, "already_running" end
    if not finite(now) or now < 0 or not finite(Config.baseCycleSeconds) or Config.baseCycleSeconds <= 0 then
        return false, "invalid_time"
    end
    if not amount(profile.cash) or profile.cash > Config.maxCash - Config.creditsPerRobot
        or not amount(profile.lifetimeEarned) or profile.lifetimeEarned > Config.maxCash - Config.creditsPerRobot then
        return false, "cash_limit"
    end
    profile.lastCycleId += 1
    profile.cycle = { id = profile.lastCycleId, designId = Config.firstRobotId,
        startedAt = now, completesAt = now + Config.baseCycleSeconds }
    return true, "started"
end

function Rules.completeCycle(profile: Profile, cycleId: number, now: number): (boolean, string)
    if not profile.active then return false, "inactive" end
    if not finite(cycleId) or cycleId ~= math.floor(cycleId) or cycleId <= profile.lastCompletedCycleId then
        return false, "duplicate_or_invalid"
    end
    local cycle = profile.cycle
    if not cycle or cycleId ~= cycle.id or cycle.designId ~= Config.firstRobotId then
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
    profile.unlockedScout = true
    profile.lastCompletedCycleId = cycleId
    profile.cycle = nil
    profile.stateVersion += 1
    return true, "completed"
end

function Rules.stop(profile: Profile)
    profile.active = false
    profile.cycle = nil
end

return table.freeze(Rules)
