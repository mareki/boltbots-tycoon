--!strict
-- Reversible local playtest values, not final progression balance.
local GameConfig = {
    project = "BoltBotsTycoon",
    displayName = "BoltBots Tycoon",
    schemaVersion = 2,
    catalogVersion = 1,
    versionLabel = "development-b4",
    maxPlots = 4,
    starterCash = 0,
    baseCycleSeconds = 9,
    creditsPerRobot = 25,
    maxCash = 1_000_000_000,
    firstUpgradePrice = 50,
    upgradedCycleSeconds = 6,
    firstRobotId = "scout",
}
return table.freeze(GameConfig)
