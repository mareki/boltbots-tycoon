--!strict
-- Tests the adopted baseline, not the still-open M1 purchase/save contracts.
local Config = require("./GameConfig")
local Rules = require("./EconomyRules")

local profile = Rules.newProfile()
assert(profile.cash == 0 and profile.robots == 0 and profile.upgradeLevel == 1)
local ok, code = Rules.tryUpgrade(profile)
assert(not ok and code == "INSUFFICIENT_CASH")
assert(profile.cash == 0 and profile.upgradeLevel == 1)

Rules.awardRobot(profile)
assert(profile.cash == Config.creditsPerRobot and profile.robots == 1)
assert(profile.lifetimeEarned == Config.creditsPerRobot)
local price = Rules.upgradePrice(1)
assert(price ~= nil)
profile.cash = price - 1
ok, code = Rules.tryUpgrade(profile)
assert(not ok and code == "INSUFFICIENT_CASH" and profile.cash == price - 1)
profile.cash = price
ok, code = Rules.tryUpgrade(profile)
assert(ok and code == "UPGRADED" and profile.cash == 0 and profile.upgradeLevel == 2)
assert(Rules.cycleSeconds(2) < Rules.cycleSeconds(1))

profile.upgradeLevel = Config.maxUpgradeLevel
profile.cash = 1000
ok, code = Rules.tryUpgrade(profile)
assert(not ok and code == "MAX_LEVEL" and profile.cash == 1000)
assert(Rules.upgradePrice(0) == nil and Rules.upgradePrice(1.5) == nil)
assert(Rules.upgradePrice(math.huge) == nil and Rules.upgradePrice(0 / 0) == nil)
assert(Rules.cycleSeconds(0) == Config.baseCycleSeconds)
print("Economy baseline: initial state, reward, insufficient/exact funds, L2 and max-level guards OK")
