--!strict
-- BoltBots Tycoon design configuration. Prices and rewards are soft currency only.
local GameConfig = {
    project = "BoltBotsTycoon",
    displayName = "BoltBots Tycoon",
    schemaVersion = 1,
    maxPlots = 4,
    starterCash = 0,
    startingUpgradeLevel = 1,
    maxUpgradeLevel = 8,
    baseCycleSeconds = 7,
    cycleMultiplier = 0.82,
    minCycleSeconds = 1.6,
    creditsPerRobot = 25,
    firstUpgradePrice = 50,
    upgradePriceMultiplier = 1.65,
    firstRobotId = "scout",
    versionLabel = "prototype-0.2",
}

return table.freeze(GameConfig)
