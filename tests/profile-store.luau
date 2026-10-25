--!strict
local Schema=require("./ProfileSchema")
local Store=require("./ProfileStore")
local Rules=require("./EconomyRules")
local records:any={}
local now=1000
local id=0
local before=false
local after=false
local callbacks=0
local backend={}
function backend:UpdateAsync(key,callback)
    if before then error("injected request failure") end
    -- Roblox may invoke the transform repeatedly; discarded attempts have no side effects.
    local raw=records[key]
    local discarded=callback(raw);callbacks+=1
    if raw then assert(raw~=discarded,"transform must return a new record") end
    local nextRecord=callback(raw);callbacks+=1
    if nextRecord then records[key]=nextRecord end
    if after then error("injected lost acknowledgement") end
    return nextRecord
end
local function guid() id+=1;return "test-"..id end
local a=Store.new(backend,function() return now end,guid)
local h=a.handle("owner")
before=true
assert(not a.open(h));assert(records.owner==nil,"load failure must never create defaults")
before=false
local ok,code,data=a.open(h);assert(ok and code=="new" and data.cash==0)
local second=a.handle("owner");local other,locked=a.open(second)
assert(not other and locked=="session_locked")
local p=Rules.newProfile();p.cash=75;p.lifetimeEarned=125;p.completed=5;p.level=2;p.unlockedOrbit=true;p.unlockedScout=true;p.selectedDesign="orbit"
after=true
assert(not a.save(h,p,false));assert(h.revision==0 and records.owner.revision==1)
local pending=h.pending
p.cash=100 -- callers freeze, but the adapter itself must retain the bound snapshot
assert(pending.data.cash==75)
after=false
assert(a.save(h,p,false));assert(h.revision==1 and records.owner.data.cash==75 and h.pending==nil)
assert(a.save(h,p,false));assert(h.revision==2 and records.owner.data.cash==100)
-- Repetition after a lost acknowledgement cannot revive an expired/lost writer.
after=true
assert(not a.save(h,p,false));after=false
now+=91
local claimed=a.open(second);assert(claimed)
local retry,lost=a.save(h,p,false);assert(not retry and lost=="lease_lost")
assert(records.owner.session.token==second.token)
-- Stale revision cannot overwrite a newer record even under the same token.
second.revision-=1
local stale,conflict=a.save(second,p,false);assert(not stale and conflict=="revision_conflict")
second.pending=nil;second.revision=records.owner.revision
assert(a.save(second,p,true));assert(records.owner.session==nil)
local h3=a.handle("owner");local joined,_,restored=a.open(h3)
assert(joined and restored.cash==100 and restored.level==2 and restored.selectedDesign=="orbit")
-- Schema1 migration is explicit; unknown/corrupt versions preserve their original bytes.
local old=Schema.copyData(p);old.unlockedOrbit=nil
records.migrate={schemaVersion=1,revision=4,data=old}
local mh=a.handle("migrate");local migrated,mc,md=a.open(mh)
assert(migrated and mc=="migrated" and md.unlockedOrbit and records.migrate.schemaVersion==2)
for _,fixture in ipairs({{schemaVersion=99,revision=0,data=Schema.copyData(p)},
    {schemaVersion=2,revision=0,data={cash=0}},
    {schemaVersion=2,revision=0,data=Schema.copyData(p),session={token="foreign",expiresAt="bad"}}}) do
    records.invalid=fixture
    assert(not a.open(a.handle("invalid")));assert(records.invalid==fixture)
end
local invalid=Schema.copyData(p);invalid.cash=0/0;assert(not Schema.validData(invalid))
invalid=Schema.copyData(p);invalid.level=1;assert(not Schema.validData(invalid))
-- Ambiguous release is idempotent, but cannot take over a subsequent active claimant.
after=true
assert(not a.save(h3,p,true));after=false
assert(a.save(h3,p,true));assert(records.owner.session==nil)
local fresh=a.handle("owner");assert(a.open(fresh))
assert(records.owner.session.token==fresh.token)
print("B3 profile tests OK: migration/corruption, repeated callbacks, failed load, ambiguous save/release, frozen snapshot, exclusive/expired lease, revision conflict and rejoin; callbacks="..callbacks)
