--!strict
local Config = require("./GameConfig")
local Rules = require("./EconomyRules")
local p = Rules.newProfile()
assert(p.cash == 0 and not p.unlockedScout and p.completed == 0)
assert(Rules.beginCycle(p, 100))
local ok, code = Rules.beginCycle(p, 100)
assert(not ok and code == "already_running")
assert(not Rules.completeCycle(p, 1, 108.99))
assert(not Rules.completeCycle(p, 2, 109))
assert(p.cash == 0 and not p.unlockedScout and p.completed == 0)
assert(Rules.completeCycle(p, 1, 109))
assert(p.cash == 25 and p.unlockedScout and p.completed == 1 and p.stateVersion == 2)
assert(not Rules.completeCycle(p, 1, 1000))
assert(p.cash == 25 and p.completed == 1)
assert(Rules.beginCycle(p, 110))
assert(not Rules.completeCycle(p, 1, 119))
assert(Rules.completeCycle(p, 2, 119))
assert(p.cash == 50 and p.completed == 2 and p.lifetimeEarned == 50)
assert(Rules.beginCycle(p, 120))
Rules.stop(p)
assert(not Rules.completeCycle(p, 3, 1000))
assert(not Rules.beginCycle(p, 1000))
assert(p.cash == 50 and p.completed == 2)

for _, invalid in ipairs({-1, math.huge, 0/0}) do
    local test = Rules.newProfile()
    assert(not Rules.beginCycle(test, invalid))
    assert(Rules.beginCycle(test, 0))
    assert(not Rules.completeCycle(test, invalid, 10))
    assert(not Rules.completeCycle(test, 1, invalid))
    assert(test.cash == 0 and not test.unlockedScout)
end
local exact = Rules.newProfile()
exact.cash = Config.maxCash - Config.creditsPerRobot
exact.lifetimeEarned = exact.cash
assert(Rules.beginCycle(exact, 0))
assert(Rules.completeCycle(exact, 1, Config.baseCycleSeconds))
assert(exact.cash == Config.maxCash and exact.lifetimeEarned == Config.maxCash)
assert(not Rules.beginCycle(exact, 20))
for _, invalid in ipairs({-1, 0.5, math.huge, 0/0, Config.maxCash - 24}) do
    local test = Rules.newProfile()
    assert(Rules.beginCycle(test, 0))
    test.cash = invalid
    assert(not Rules.completeCycle(test, 1, 10))
    assert(test.completed == 0 and not test.unlockedScout)
end
print("B1 rules: due completion, cash + Scout atomic, duplicate/old/unknown/early denial, stop, finite values and exact/overflow limits OK")
