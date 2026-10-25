assert(game:GetService("RunService"):IsStudio() and not game:GetService("RunService"):IsRunning())
assert(game.GameId==10772906084 and game.PlaceId==112662761038118)
assert(not string.find(game.ServerScriptService.Server.Main.Source,"fixture_b5_gameplay",1,true),"temporary fixture key remains")
assert(not game:FindFirstChild("B4TemporaryProbe",true),"temporary B4 probe remains")
assert(workspace:GetAttribute("B4ProbeRun")==nil and workspace:GetAttribute("B4ProbeClients")==nil)
assert(workspace:GetAttribute("B3RejectStoreWrites")==nil)
settings().Rendering.QualityLevel=Enum.QualityLevel.Automatic
print("BOLTBOTS_B5_FINAL_CLEAN",game.GameId,game.PlaceId,settings().Rendering.QualityLevel,game:GetService("RunService"):IsRunning())
