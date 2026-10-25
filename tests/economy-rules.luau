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

local buyer = Rules.newProfile()
local function upgrade(id, level, catalog, machine)
    return Rules.command(buyer,"upgrade",{requestId=tostring(id),machineId=machine or "starter",expectedLevel=level or 1,catalogVersion=catalog or Config.catalogVersion})
end
assert(not upgrade(1).ok and buyer.cash==0 and buyer.level==1 and not buyer.unlockedOrbit)
assert(Rules.beginCycle(buyer,0)); assert(Rules.completeCycle(buyer,1,9))
assert(Rules.beginCycle(buyer,9)); assert(Rules.completeCycle(buyer,2,18))
assert(buyer.cash==50)
assert(not Rules.command(buyer,"select",{requestId="2",designId="orbit"}).ok)
assert(not upgrade(3,1,999).ok)
assert(not upgrade(4,1,nil,"other_factory").ok)
assert(not Rules.command(buyer,"upgrade",{requestId="5",machineId="starter",expectedLevel=1,catalogVersion=1,cash=0}).ok)
assert(buyer.cash==50 and buyer.level==1 and not buyer.unlockedOrbit)
assert(Rules.beginCycle(buyer,18))
local running=buyer.cycle
local result=upgrade(6)
assert(result.ok and buyer.cash==0 and buyer.level==2 and buyer.unlockedOrbit)
assert(upgrade(6)==result and buyer.cash==0)
assert(not upgrade(7).ok and not upgrade(8,2).ok)
assert(Rules.command(buyer,"select",{requestId="9",designId="orbit"}).ok)
assert(buyer.cycle==running and running and running.designId=="scout" and running.completesAt==27)
assert(not Rules.completeCycle(buyer,3,24))
assert(Rules.completeCycle(buyer,3,27))
assert(Rules.beginCycle(buyer,27))
assert(buyer.cycle and buyer.cycle.designId=="orbit" and buyer.cycle.completesAt==33)
assert(not Rules.completeCycle(buyer,4,32.99))
assert(Rules.completeCycle(buyer,4,33) and buyer.cash==50 and buyer.completed==4)
assert(not Rules.completeCycle(buyer,4,40) and buyer.cash==50)
for id=10,50 do assert(Rules.command(buyer,"select",{requestId=tostring(id),designId="scout"}).ok) end
assert(#buyer.requestOrder==32 and buyer.selectedDesign=="scout")
assert(not Rules.command(buyer,"select",{requestId="9",designId="orbit"}).ok and buyer.selectedDesign=="scout")
assert(not Rules.command(buyer,"select",{requestId="51",designId="unknown"}).ok)
for _,id in ipairs({"", "0", "-1", "1.5", "nan", string.rep("9",50)}) do
    assert(not Rules.command(buyer,"select",{requestId=id,designId="orbit"}).ok)
end
for _,invalid in ipairs({-1,0.5,math.huge,0/0}) do
    local corrupt=Rules.newProfile();corrupt.cash=invalid
    assert(not Rules.command(corrupt,"upgrade",{requestId="1",machineId="starter",expectedLevel=1,catalogVersion=1}).ok)
    assert(corrupt.level==1 and not corrupt.unlockedOrbit)
end
Rules.stop(buyer)
assert(not Rules.command(buyer,"select",{requestId="52",designId="orbit"}).ok)
print("B2 rules: exact-price atomic L2/Orbit, funds/stale/foreign/unknown denial, duplicate and evicted replay, next-cycle design AND timing, Orbit completion and bounded history OK")

local short = Rules.newProfile();short.cash = 49
local shortResult=Rules.command(short,"upgrade",{requestId="1",machineId="starter",expectedLevel=1,catalogVersion=1})
assert(not shortResult.ok and shortResult.code=="funds" and short.cash==49 and short.level==1 and not short.unlockedOrbit)
