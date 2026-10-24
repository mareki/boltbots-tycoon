--!strict
-- A2 diagnostic baseline adopted from the v0.2 reference; not an accepted M1 implementation.
-- Factory contracts, premium scene and persistence are implemented/verified in later M1 steps.
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("GameConfig"))
local Rules = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("EconomyRules"))
local WorldBuilder = require(script.Parent:WaitForChild("Services"):WaitForChild("WorldBuilder"))

local remotes = Instance.new("Folder")
remotes.Name = "BoltBotsRemotes"
remotes.Parent = ReplicatedStorage
local stateChanged = Instance.new("RemoteEvent")
stateChanged.Name = "StateChanged"
stateChanged.Parent = remotes
local requestUpgrade = Instance.new("RemoteEvent")
requestUpgrade.Name = "RequestUpgrade"
requestUpgrade.Parent = remotes
local getSnapshot = Instance.new("RemoteFunction")
getSnapshot.Name = "GetSnapshot"
getSnapshot.Parent = remotes

local plots = WorldBuilder.Build()
local profiles = {} :: {[Player]: any}
local assignedPlots = {} :: {[Player]: any}
local lastUpgradeRequest = {} :: {[Player]: number}

local function snapshot(player: Player, notice: string?): {[string]: any}
    local profile = profiles[player]
    if not profile then
        return { ready = false, notice = notice or "Waiting for a factory" }
    end
    local price = Rules.upgradePrice(profile.upgradeLevel)
    return {
        ready = true,
        cash = profile.cash,
        robots = profile.robots,
        upgradeLevel = profile.upgradeLevel,
        upgradePrice = price,
        productionSeconds = Rules.cycleSeconds(profile.upgradeLevel),
        cashPerRobot = Config.creditsPerRobot,
        secondsUntilNextRobot = math.max(0, profile.nextProductionAt - os.clock()),
        plotIndex = assignedPlots[player].Index,
        notice = notice,
        version = Config.versionLabel,
    }
end

local function publish(player: Player, notice: string?)
    if player.Parent == Players then
        stateChanged:FireClient(player, snapshot(player, notice))
    end
end

local function relocate(player: Player, plot)
    local function move(character: Model)
        local root = character:WaitForChild("HumanoidRootPart", 10)
        if root and player.Parent == Players then
            character:PivotTo(plot.SpawnCFrame)
        end
    end
    player.CharacterAdded:Connect(move)
    if player.Character then
        task.spawn(move, player.Character)
    end
end

local function handleUpgrade(player: Player, source: string)
    local profile = profiles[player]
    local plot = assignedPlots[player]
    if not profile or not plot then
        return
    end
    local now = os.clock()
    if now - (lastUpgradeRequest[player] or -100) < 0.35 then
        return
    end
    lastUpgradeRequest[player] = now
    if source == "console" then
        local character = player.Character
        local root = character and character:FindFirstChild("HumanoidRootPart")
        if not root or (root.Position - plot.UpgradeConsole.Position).Magnitude > 14 then
            publish(player, "Too far from the upgrade console")
            return
        end
    end
    local success, code = Rules.tryUpgrade(profile)
    if success then
        WorldBuilder.SetLevel(plot, profile.upgradeLevel)
        profile.nextProductionAt = math.min(profile.nextProductionAt, now + Rules.cycleSeconds(profile.upgradeLevel))
        publish(player, "Assembler upgraded")
        print("BOLTBOTS_MACHINE_PURCHASE", player.UserId, profile.upgradeLevel)
    elseif code == "MAX_LEVEL" then
        publish(player, "Maximum upgrade level reached")
    else
        publish(player, "Not enough Factory Cash")
    end
end

for _, plot in ipairs(plots) do
    plot.UpgradePrompt.Triggered:Connect(function(who: Player)
        if assignedPlots[who] == plot then
            handleUpgrade(who, "console")
        end
    end)
end

requestUpgrade.OnServerEvent:Connect(function(player: Player, ...)
    -- Strict no-argument protocol: no forged price, amount or target plot accepted.
    if select("#", ...) ~= 0 then
        return
    end
    handleUpgrade(player, "hud")
end)

getSnapshot.OnServerInvoke = function(player: Player, ...)
    if select("#", ...) ~= 0 then
        return { ready = false, notice = "Bad request" }
    end
    return snapshot(player)
end

local function assignPlayer(player: Player)
    local occupied = {}
    for _, plot in pairs(assignedPlots) do
        occupied[plot.Index] = true
    end
    local plot = nil
    for _, candidate in ipairs(plots) do
        if not occupied[candidate.Index] then
            plot = candidate
            break
        end
    end
    if not plot then
        player:Kick("All factory plots are occupied. Rejoin another server.")
        return
    end
    assignedPlots[player] = plot
    local profile = Rules.newProfile()
    profile.nextProductionAt = os.clock() + Rules.cycleSeconds(profile.upgradeLevel)
    profiles[player] = profile
    WorldBuilder.SetOwner(plot, player.DisplayName)
    WorldBuilder.SetLevel(plot, profile.upgradeLevel)
    relocate(player, plot)
    print("BOLTBOTS_SESSION_START", player.UserId, plot.Index)
    publish(player, "Your first Scout robot is on its way")
end

local function removePlayer(player: Player)
    local plot = assignedPlots[player]
    if plot then
        WorldBuilder.SetOwner(plot, nil)
        WorldBuilder.SetLevel(plot, Config.startingUpgradeLevel)
    end
    profiles[player] = nil
    assignedPlots[player] = nil
    lastUpgradeRequest[player] = nil
    -- This temporary A2 baseline has no persistence. M1 still requires real Save/Rejoin.
end

Players.PlayerAdded:Connect(assignPlayer)
Players.PlayerRemoving:Connect(removePlayer)
for _, player in ipairs(Players:GetPlayers()) do
    task.spawn(assignPlayer, player)
end

task.spawn(function()
    while true do
        local now = os.clock()
        for player, profile in pairs(profiles) do
            if profile.nextProductionAt <= now then
                -- Bound catch-up; prototype has no offline rewards or externally set clocks.
                Rules.awardRobot(profile)
                local plot = assignedPlots[player]
                if plot then
                    WorldBuilder.PlayProductionVisual(plot)
                end
                profile.nextProductionAt = now + Rules.cycleSeconds(profile.upgradeLevel)
                if profile.robots == 1 then
                    print("BOLTBOTS_FIRST_ROBOT", player.UserId)
                    publish(player, "Scout robot complete! Collect cash for an upgrade")
                else
                    publish(player)
                end
            end
        end
        task.wait(0.25)
    end
end)

print("BOLTBOTS_SERVER_BOOT", Config.project, Config.versionLabel)
