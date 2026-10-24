--!strict
-- Pure, deterministic rules. Never trust client-provided cash, prices or rewards.
local Config = require(script.Parent.GameConfig)

local Rules = {}

type Profile = {
    cash: number,
    robots: number,
    upgradeLevel: number,
    lifetimeEarned: number,
    nextProductionAt: number,
}

function Rules.newProfile(): Profile
    return {
        cash = Config.starterCash,
        robots = 0,
        upgradeLevel = Config.startingUpgradeLevel,
        lifetimeEarned = 0,
        nextProductionAt = 0,
    }
end

function Rules.upgradePrice(level: number): number?
    if type(level) ~= "number" or level ~= math.floor(level) or level < 1 or level >= Config.maxUpgradeLevel then
        return nil
    end
    return math.floor(Config.firstUpgradePrice * (Config.upgradePriceMultiplier ^ (level - 1)) + 0.5)
end

function Rules.cycleSeconds(level: number): number
    if type(level) ~= "number" or level < 1 or level > Config.maxUpgradeLevel then
        return Config.baseCycleSeconds
    end
    return math.max(Config.minCycleSeconds, Config.baseCycleSeconds * (Config.cycleMultiplier ^ (level - 1)))
end

function Rules.robotsPerMinute(level: number): number
    return 60 / Rules.cycleSeconds(level)
end

function Rules.awardRobot(profile: Profile): ()
    profile.cash += Config.creditsPerRobot
    profile.lifetimeEarned += Config.creditsPerRobot
    profile.robots += 1
end

function Rules.tryUpgrade(profile: Profile): (boolean, string)
    local price = Rules.upgradePrice(profile.upgradeLevel)
    if price == nil then
        return false, "MAX_LEVEL"
    end
    if profile.cash < price then
        return false, "INSUFFICIENT_CASH"
    end
    profile.cash -= price
    profile.upgradeLevel += 1
    return true, "UPGRADED"
end

return table.freeze(Rules)
