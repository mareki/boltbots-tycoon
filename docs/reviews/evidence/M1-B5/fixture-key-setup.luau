-- Studio-only test setup: change only the key of this private session.
-- No existing profile is replaced/deleted, no cash/rights/timing is injected.
assert(game.GameId==10772906084 and game.PlaceId==112662761038118)
assert(game:GetService("RunService"):IsStudio() and not game:GetService("RunService"):IsRunning())
local main=game.ServerScriptService.Server.Main
local needle='store.handle("player_"..player.UserId)'
local a,b=string.find(main.Source,needle,1,true)
assert(a and not string.find(main.Source,needle,b+1,true))
main.Source=string.sub(main.Source,1,a-1)..'store.handle("fixture_b5_gameplay_20261025_"..player.UserId)'..string.sub(main.Source,b+1)
print("BOLTBOTS_B5_FIXTURE_KEY_READY", "fixture_b5_gameplay_20261025_", "one source substitution; personal player_ key untouched")
