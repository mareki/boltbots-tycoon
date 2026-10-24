--!strict
-- Mobile-aware proof-of-concept HUD; all economy calculations happen on the server.
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local player = Players.LocalPlayer
local remotes = ReplicatedStorage:WaitForChild("BoltBotsRemotes")
local stateChanged = remotes:WaitForChild("StateChanged") :: RemoteEvent
local requestUpgrade = remotes:WaitForChild("RequestUpgrade") :: RemoteEvent
local getSnapshot = remotes:WaitForChild("GetSnapshot") :: RemoteFunction

local NAVY = Color3.fromRGB(16, 27, 53)
local PANEL = Color3.fromRGB(23, 43, 77)
local CYAN = Color3.fromRGB(72, 216, 244)
local AMBER = Color3.fromRGB(255, 206, 83)
local WHITE = Color3.fromRGB(244, 248, 255)
local MUTED = Color3.fromRGB(185, 200, 219)

local gui = Instance.new("ScreenGui")
gui.Name = "BoltBotsHUD"
gui.IgnoreGuiInset = false
gui.ResetOnSpawn = false
gui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
gui.Parent = player:WaitForChild("PlayerGui")

local function round(target: Instance, radius: number)
    local corner = Instance.new("UICorner")
    corner.CornerRadius = UDim.new(0, radius)
    corner.Parent = target
end

local function text(parent: Instance, name: string, content: string, color: Color3, font: Enum.Font, size: number): TextLabel
    local label = Instance.new("TextLabel")
    label.Name = name
    label.BackgroundTransparency = 1
    label.Text = content
    label.TextColor3 = color
    label.TextSize = size
    label.TextWrapped = true
    label.Font = font
    label.TextXAlignment = Enum.TextXAlignment.Left
    label.Parent = parent
    return label
end

local function panel(name: string, width: number, height: number, bottom: boolean): Frame
    local frame = Instance.new("Frame")
    frame.Name = name
    frame.Size = UDim2.new(width, 0, 0, height)
    frame.AnchorPoint = Vector2.new(0.5, if bottom then 1 else 0)
    frame.Position = UDim2.new(0.5, 0, if bottom then 1 else 0, if bottom then -24 else 16)
    frame.BackgroundColor3 = PANEL
    frame.BorderSizePixel = 0
    frame.Parent = gui
    round(frame, 15)
    local constraint = Instance.new("UISizeConstraint")
    constraint.MaxSize = Vector2.new(640, height)
    constraint.Parent = frame
    return frame
end

local top = panel("TopHUD", 0.94, 100, false)
local name = text(top, "GameName", "BOLTBOTS  /  FACTORY 01", CYAN, Enum.Font.GothamBold, 15)
name.Size = UDim2.new(1, -28, 0, 24)
name.Position = UDim2.fromOffset(14, 9)
local cash = text(top, "Cash", "Factory Cash: 0", AMBER, Enum.Font.GothamBold, 21)
cash.Size = UDim2.new(0.66, -10, 0, 30)
cash.Position = UDim2.fromOffset(14, 36)
local production = text(top, "Production", "1 robot / 7s", MUTED, Enum.Font.Gotham, 15)
production.Size = UDim2.new(0.36, -14, 0, 28)
production.Position = UDim2.new(0.64, 0, 0, 37)
local progress = text(top, "Progress", "Robots built: 0", WHITE, Enum.Font.Gotham, 13)
progress.Size = UDim2.new(1, -28, 0, 20)
progress.Position = UDim2.fromOffset(14, 71)

local bottom = panel("UpgradePanel", 0.94, 116, true)
local objective = text(bottom, "Objective", "First goal: assemble your Scout robot", WHITE, Enum.Font.GothamBold, 15)
objective.Size = UDim2.new(1, -22, 0, 42)
objective.Position = UDim2.fromOffset(12, 7)
local button = Instance.new("TextButton")
button.Name = "UpgradeButton"
button.Size = UDim2.new(0.65, -16, 0, 48)
button.Position = UDim2.new(0, 12, 1, -58)
button.BackgroundColor3 = CYAN
button.TextColor3 = NAVY
button.Font = Enum.Font.GothamBold
button.TextSize = 16
button.TextWrapped = true
button.Text = "UPGRADE ASSEMBLER"
button.Parent = bottom
round(button, 10)
local timerText = text(bottom, "Timer", "Next robot: --", MUTED, Enum.Font.Gotham, 13)
timerText.Size = UDim2.new(0.35, -8, 0, 48)
timerText.Position = UDim2.new(0.65, 0, 1, -56)

local toast = text(gui, "Toast", "", WHITE, Enum.Font.GothamBold, 16)
toast.BackgroundColor3 = NAVY
toast.BackgroundTransparency = 0.06
toast.TextXAlignment = Enum.TextXAlignment.Center
toast.AnchorPoint = Vector2.new(0.5, 0)
toast.Position = UDim2.new(0.5, 0, 0, 128)
toast.Size = UDim2.new(0.88, 0, 0, 46)
toast.Visible = false
round(toast, 10)
local toastConstraint = Instance.new("UISizeConstraint")
toastConstraint.MaxSize = Vector2.new(600, 46)
toastConstraint.Parent = toast

local lastState: {[string]: any}? = nil
local lastNotice = ""
local localNextAt = 0
local function show(state: {[string]: any})
    if state.ready ~= true then
        objective.Text = state.notice or "Connecting to your factory..."
        return
    end
    lastState = state
    cash.Text = "Factory Cash: " .. tostring(state.cash)
    production.Text = string.format("Robot / %.1fs", state.productionSeconds)
    progress.Text = "Robots built: " .. tostring(state.robots) .. "  |  Assembler L" .. tostring(state.upgradeLevel)
    if state.robots == 0 then
        objective.Text = "WATCH: Your first Scout robot is being built"
    elseif state.upgradePrice then
        objective.Text = "NEXT: Upgrade your assembler to make robots faster"
    else
        objective.Text = "MAX LEVEL: Build more robots and enjoy your factory"
    end
    localNextAt = os.clock() + math.max(0, state.secondsUntilNextRobot or 0)
    if state.upgradePrice then
        button.Text = "UPGRADE - " .. tostring(state.upgradePrice) .. " Cash"
        button.Active = true
        button.AutoButtonColor = true
        button.BackgroundColor3 = CYAN
    else
        button.Text = "MAX LEVEL"
        button.Active = false
        button.AutoButtonColor = false
        button.BackgroundColor3 = MUTED
    end
    if type(state.notice) == "string" and state.notice ~= "" and state.notice ~= lastNotice then
        toast.Text = state.notice
        toast.Visible = true
        lastNotice = state.notice
        local captured = lastNotice
        task.delay(3, function()
            if lastNotice == captured then
                toast.Visible = false
            end
        end)
    end
end

button.Activated:Connect(function()
    if lastState and lastState.upgradePrice then
        requestUpgrade:FireServer()
    end
end)

stateChanged.OnClientEvent:Connect(function(incoming)
    if type(incoming) == "table" then
        show(incoming)
    end
end)

local success, initial = pcall(function()
    return getSnapshot:InvokeServer()
end)
if success and type(initial) == "table" then
    show(initial)
else
    objective.Text = "Could not fetch factory state. Rejoin to retry."
end

task.spawn(function()
    while gui.Parent do
        if lastState then
            local remaining = math.max(0, math.ceil(localNextAt - os.clock()))
            timerText.Text = "Next robot: " .. tostring(remaining) .. "s"
        end
        task.wait(0.5)
    end
end)

print("BOLTBOTS_CLIENT_BOOT")
