-- Explicit diagnostic, run in Studio's SERVER command bar for the authorized private target.
-- Synthetic fixture only; no player profile is read or changed.
assert(game.GameId==10772906084 and game.PlaceId==112662761038118)
local backend=game:GetService("DataStoreService"):GetDataStore("BoltBots_B3_20261025")
local Store=require(game.ServerScriptService.Server.Services.ProfileStore)
local function guid() return game:GetService("HttpService"):GenerateGUID(false) end
local key="fixture_schema1_session_b3_20261025"
local seed={schemaVersion=1,revision=4,data={cash=75,completed=5,lifetimeEarned=125,level=2,unlockedScout=true,selectedDesign="orbit"}}
local seeded=backend:UpdateAsync(key,function(old) assert(old==nil,"fixture already exists; do not overwrite");return seed end)
assert(seeded.revision==4)
local a=Store.new(backend,os.time,guid)
local h=a.handle(key)
local ok,code,data=a.open(h)
assert(ok and code=="migrated" and data.cash==75 and data.unlockedOrbit)
local competing=a.handle(key)
local other,reason=a.open(competing)
assert(not other and reason=="session_locked")
local once=true
local ambiguous={}
function ambiguous:UpdateAsync(k,transform)
    local result=backend:UpdateAsync(k,transform)
    if once then once=false;error("DIAGNOSTIC acknowledgement dropped AFTER actual Roblox commit") end
    return result
end
local retryAdapter=Store.new(ambiguous,os.time,guid)
data.cash=100
assert(not retryAdapter.save(h,data,false))
assert(h.revision==4 and h.pending~=nil)
assert(retryAdapter.save(h,data,false))
assert(h.revision==5)
assert(a.save(h,data,true))
local joined,joinCode,restored=a.open(competing)
assert(joined and restored.cash==100 and restored.selectedDesign=="orbit")
assert(a.save(competing,restored,true))
local record=backend:GetAsync(key)
assert(record.schemaVersion==2 and record.revision==7 and record.session==nil and record.data.cash==100)
print("BOLTBOTS_B3_REAL_FIXTURE",code,reason,"ambiguous_write_once",record.schemaVersion,record.revision,record.data.cash,record.data.selectedDesign,"released")
