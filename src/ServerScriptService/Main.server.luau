--!strict
-- B1 local session adapter. Persistence and purchase commands arrive in B2/B3.
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")
local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared:WaitForChild("GameConfig"))
local Rules = require(Shared:WaitForChild("EconomyRules"))
local WorldBuilder = require(script.Parent:WaitForChild("Services"):WaitForChild("WorldBuilder"))
local plots = WorldBuilder.Build()
local sessions: {[Player]: any} = {}

local remotes = Instance.new("Folder")
remotes.Name = "BoltBotsRemotes"
remotes.Parent = ReplicatedStorage
local stateChanged = Instance.new("RemoteEvent")
stateChanged.Name = "StateChanged"
stateChanged.Parent = remotes
local getSnapshot = Instance.new("RemoteFunction")
getSnapshot.Name = "GetSnapshot"
getSnapshot.Parent = remotes

local function snapshot(player: Player, notice: string?)
    local session = sessions[player]
    if not session then return { ready = false, notice = "Deine Werkstatt wird vorbereitet …" } end
    local profile = session.profile
    local cycle = profile.cycle
    return {
        ready = true, cash = profile.cash, completed = profile.completed,
        unlockedScout = profile.unlockedScout, stateVersion = profile.stateVersion,
        plotIndex = session.plot.Index, cycleStart = if cycle then cycle.startedAt else 0,
        cycleId = if cycle then cycle.id else profile.lastCycleId,
        cycleSeconds = Config.baseCycleSeconds, cashPerRobot = Config.creditsPerRobot,
        productionActive = cycle ~= nil, notice = notice,
        saveStatus = "local_session_only", version = Config.versionLabel,
    }
end
local function publish(player: Player, notice: string?)
    if player.Parent == Players then stateChanged:FireClient(player, snapshot(player, notice)) end
end
local function startCycle(session)
    local ok, reason = Rules.beginCycle(session.profile, Workspace:GetServerTimeNow())
    local cycle = session.profile.cycle
    if ok and cycle then
        session.plot.Model:SetAttribute("CycleStart", cycle.startedAt)
        session.plot.Model:SetAttribute("CycleSeconds", Config.baseCycleSeconds)
        session.plot.Model:SetAttribute("CycleId", cycle.id)
        session.plot.Model:SetAttribute("Active", true)
    else
        session.plot.Model:SetAttribute("Active", false)
        warn("BOLTBOTS_PRODUCTION_PAUSED", reason)
    end
end

getSnapshot.OnServerInvoke = function(player: Player, ...)
    if select("#", ...) ~= 0 then return { ready = false, notice = "Ungültige Anfrage." } end
    -- Query only. There is deliberately no client production-completion remote.
    return snapshot(player)
end

local function assignPlayer(player: Player)
    if sessions[player] then return end
    local plot = nil
    for _, candidate in ipairs(plots) do
        if not candidate.Occupied then plot = candidate; break end
    end
    if not plot then player:Kick("Alle Werkstätten sind belegt. Bitte einem anderen Server beitreten."); return end
    plot.Occupied = true
    player.RespawnLocation = plot.Spawn
    local session = { profile = Rules.newProfile(), plot = plot }
    sessions[player] = session
    WorldBuilder.SetOccupied(plot, true)
    local function relocate(character: Model)
        local root = character:WaitForChild("HumanoidRootPart", 10)
        if root and sessions[player] == session then character:PivotTo(plot.SpawnCFrame) end
    end
    session.characterConnection = player.CharacterAdded:Connect(relocate)
    if player.Character then task.spawn(relocate, player.Character) end
    startCycle(session)
    publish(player)
    print("BOLTBOTS_SESSION_START", "slot=" .. plot.Index, Config.versionLabel, "local_session_only")
end
local function removePlayer(player: Player)
    local session = sessions[player]
    if not session then return end
    Rules.stop(session.profile)
    session.characterConnection:Disconnect()
    WorldBuilder.SetOccupied(session.plot, false)
    session.plot.Occupied = false
    sessions[player] = nil
    print("BOLTBOTS_SESSION_END", "slot=" .. session.plot.Index, "not_persisted")
end
Players.PlayerAdded:Connect(assignPlayer)
Players.PlayerRemoving:Connect(removePlayer)
for _, player in ipairs(Players:GetPlayers()) do assignPlayer(player) end

task.spawn(function()
    while true do
        local now = Workspace:GetServerTimeNow()
        for player, session in pairs(sessions) do
            local cycle = session.profile.cycle
            if cycle and now >= cycle.completesAt then
                local ok, reason = Rules.completeCycle(session.profile, cycle.id, now)
                if ok then
                    local profile = session.profile
                    if profile.completed <= 3 or profile.completed % 10 == 0 then
                        print("BOLTBOTS_COMPLETE", "cycle=" .. cycle.id, "cash=" .. profile.cash,
                            "completed=" .. profile.completed, "scout=" .. tostring(profile.unlockedScout))
                    end
                    if profile.completed == 1 then print("BOLTBOTS_ROBOT_UNLOCKED", "scout") end
                    startCycle(session)
                    publish(player, if profile.completed == 1 then "Scout entdeckt! +25 Factory Cash" else nil)
                else
                    Rules.stop(session.profile)
                    session.plot.Model:SetAttribute("Active", false)
                    publish(player, "Produktion pausiert: " .. reason)
                end
            end
        end
        task.wait(0.1)
    end
end)
print("BOLTBOTS_SERVER_BOOT", Config.project, Config.versionLabel)
