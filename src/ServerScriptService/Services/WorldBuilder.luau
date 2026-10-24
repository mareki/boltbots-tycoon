--!strict
-- Server-created geometry: self-contained, owned, non-commercial prototype assets.
local Workspace = game:GetService("Workspace")
local Config = require(game:GetService("ReplicatedStorage"):WaitForChild("Shared"):WaitForChild("GameConfig"))

local WorldBuilder = {}

local COLORS = {
    floor = Color3.fromRGB(18, 36, 65),
    steel = Color3.fromRGB(38, 61, 90),
    cyan = Color3.fromRGB(72, 216, 244),
    amber = Color3.fromRGB(255, 206, 83),
    coral = Color3.fromRGB(255, 149, 107),
    white = Color3.fromRGB(244, 248, 255),
    green = Color3.fromRGB(90, 217, 166),
}

local function part(parent: Instance, name: string, size: Vector3, position: Vector3, color: Color3, material: Enum.Material?): Part
    local item = Instance.new("Part")
    item.Name = name
    item.Size = size
    item.Position = position
    item.Anchored = true
    item.Color = color
    item.Material = material or Enum.Material.SmoothPlastic
    item.Parent = parent
    return item
end

local function billboard(adornee: BasePart, name: string, content: string, width: number, height: number): TextLabel
    local gui = Instance.new("BillboardGui")
    gui.Name = name
    gui.Size = UDim2.fromOffset(width, height)
    gui.StudsOffsetWorldSpace = Vector3.new(0, 3.5, 0)
    gui.AlwaysOnTop = true
    gui.Adornee = adornee
    gui.Parent = adornee
    local text = Instance.new("TextLabel")
    text.Name = "Label"
    text.Size = UDim2.fromScale(1, 1)
    text.BackgroundTransparency = 0.12
    text.BackgroundColor3 = COLORS.floor
    text.TextColor3 = COLORS.white
    text.TextStrokeTransparency = 0.7
    text.Text = content
    text.TextScaled = true
    text.Font = Enum.Font.GothamBold
    text.Parent = gui
    local corner = Instance.new("UICorner")
    corner.CornerRadius = UDim.new(0, 9)
    corner.Parent = text
    return text
end

local function plotGeometry(root: Instance, index: number, origin: Vector3)
    local model = Instance.new("Model")
    model.Name = "FactoryPlot_" .. tostring(index)
    model.Parent = root
    part(model, "FactoryPlatform", Vector3.new(74, 1, 65), origin, COLORS.steel)
    part(model, "FactoryAccent", Vector3.new(72, 0.3, 1), origin + Vector3.new(0, 0.7, -30), COLORS.cyan, Enum.Material.Neon)
    for x = -24, 24, 24 do
        part(model, "FloorLane", Vector3.new(4, 0.12, 46), origin + Vector3.new(x, 0.63, 0), COLORS.floor)
    end
    local input = part(model, "InputHopper", Vector3.new(9, 6, 9), origin + Vector3.new(-18, 3.5, -4), COLORS.coral)
    local assembler = part(model, "RobotAssembler", Vector3.new(11, 8, 12), origin + Vector3.new(0, 4.5, -4), COLORS.amber)
    local packager = part(model, "PackagingStation", Vector3.new(9, 6, 9), origin + Vector3.new(18, 3.5, -4), COLORS.green)
    part(model, "Conveyor", Vector3.new(37, 0.65, 5), origin + Vector3.new(0, 1.1, -4), COLORS.floor)
    for x = -15, 15, 5 do
        part(model, "ConveyorGlow", Vector3.new(2, 0.12, 4.8), origin + Vector3.new(x, 1.48, -4), COLORS.cyan, Enum.Material.Neon)
    end
    part(model, "AssemblerIndicator", Vector3.new(7, 0.45, 0.45), assembler.Position + Vector3.new(0, 2.5, -6.25), COLORS.white, Enum.Material.Neon)
    part(model, "HopperIndicator", Vector3.new(5, 0.45, 0.45), input.Position + Vector3.new(0, 1.5, -4.6), COLORS.amber, Enum.Material.Neon)
    local upgrade = part(model, "UpgradeConsole", Vector3.new(6, 4, 5), origin + Vector3.new(18, 2.5, 16), COLORS.cyan)
    local prompt = Instance.new("ProximityPrompt")
    prompt.Name = "UpgradePrompt"
    prompt.ActionText = "Upgrade assembler"
    prompt.ObjectText = "BoltBots console"
    prompt.MaxActivationDistance = 12
    prompt.HoldDuration = 0.25
    prompt.RequiresLineOfSight = false
    prompt.Enabled = false
    prompt.Parent = upgrade
    local ownerSign = part(model, "OwnerSign", Vector3.new(14, 5, 1), origin + Vector3.new(-20, 4.5, 29), COLORS.floor)
    local ownerLabel = billboard(ownerSign, "OwnerBillboard", "AVAILABLE FACTORY", 220, 50)
    local levelLabel = billboard(assembler, "LevelBillboard", "ASSEMBLER L1", 176, 44)
    local pedestal = part(model, "RobotShowcasePedestal", Vector3.new(7, 1.5, 7), origin + Vector3.new(0, 1.3, 19), COLORS.cyan)
    part(model, "ShowcaseLight", Vector3.new(5, 0.15, 5), pedestal.Position + Vector3.new(0, 0.85, 0), COLORS.white, Enum.Material.Neon)
    return {
        Index = index,
        Model = model,
        Origin = origin,
        SpawnCFrame = CFrame.new(origin + Vector3.new(-28, 6, 18)),
        OwnerLabel = ownerLabel,
        LevelLabel = levelLabel,
        UpgradeConsole = upgrade,
        UpgradePrompt = prompt,
        StartPosition = input.Position + Vector3.new(0, 1.7, 0),
        EndPosition = packager.Position + Vector3.new(0, 1.7, 0),
    }
end

function WorldBuilder.Build()
    local old = Workspace:FindFirstChild("BoltBotsWorld")
    if old then
        old:Destroy()
    end
    local root = Instance.new("Folder")
    root.Name = "BoltBotsWorld"
    root.Parent = Workspace
    part(root, "Ground", Vector3.new(190, 1, 190), Vector3.new(0, -1.1, 0), COLORS.floor)
    local spawn = Instance.new("SpawnLocation")
    spawn.Name = "LobbySpawn"
    spawn.Size = Vector3.new(16, 1, 16)
    spawn.Position = Vector3.new(0, 1, 0)
    spawn.Anchored = true
    spawn.Neutral = true
    spawn.Color = COLORS.amber
    spawn.Parent = root
    local plots = {}
    local locations = {
        Vector3.new(-46, 0, -48),
        Vector3.new(46, 0, -48),
        Vector3.new(-46, 0, 48),
        Vector3.new(46, 0, 48),
    }
    for index = 1, Config.maxPlots do
        table.insert(plots, plotGeometry(root, index, locations[index]))
    end
    local lighting = game:GetService("Lighting")
    lighting.ClockTime = 14
    lighting.Brightness = 2
    lighting.Ambient = Color3.fromRGB(115, 155, 202)
    return plots
end

function WorldBuilder.SetOwner(plot, name: string?)
    plot.OwnerLabel.Text = if name then (name .. "'s factory") else "AVAILABLE FACTORY"
    plot.UpgradePrompt.Enabled = name ~= nil
end

function WorldBuilder.SetLevel(plot, level: number)
    plot.LevelLabel.Text = "ASSEMBLER L" .. tostring(level)
end

function WorldBuilder.PlayProductionVisual(plot)
    -- Visuals only: rewards are credited independently by server EconomyRules.
    local model = Instance.new("Model")
    model.Name = "ProducedScoutVisual"
    model.Parent = plot.Model
    local start = plot.StartPosition
    part(model, "Body", Vector3.new(2.3, 2.4, 1.8), start, COLORS.white)
    local head = part(model, "Head", Vector3.new(2.7, 2, 2), start + Vector3.new(0, 2.0, 0), COLORS.white)
    part(model, "Visor", Vector3.new(2.1, 0.75, 0.14), head.Position + Vector3.new(0, 0, -1.07), COLORS.cyan, Enum.Material.Neon)
    part(model, "LeftLeg", Vector3.new(0.7, 1.1, 0.8), start + Vector3.new(-0.7, -1.7, 0), COLORS.steel)
    part(model, "RightLeg", Vector3.new(0.7, 1.1, 0.8), start + Vector3.new(0.7, -1.7, 0), COLORS.steel)
    -- Set a stable root pivot before moving the whole model.
    model.PrimaryPart = model:FindFirstChild("Body") :: BasePart
    model:PivotTo(CFrame.new(start))
    task.spawn(function()
        for step = 1, 18 do
            if not model.Parent then
                return
            end
            local t = step / 18
            local p = start:Lerp(plot.EndPosition, t)
            model:PivotTo(CFrame.new(p))
            task.wait(0.045)
        end
        model:Destroy()
    end)
end

return WorldBuilder
