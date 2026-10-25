--!strict
-- Presentation reads authoritative snapshots/timestamps; it never awards cash or design rights.
local Players=game:GetService("Players")
local ReplicatedStorage=game:GetService("ReplicatedStorage")
local RunService=game:GetService("RunService")
local UserInputService=game:GetService("UserInputService")
local GuiService=game:GetService("GuiService")
local ContextActionService=game:GetService("ContextActionService")
local Workspace=game:GetService("Workspace")
local player=Players.LocalPlayer
local controls=require(player:WaitForChild("PlayerScripts"):WaitForChild("PlayerModule")):GetControls()
local Scout=require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("ScoutModel"))
local Orbit=require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("OrbitModel"))
local builders={scout=Scout,orbit=Orbit}
local remotes=ReplicatedStorage:WaitForChild("BoltBotsRemotes")
local changed=remotes:WaitForChild("StateChanged") :: RemoteEvent
local query=remotes:WaitForChild("GetSnapshot") :: RemoteFunction
local command=remotes:WaitForChild("Command") :: RemoteFunction
local C={navy=Color3.fromRGB(16,27,53),panel=Color3.fromRGB(23,43,63),cyan=Color3.fromRGB(72,216,244),
    amber=Color3.fromRGB(255,206,83),white=Color3.fromRGB(244,248,255),muted=Color3.fromRGB(185,200,219)}
local gui=Instance.new("ScreenGui");gui.Name="BoltBotsHUD";gui.ResetOnSpawn=false;gui.IgnoreGuiInset=false
 gui.ZIndexBehavior=Enum.ZIndexBehavior.Sibling;gui.Parent=player:WaitForChild("PlayerGui")
local function corner(object,radius)
    local c=Instance.new("UICorner");c.CornerRadius=UDim.new(0,radius);c.Parent=object
end
local function frame(parent,name,size,position,color)
    local f=Instance.new("Frame");f.Name=name;f.Size=size;f.Position=position;f.BackgroundColor3=color or C.panel
    f.BorderSizePixel=0;f.Parent=parent;corner(f,16);return f
end
local function text(parent,name,value,size,position,textSize,color)
    local t=Instance.new("TextLabel");t.Name=name;t.Text=value;t.Size=size;t.Position=position
    t.BackgroundTransparency=1;t.TextColor3=color or C.white;t.TextSize=textSize;t.Font=Enum.Font.GothamMedium
    t.TextXAlignment=Enum.TextXAlignment.Left;t.TextYAlignment=Enum.TextYAlignment.Center;t.TextWrapped=true;t.Parent=parent;return t
end
local function button(parent,name,value,size,position,color)
    local b=Instance.new("TextButton");b.Name=name;b.Text=value;b.Size=size;b.Position=position
    b.BackgroundColor3=color or C.panel;b.TextColor3=if color then C.navy else C.white;b.Font=Enum.Font.GothamBold
    b.TextSize=15;b.TextWrapped=true;b.BorderSizePixel=0;b.AutoButtonColor=true;b.Selectable=true;b.Parent=parent;corner(b,13)
    local stroke=Instance.new("UIStroke");stroke.ApplyStrokeMode=Enum.ApplyStrokeMode.Border;stroke.Thickness=2;stroke.Color=C.white;stroke.Enabled=false;stroke.Parent=b
    b.SelectionGained:Connect(function() stroke.Enabled=true end)
    b.SelectionLost:Connect(function() stroke.Enabled=false end)
    return b
end
local header=frame(gui,"Header",UDim2.fromOffset(310,84),UDim2.fromOffset(16,10));header.BackgroundTransparency=0.08
local brand=text(gui,"Brand","BOLT  BOTS",UDim2.fromOffset(230,32),UDim2.fromOffset(22,12),24,C.white)
brand.Font=Enum.Font.GothamBlack
local preview=text(gui,"SessionNotice","Lokale Vorschau · ohne Speichern",UDim2.fromOffset(290,23),UDim2.fromOffset(22,45),14,C.muted)
local cashPanel=frame(gui,"CashPanel",UDim2.fromOffset(210,72),UDim2.new(1,-232,0,12))
local cashCaption=text(cashPanel,"CashCaption","FACTORY CASH",UDim2.new(1,-28,0,20),UDim2.fromOffset(14,8),14,C.muted)
local cash=text(cashPanel,"Cash","—",UDim2.new(1,-28,0,36),UDim2.fromOffset(14,27),29,C.amber);cash.Font=Enum.Font.GothamBold
local goal=frame(gui,"Goal",UDim2.fromOffset(310,88),UDim2.fromOffset(22,86))
local eyebrow=text(goal,"Eyebrow","DEIN ERSTER ROBOTER",UDim2.new(1,-28,0,20),UDim2.fromOffset(14,10),14,C.cyan)
local objective=text(goal,"Objective","Sieh deinem ersten Scout zu.",UDim2.new(1,-28,0,42),UDim2.fromOffset(14,31),17)
local upgradeButton=button(gui,"Upgrade","Assembler ausbauen",UDim2.fromOffset(310,44),UDim2.fromOffset(22,204),C.amber)
local production=frame(gui,"Production",UDim2.fromOffset(310,65),UDim2.new(0.5,-155,1,-142))
local phase=text(production,"Phase","Werkstatt wird vorbereitet …",UDim2.new(1,-28,0,27),UDim2.fromOffset(14,7),15)
local progressTrack=frame(production,"Track",UDim2.new(1,-28,0,5),UDim2.fromOffset(14,43),Color3.fromRGB(57,77,94))
local progressFill=frame(progressTrack,"Fill",UDim2.fromScale(0,1),UDim2.fromScale(0,0),C.cyan)
local nav=frame(gui,"Navigation",UDim2.fromOffset(430,54),UDim2.new(0.5,-215,1,-68),C.navy)
local collectionButton=button(nav,"Collection","Sammlung  0/2",UDim2.fromOffset(144,44),UDim2.fromOffset(5,5),C.cyan)
local cameraButton=button(nav,"Camera","Erkunden",UDim2.fromOffset(122,44),UDim2.fromOffset(154,5))
local motionButton=button(nav,"Motion","Bewegung: an",UDim2.fromOffset(144,44),UDim2.fromOffset(281,5))
local reward=frame(gui,"Reward",UDim2.fromOffset(360,62),UDim2.new(0.5,-180,0,92),C.panel);reward.Visible=false
local rewardText=text(reward,"RewardText","Scout entdeckt!  +25 Cash",UDim2.new(1,-24,1,0),UDim2.fromOffset(12,0),19,C.amber)
rewardText.TextXAlignment=Enum.TextXAlignment.Center;rewardText.Font=Enum.Font.GothamBold

local shade=frame(gui,"CollectionOverlay",UDim2.fromScale(1,1),UDim2.fromScale(0,0),C.navy)
shade.BackgroundTransparency=0.2;shade.Visible=false;shade.ZIndex=10;shade.Active=true
local card=frame(shade,"ScoutCard",UDim2.fromOffset(520,620),UDim2.new(0.5,-260,0.5,-310),C.panel);card.ZIndex=11
local close=button(card,"Close","×",UDim2.fromOffset(46,46),UDim2.new(1,-58,0,12));close.ZIndex=13;close.TextSize=28
local collectionTitle=text(card,"CollectionTitle","DEINE SAMMLUNG",UDim2.new(1,-90,0,30),UDim2.fromOffset(24,19),16,C.cyan);collectionTitle.ZIndex=12
local portrait=Instance.new("ViewportFrame");portrait.Name="ScoutPortrait";portrait.Size=UDim2.new(1,-36,0,380)
portrait.Position=UDim2.fromOffset(18,63);portrait.BackgroundColor3=C.navy;portrait.BorderSizePixel=0;portrait.ZIndex=12;portrait.Parent=card;corner(portrait,20)
portrait.Ambient=Color3.fromRGB(165,188,207);portrait.LightColor=Color3.fromRGB(255,242,215);portrait.LightDirection=Vector3.new(-1,-1,-1)
local portraitWorld=Instance.new("WorldModel");portraitWorld.Parent=portrait
local portraitBot=Scout.Build(portraitWorld,1)
local portraitCamera=Instance.new("Camera");portraitCamera.FieldOfView=34;portraitCamera.CFrame=CFrame.lookAt(Vector3.new(-4.8,4.5,13),Vector3.new(0,3.2,0))
portraitCamera.Parent=portrait;portrait.CurrentCamera=portraitCamera
local scoutTitle=text(card,"ScoutName","SCOUT",UDim2.new(1,-48,0,40),UDim2.fromOffset(24,450),30);scoutTitle.Font=Enum.Font.GothamBlack;scoutTitle.ZIndex=12
local scoutStatus=text(card,"ScoutStatus","Noch nicht entdeckt",UDim2.new(1,-48,0,28),UDim2.fromOffset(24,490),17,C.amber);scoutStatus.ZIndex=12
local scoutDescription=text(card,"ScoutDescription","Dein neugieriger kleiner Werkstattfreund.\nSchließe die erste Produktion ab.",UDim2.new(1,-48,0,64),UDim2.fromOffset(24,528),16,C.muted);scoutDescription.ZIndex=12

local scoutChoice=button(card,"ScoutChoice","Scout",UDim2.fromOffset(225,44),UDim2.fromOffset(24,62));scoutChoice.ZIndex=13
local orbitChoice=button(card,"OrbitChoice","Orbit · L2",UDim2.fromOffset(225,44),UDim2.fromOffset(267,62));orbitChoice.ZIndex=13
local selectButton=button(card,"Produce","Ab nächstem Zyklus produzieren",UDim2.new(1,-48,0,44),UDim2.new(0,24,1,-56),C.cyan);selectButton.ZIndex=13
local upgradeCard=frame(shade,"UpgradeCard",UDim2.fromOffset(520,340),UDim2.new(0.5,-260,0.5,-170),C.panel);upgradeCard.ZIndex=11;upgradeCard.Visible=false
local upgradeClose=button(upgradeCard,"CloseUpgrade","×",UDim2.fromOffset(46,46),UDim2.new(1,-58,0,12));upgradeClose.ZIndex=13;upgradeClose.TextSize=28
local upgradeTitle=text(upgradeCard,"UpgradeTitle","DEINE NÄCHSTE STUFE",UDim2.new(1,-100,0,32),UDim2.fromOffset(24,20),19,C.amber)
local upgradeLevel=text(upgradeCard,"UpgradeLevel","ASSEMBLER  L1 → L2",UDim2.new(1,-48,0,36),UDim2.fromOffset(24,64),23)
local upgradeEffect=text(upgradeCard,"UpgradeEffect","9s → 6s pro Roboter · weiter +25 Cash\nOrbit-Design + neues Maschinenmodul",UDim2.new(1,-48,0,58),UDim2.fromOffset(24,106),16,C.muted)
local upgradeStatus=text(upgradeCard,"UpgradeStatus","Preis: 50 Factory Cash",UDim2.new(1,-48,0,48),UDim2.fromOffset(24,166),16,C.amber)
local buyButton=button(upgradeCard,"Buy","Für 50 Cash verbessern",UDim2.new(1,-48,0,44),UDim2.fromOffset(24,224),C.amber);buyButton.ZIndex=13
local cancelButton=button(upgradeCard,"Cancel","Abbrechen",UDim2.new(1,-48,0,44),UDim2.fromOffset(24,276));cancelButton.ZIndex=13
for _,label in ipairs({upgradeTitle,upgradeLevel,upgradeEffect,upgradeStatus}) do label.ZIndex=12 end

-- Persistence uses its own blocking status card so platform menus never dismiss an unsafe state.
local recovery=frame(gui,"RecoveryOverlay",UDim2.fromScale(1,1),UDim2.fromScale(0,0),C.navy)
recovery.BackgroundTransparency=0.18;recovery.ZIndex=20;recovery.Active=true
local recoveryCard=frame(recovery,"RecoveryCard",UDim2.fromOffset(490,270),UDim2.new(0.5,-245,0.5,-135));recoveryCard.ZIndex=21
local recoveryTitle=text(recoveryCard,"RecoveryTitle","Deine Werkstatt wartet",UDim2.new(1,-40,0,54),UDim2.fromOffset(20,14),24,C.cyan);recoveryTitle.ZIndex=22
local recoveryText=text(recoveryCard,"RecoveryText","Dein Fortschritt wird sicher geladen …",UDim2.new(1,-40,0,100),UDim2.fromOffset(20,76),17,C.white);recoveryText.ZIndex=22
local retryButton=button(recoveryCard,"Retry","Erneut versuchen",UDim2.new(1,-40,0,48),UDim2.fromOffset(20,200),C.cyan);retryButton.ZIndex=22;retryButton.Visible=false
local inputBlocked=true
local lastViewVersion=-1
local state=nil
local detailDesign="scout"
local portraitBuilder=Scout
local modal="collection"
local offer=nil
local pending=false
local requestSequence=0
local refreshDialogs

local ownOrigin=Vector3.zero
local overview=true
local reduced=false
local rewardUntil=0
local lastCompleted=0
local layoutWidth=0
local layoutHeight=0
local function layout()
    local camera=Workspace.CurrentCamera;if not camera then return end
    local width=gui.AbsoluteSize.X;local height=gui.AbsoluteSize.Y
    layoutWidth=width
    layoutHeight=height
    local rw=math.min(490,width-24)
    recoveryCard.Size=UDim2.fromOffset(rw,270);recoveryCard.Position=UDim2.new(0.5,-rw/2,0.5,-135)
    local narrow=width<700
    local short=height<500 and width>600
    brand.TextSize=if narrow then 20 else 24
    preview.Size=UDim2.fromOffset(if narrow then width-56 else 286,23)
    header.Size=UDim2.fromOffset(if narrow then width-32 else 310,if narrow then 90 else 84)
    brand.Position=UDim2.fromOffset(28,22)
    cashPanel.Size=UDim2.fromOffset(if narrow then 136 else 210,if narrow then 56 else 72)
    cashPanel.Position=UDim2.new(1,if narrow then -152 else -232,0,10)
    cashCaption.TextSize=14;cashCaption.Position=UDim2.fromOffset(12,5)
    cash.Position=UDim2.fromOffset(12,22);cash.Size=UDim2.new(1,-24,0,30);cash.TextSize=if narrow then 24 else 29
    -- On narrow screens the persistence notice is below the whole header, never under cash.
    preview.Position=UDim2.fromOffset(28,if narrow then 72 else 60)
    goal.Size=UDim2.fromOffset(if narrow then width-32 else 310,if narrow then 70 else 88)
    goal.Position=UDim2.fromOffset(16,if narrow then 110 else 106)
    objective.TextSize=if narrow then 15 else 17;objective.Position=UDim2.fromOffset(14,28);objective.Size=UDim2.new(1,-28,0,if narrow then 32 else 42)
    local touchExplore=UserInputService.TouchEnabled and not overview
    local bottom=if touchExplore then 150 else 66
    local navWidth=math.min(430,width-24);nav.Size=UDim2.fromOffset(navWidth,54);nav.Position=UDim2.new(0.5,-navWidth/2,1,-bottom)
    local third=(navWidth-20)/3
    for i,b in ipairs({collectionButton,cameraButton,motionButton}) do
        b.Size=UDim2.fromOffset(third,44);b.Position=UDim2.fromOffset(5+(i-1)*(third+5),5);b.TextSize=if narrow then 14 else 15
    end
    production.Position=UDim2.new(0.5,-155,1,-bottom-74)
    local cw=math.min(if short then 720 else 520,width-24);local ch=math.min(620,height-24)
    card.Size=UDim2.fromOffset(cw,ch);card.Position=UDim2.new(0.5,-cw/2,0.5,-ch/2)
    upgradeButton.Size=UDim2.fromOffset(if narrow then width-32 else 310,44)
    upgradeButton.Position=UDim2.fromOffset(16,if narrow then 188 else 204)
    upgradeCard.Size=UDim2.fromOffset(math.min(520,width-24),math.min(340,height-24))
    upgradeCard.Position=UDim2.new(0.5,-math.min(520,width-24)/2,0.5,-math.min(340,height-24)/2)
    local ph=ch-310
    portrait.Position=UDim2.fromOffset(18,116);portrait.Size=UDim2.new(1,-36,0,ph)
    for i,b in ipairs({scoutChoice,orbitChoice}) do b.Size=UDim2.fromOffset((cw-56)/2,44);b.Position=UDim2.fromOffset(24+(i-1)*(cw-8)/2,62) end
    scoutTitle.Position=UDim2.fromOffset(24,ph+122);scoutStatus.Position=UDim2.fromOffset(24,ph+162);scoutDescription.Position=UDim2.fromOffset(24,ph+192)
    for _,label in ipairs({scoutTitle,scoutStatus,scoutDescription}) do label.Size=UDim2.new(1,-48,0,if label==scoutDescription then 48 elseif label==scoutTitle then 40 else 28) end
    selectButton.Size=UDim2.new(1,-48,0,44);selectButton.Position=UDim2.new(0,24,1,-56)
    if short then
        portrait.Position=UDim2.fromOffset(18,63);portrait.Size=UDim2.fromOffset(cw*0.40,ch-81)
        local tx=cw*0.45;local tw=cw-tx-24
        for i,b in ipairs({scoutChoice,orbitChoice}) do b.Size=UDim2.fromOffset((tw-8)/2,44);b.Position=UDim2.fromOffset(tx+(i-1)*(tw+8)/2,62) end
        scoutTitle.Position=UDim2.fromOffset(tx,110);scoutStatus.Position=UDim2.fromOffset(tx,149);scoutDescription.Position=UDim2.fromOffset(tx,180)
        for _,label in ipairs({scoutTitle,scoutStatus,scoutDescription}) do label.Size=UDim2.fromOffset(tw,if label==scoutDescription then 72 elseif label==scoutTitle then 38 else 28) end
        selectButton.Size=UDim2.fromOffset(tw,44);selectButton.Position=UDim2.new(0,tx,1,-56)
    end
    reward.Size=UDim2.fromOffset(math.min(360,width-32),62);reward.Position=UDim2.new(0.5,-math.min(360,width-32)/2,0,if narrow then upgradeButton.Position.Y.Offset+upgradeButton.Size.Y.Offset+8 else 92)
    preview.TextSize=14;eyebrow.TextSize=14;eyebrow.Position=UDim2.fromOffset(14,10);rewardText.TextSize=19
    if short then
        header.Size=UDim2.fromOffset(260,58)
        brand.TextSize=18;brand.Position=UDim2.fromOffset(28,12)
        preview.TextSize=14;preview.Position=UDim2.fromOffset(28,41);preview.Size=UDim2.fromOffset(240,18)
        cashPanel.Size=UDim2.fromOffset(136,56);cashPanel.Position=UDim2.new(1,-152,0,10);cash.TextSize=24
        goal.Size=UDim2.fromOffset(250,64);goal.Position=UDim2.fromOffset(16,76)
        upgradeButton.Size=UDim2.fromOffset(250,44);upgradeButton.Position=UDim2.fromOffset(16,150)
        eyebrow.TextSize=14;eyebrow.Position=UDim2.fromOffset(12,2)
        objective.TextSize=14;objective.Position=UDim2.fromOffset(12,24);objective.Size=UDim2.new(1,-24,0,36)
        reward.Size=UDim2.fromOffset(260,46);reward.Position=UDim2.new(1,-276,0,76);rewardText.TextSize=15
    end
end
local function setOverview(value)
    overview=value;cameraButton.Text=if overview then "Erkunden" else "Werkstatt"
    if overview then controls:Disable() else controls:Enable();GuiService.SelectedObject=nil end
    layout()
    -- The dedicated workshop camera focuses its owner's slot. Exploration restores neighbours.
    local world=Workspace:FindFirstChild("BoltBotsWorld")
    if world and state then
        for _,plot in ipairs(world:GetChildren()) do
            if plot:IsA("Model") and plot:GetAttribute("Origin") then
                local hidden=overview and plot.Name~="FactoryPlot_"..state.plotIndex
                for _,item in ipairs(plot:GetDescendants()) do
                    if item:IsA("BasePart") then item.LocalTransparencyModifier=if hidden then 1 else 0 end
                    if item:IsA("SurfaceGui") then item.Enabled=not hidden end
                end
            end
        end
    end
    local camera=Workspace.CurrentCamera;if not camera then return end
    if overview then camera.CameraType=Enum.CameraType.Scriptable
    else
        camera.CameraType=Enum.CameraType.Custom
        local char=player.Character;local humanoid=char and char:FindFirstChildOfClass("Humanoid")
        if humanoid then camera.CameraSubject=humanoid end
    end
end
local function setNavigationEnabled(enabled)
    for _,action in ipairs({collectionButton,cameraButton,motionButton,upgradeButton}) do
        action.Active=enabled and not inputBlocked;action.Selectable=action.Active
    end
end
local function closeCollection()
    shade.Visible=false;setNavigationEnabled(true)
    -- Controller navigation returns to its trigger. Pointer/keyboard players resume world input.
    local gamepad=string.sub(UserInputService:GetLastInputType().Name,1,7)=="Gamepad"
    GuiService.SelectedObject=if gamepad then (if modal=="upgrade" then upgradeButton else collectionButton) else nil
    if not overview and not inputBlocked then controls:Enable() end
end
local function openCollection()
    if inputBlocked or not state then return end
    modal="collection";card.Visible=true;upgradeCard.Visible=false
    shade.Visible=true;setNavigationEnabled(false);GuiService.SelectedObject=close
    if refreshDialogs then refreshDialogs() end
    controls:Disable()
end
local function openUpgrade()
    if inputBlocked or shade.Visible or not state then return end
    modal="upgrade";offer={level=state.level,catalogVersion=state.catalogVersion,price=state.upgradePrice}
    card.Visible=false;upgradeCard.Visible=true;shade.Visible=true;setNavigationEnabled(false)
    GuiService.SelectedObject=cancelButton;controls:Disable()
    if refreshDialogs then refreshDialogs() end
end
close.Activated:Connect(closeCollection)
upgradeClose.Activated:Connect(closeCollection)
cancelButton.Activated:Connect(closeCollection)
upgradeButton.Activated:Connect(openUpgrade)
-- Escape belongs to Roblox's platform menu; dismiss our modal when that menu opens.
GuiService.MenuOpened:Connect(function() if shade.Visible then closeCollection() end end)
collectionButton.Activated:Connect(function() if not shade.Visible then openCollection() end end)
cameraButton.Activated:Connect(function() if not inputBlocked and not shade.Visible then setOverview(not overview) end end)
motionButton.Activated:Connect(function()
    if inputBlocked or shade.Visible then return end
    reduced=not reduced;motionButton.Text=if reduced then "Bewegung: ruhig" else "Bewegung: an"
end)
ContextActionService:BindActionAtPriority("CloseScoutCollection",function(_,inputState)
    if shade.Visible and inputState==Enum.UserInputState.Begin then closeCollection();return Enum.ContextActionResult.Sink end
    return Enum.ContextActionResult.Pass
end,false,3000,Enum.KeyCode.ButtonB)
UserInputService.InputBegan:Connect(function(input,processed)
    if inputBlocked or GuiService.MenuIsOpen or UserInputService:GetFocusedTextBox() then return end
    -- M remains a modal close shortcut even while GUI selection consumes other keys.
    if input.KeyCode==Enum.KeyCode.M then
        if shade.Visible then closeCollection() elseif not processed then openCollection() end
        return
    end
    if processed then return end
    if input.KeyCode==Enum.KeyCode.V and not shade.Visible then setOverview(not overview) end
end)
local function setDetail(design)
    if detailDesign~=design then
        detailDesign=design;portraitBot.Model:Destroy();portraitBuilder=builders[design]
        portraitBot=portraitBuilder.Build(portraitWorld,1)
    end
    if refreshDialogs then refreshDialogs() end
end
refreshDialogs=function()
    if not state then return end
    local unlocked=if detailDesign=="orbit" then state.unlockedOrbit else state.unlockedScout
    scoutTitle.Text=string.upper(detailDesign)
    scoutStatus.Text=if unlocked then "✓  Design freigeschaltet" else "Noch nicht entdeckt"
    scoutDescription.Text=if detailDesign=="orbit" then (if unlocked then "Der nachdenkliche Sternenfreund.\nSein kleiner Mond begleitet ihn." else "Ein neuer Freund wartet auf dich.\nVerbessere den Assembler auf L2.")
        else (if unlocked then "Dein neugieriger Werkstattfreund.\nBereit für den nächsten Auftrag." else "Schließe deine erste Produktion ab.")
    portrait.ImageColor3=if unlocked then Color3.new(1,1,1) else Color3.fromRGB(75,79,104)
    orbitChoice.Text=if state.unlockedOrbit then "Orbit" else "Orbit · L2"
    for id,b in pairs({scout=scoutChoice,orbit=orbitChoice}) do
        b.BackgroundColor3=if id==detailDesign then C.cyan else C.navy;b.TextColor3=if id==detailDesign then C.navy else C.white
        b.Active=not pending;b.Selectable=not pending
    end
    local allowed=detailDesign=="scout" or state.unlockedOrbit
    selectButton.Active=allowed and not pending;selectButton.Selectable=allowed and not pending
    selectButton.Text=if pending then "Wird bestätigt …" elseif not allowed then "Gesperrt · Assembler auf L2" elseif state.selectedDesign==detailDesign then "✓  Für nächste Produktion gewählt" else "Ab nächstem Zyklus produzieren"
    selectButton.BackgroundColor3=if allowed then C.cyan else C.muted
    if offer then
        upgradeLevel.Text="ASSEMBLER  L"..offer.level..(if offer.level==1 then " → L2" else " · AUSGEBAUT")
        upgradeEffect.Text=if offer.level==1 then "Ab nächstem Zyklus: 9s → "..state.upgradedCycleSeconds.."s\n+25 Cash · Orbit + Maschinenmodul" else "L2 arbeitet alle 6 Sekunden.\nEntdecke Orbit in der Sammlung."
        local deficit=math.max(0,offer.price-state.cash)
        upgradeStatus.Text=if state.level==2 then "✓  L2 und Orbit sind freigeschaltet." elseif deficit>0 then "Preis: "..offer.price.." Cash · Dir fehlen "..deficit.." Cash." else "Preis: "..offer.price.." Cash · Bereit zum Ausbau."
        buyButton.Text=if pending then "Wird bestätigt …" elseif state.level==2 then "✓  Bereits auf L2" else "Für "..offer.price.." Cash verbessern"
        buyButton.Active=not pending and state.level==1;buyButton.Selectable=buyButton.Active
    end
end
scoutChoice.Activated:Connect(function() if not pending then setDetail("scout") end end)
orbitChoice.Activated:Connect(function() if not pending then setDetail("orbit") end end)
local function show(incoming)
    if type(incoming.stateVersion)~="number" or incoming.stateVersion<lastViewVersion then return end
    lastViewVersion=incoming.stateVersion
    local status=incoming.saveStatus
    local wasBlocked=inputBlocked
    inputBlocked=status~="saved" and status~="local_session_only"
    recovery.Visible=status=="loading" or status=="load_failed" or status=="save_failed"
    if recovery.Visible then
        shade.Visible=false;reward.Visible=false;controls:Disable()
        local loading=status=="loading"
        recoveryTitle.Text=if loading then "Deine Werkstatt wartet" elseif incoming.saveError=="no_plot" then "Alle Werkstätten sind belegt" elseif status=="load_failed" then "Noch nicht verbunden" else "Sicher pausiert"
        recoveryText.Text=if loading then "Dein Fortschritt wird sicher geladen …" elseif incoming.saveError=="session_locked" then "Deine Werkstatt ist noch in einer anderen Sitzung geöffnet. Warte kurz und versuche es erneut."
            elseif incoming.saveError=="lease_lost" or incoming.saveError=="revision_conflict" then "Diese Sitzung ist abgelaufen. Dein letzter gesicherter Stand bleibt erhalten. Bitte tritt erneut bei."
            elseif incoming.saveError=="no_plot" then "Hier sind gerade alle 4 Werkstätten belegt. Dein Fortschritt bleibt erhalten. Versuche es erneut, sobald ein Platz frei wird."
            elseif status=="load_failed" then "Dein Fortschritt konnte nicht bestätigt werden. Es wird keine neue Fabrik angelegt. Versuche es erneut."
            else "Speichern ist noch nicht bestätigt. Produktion und Käufe pausieren. Dein aktueller Stand bleibt hier erhalten."
        retryButton.Visible=not loading and incoming.saveError~="lease_lost" and incoming.saveError~="revision_conflict"
        retryButton.Active=incoming.canRetry==true;retryButton.Selectable=retryButton.Active
        retryButton.Text=if incoming.canRetry then "Erneut versuchen" else "Wird geprüft …"
        GuiService.SelectedObject=if retryButton.Visible and retryButton.Active then retryButton else nil
    elseif wasBlocked and not inputBlocked then
        if shade.Visible then
            GuiService.SelectedObject=if modal=="upgrade" then cancelButton else close
        else GuiService.SelectedObject=nil;if not overview then controls:Enable() end end
    end
    setNavigationEnabled(not shade.Visible)
    preview.Text=if status=="local_session_only" then "Lokale Vorschau · ohne Speichern" elseif status=="saving" then "Fortschritt wird gesichert …"
        elseif status=="saved" then (if incoming.unsaved then "Fortschritt wird automatisch gesichert" else "✓  Fortschritt gesichert") else "Verbindung wird geprüft …"
    if incoming.ready~=true then cash.Text="—";objective.Text="Deine Werkstatt wird geladen …";phase.Text="Fortschritt noch nicht bestätigt";return end
    local stateWasLoaded=state~=nil
    local oldLevel=if state then state.level else incoming.level
    state=incoming;cash.Text=tostring(incoming.cash)
    local plot=Workspace:WaitForChild("BoltBotsWorld"):FindFirstChild("FactoryPlot_"..incoming.plotIndex)
    if plot then ownOrigin=plot:GetAttribute("Origin") end
    collectionButton.Text="Sammlung  "..((if incoming.unlockedScout then 1 else 0)+(if incoming.unlockedOrbit then 1 else 0)).."/2"
    eyebrow.Text=if incoming.level==2 then "DEIN NÄCHSTES DESIGN" else "DEIN NÄCHSTER AUSBAU"
    local selectedName=if incoming.selectedDesign=="orbit" then "Orbit" else "Scout"
    local currentName=if incoming.currentDesign=="orbit" then "Orbit" else "Scout"
    objective.Text=if incoming.level==2 then (if incoming.selectedDesign~=incoming.currentDesign then selectedName.." folgt nach diesem "..currentName.."." elseif incoming.selectedDesign=="scout" then "Orbit ist frei! Wähle ihn in der Sammlung." else "Orbit läuft. Scout bleibt wählbar.") elseif incoming.unlockedScout then "Spare 50 Cash für Assembler L2 + Orbit." else "Sieh deinem ersten Scout zu."
    upgradeButton.Text=if incoming.level==2 then "Assembler L2  ·  6s / Roboter" else "Ausbauen  ·  50 Cash"
    if stateWasLoaded and incoming.completed>lastCompleted then
        rewardText.Text=if lastCompleted==0 then "Scout entdeckt!  +25 Cash" else "+25 Factory Cash  ·  Fertig verpackt"
        rewardUntil=os.clock()+2.8;reward.Visible=true
    end
    if incoming.level>oldLevel then rewardText.Text="L2 ist da!  Orbit freigeschaltet";rewardUntil=os.clock()+4;reward.Visible=true end
    lastCompleted=incoming.completed
    if not incoming.productionActive then objective.Text=incoming.notice or "Cashgrenze erreicht · Produktion pausiert" end
    refreshDialogs()
end
local errors={funds="Noch nicht genug Cash. Warte auf die nächste Produktion.",stale_state="Stand geändert. Schließe den Dialog und bestätige die neuen Daten.",
    forbidden="Diese Maschine gehört nicht zu deiner Werkstatt.",locked="Orbit braucht den Assembler auf L2.",rate_limited="Einen Moment bitte. Versuche es gleich erneut.",
    level_limit="Dein Assembler ist bereits auf L2.",inactive="Die Sitzung ist nicht bereit.",stale_request="Diese Anfrage ist veraltet. Öffne die Ansicht erneut."}
local function sendIntent(kind,payload)
    if inputBlocked or pending or not state then return end
    pending=true;requestSequence+=1;payload.requestId=tostring(requestSequence);refreshDialogs()
    task.spawn(function()
        local ok,response=pcall(function() return command:InvokeServer(kind,payload) end)
        pending=false;refreshDialogs()
        if ok and type(response)=="table" then
            if type(response.view)=="table" then show(response.view) end
            if response.ok then
                if kind=="upgrade" then
                    if shade.Visible and modal=="upgrade" then closeCollection();setDetail("orbit");openCollection() end
                else
                    rewardText.Text=string.upper(state.selectedDesign).." · ab nächstem Zyklus";rewardUntil=os.clock()+3;reward.Visible=true
                    closeCollection()
                end
            else
                local message=errors[response.code] or "Anfrage abgelehnt. Dein Fortschritt bleibt erhalten."
                if modal=="upgrade" and shade.Visible then upgradeStatus.Text=message else scoutDescription.Text=message end
            end
        else
            local message="Keine Bestätigung. Prüfe den aktuellen Stand vor einem neuen Versuch."
            if modal=="upgrade" then upgradeStatus.Text=message else scoutDescription.Text=message end
        end
        buyButton.Active=state.level==1;buyButton.Selectable=buyButton.Active
        selectButton.Active=detailDesign=="scout" or state.unlockedOrbit;selectButton.Selectable=selectButton.Active
    end)
end
buyButton.Activated:Connect(function()
    if not shade.Visible or modal~="upgrade" or not offer or not state or state.level~=1 then return end
    sendIntent("upgrade",{machineId="starter",expectedLevel=offer.level,catalogVersion=offer.catalogVersion})
end)
selectButton.Activated:Connect(function()
    if shade.Visible and modal=="collection" and (detailDesign=="scout" or state and state.unlockedOrbit) then sendIntent("select",{designId=detailDesign}) end
end)
retryButton.Activated:Connect(function()
    if not retryButton.Active then return end
    retryButton.Active=false;retryButton.Selectable=false;retryButton.Text="Wird geprüft …"
    task.spawn(function()
        local ok,response=pcall(function() return command:InvokeServer("retry",{}) end)
        if ok and type(response)=="table" and type(response.view)=="table" then show(response.view)
        else retryButton.Active=true;retryButton.Selectable=true;retryButton.Text="Erneut versuchen" end
    end)
end)
changed.OnClientEvent:Connect(show)
local success,initial=pcall(function() return query:InvokeServer() end)
if success and type(initial)=="table" then show(initial) else objective.Text="Verbindung fehlgeschlagen. Bitte erneut beitreten." end
layout()

-- Local, bounded visuals for each active plot. All cycle timing originates on the server.
local visuals={}
local world=Workspace:WaitForChild("BoltBotsWorld")
local function makeCrate(parent)
    local model=Instance.new("Model");model.Name="ShippingCarton";model.Parent=parent
    local function piece(name,size)
        local p=Instance.new("Part");p.Name=name;p.Size=size;p.Anchored=true;p.CanCollide=false;p.CanQuery=false;p.CanTouch=false
        p.Material=Enum.Material.Cardboard;p.Color=Color3.fromRGB(186,142,90);p.Parent=model;return p
    end
    local base=piece("Carton base",Vector3.new(5.4,0.16,4.3))
    local walls={piece("Left wall",Vector3.new(0.18,7,4.3)),piece("Right wall",Vector3.new(0.18,7,4.3)),
        piece("Front wall",Vector3.new(5.4,7,0.18)),piece("Back wall",Vector3.new(5.4,7,0.18))}
    local lids={piece("Cover left",Vector3.new(2.7,0.16,4.3)),piece("Cover right",Vector3.new(2.7,0.16,4.3))}
    local tape=piece("Sealed tape",Vector3.new(0.24,0.03,4.32));tape.Color=Color3.fromRGB(239,207,142)
    local label=Instance.new("SurfaceGui");label.Face=Enum.NormalId.Back;label.CanvasSize=Vector2.new(400,500);label.LightInfluence=0.5;label.Parent=walls[3]
    local mark=Instance.new("TextLabel");mark.Size=UDim2.fromScale(0.8,0.24);mark.Position=UDim2.fromScale(0.1,0.45)
    mark.BackgroundColor3=Color3.fromRGB(239,229,200);mark.Text="SCOUT\n↑  BOLT BOTS";mark.TextColor3=C.navy;mark.Font=Enum.Font.GothamBold;mark.TextSize=37;mark.Parent=label
    return {Model=model,Base=base,Walls=walls,Lids=lids,Tape=tape,Label=label,Mark=mark}
end
local function poseCrate(crate,base,f,visible)
    local rise=math.clamp((f-0.72)/0.14,0,1)
    local height=math.max(0.05,7*rise)
    crate.Base.CFrame=base*CFrame.new(0,0.08,0)
    for i,p in ipairs(crate.Walls) do
        p.Size=Vector3.new(if i<=2 then 0.18 else 5.4,height,if i<=2 then 4.3 else 0.18)
        local offset=if i==1 then Vector3.new(-2.61,height/2+0.16,0) elseif i==2 then Vector3.new(2.61,height/2+0.16,0)
            elseif i==3 then Vector3.new(0,height/2+0.16,2.06) else Vector3.new(0,height/2+0.16,-2.06)
        p.CFrame=base*CFrame.new(offset);p.Transparency=if visible then 0 else 1
    end
    local closing=math.clamp((f-0.86)/0.06,0,1)
    for i,p in ipairs(crate.Lids) do
        p.CFrame=base*CFrame.new((if i==1 then -1 else 1)*(4.05-2.7*closing),7.24,0)
        p.Transparency=if visible and f>=0.86 then 0 else 1
    end
    crate.Tape.CFrame=base*CFrame.new(0,7.34,0)
    crate.Tape.Transparency=if visible and f>=0.92 then 0 else 1
    crate.Base.Transparency=if visible then 0 else 1;crate.Label.Enabled=visible and rise>0.65
end
for _,plot in ipairs(world:GetChildren()) do
    if plot:IsA("Model") and plot:GetAttribute("Origin") then
        local container=Instance.new("Folder");container.Name="LocalProductionVisual";container.Parent=plot
        local bot=Scout.Build(container,1)
        local crate=makeCrate(container)
        local loose=Instance.new("Part");loose.Name="IncomingBody";loose.Size=Vector3.new(2,1.8,1.5)
        loose.Color=Color3.fromRGB(242,237,217);loose.Anchored=true;loose.CanCollide=false;loose.CanQuery=false;loose.Parent=container
        local mesh=Instance.new("SpecialMesh");mesh.MeshType=Enum.MeshType.Sphere;mesh.Parent=loose
        table.insert(visuals,{plot=plot,origin=plot:GetAttribute("Origin"),container=container,ownerLabel=plot:FindFirstChild("OwnerLabel",true),bot=bot,builder=Scout,design="scout",crate=crate,loose=loose})
    end
end
setOverview(true)
local lastVisualTick=0
RunService.RenderStepped:Connect(function()
    local now=Workspace:GetServerTimeNow();local camera=Workspace.CurrentCamera
    if camera and (math.abs(gui.AbsoluteSize.X-layoutWidth)>1 or math.abs(gui.AbsoluteSize.Y-layoutHeight)>1) then layout() end
    local character=player.Character
    local touchGui=player.PlayerGui:FindFirstChild("TouchGui")
    if touchGui and touchGui:IsA("ScreenGui") then touchGui.Enabled=not overview and not shade.Visible and not inputBlocked end
    if character then
        for _,piece in ipairs(character:GetDescendants()) do
            if piece:IsA("BasePart") then piece.LocalTransparencyModifier=if overview then 1 else 0 end
        end
    end
    if overview and camera then
        local narrow=camera.ViewportSize.X<700
        camera.FieldOfView=if narrow then 65 else 48
        camera.CFrame=CFrame.lookAt(ownOrigin+(if narrow then Vector3.new(12,46,64) else Vector3.new(21,18,32)),ownOrigin+Vector3.new(-1,4.3,-0.4))
    end
    if reward.Visible and os.clock()>rewardUntil then reward.Visible=false end
    if state and state.productionActive then
        local f=math.clamp(((state.pausedAt or now)-state.cycleStart)/state.cycleSeconds,0,1)
        local label=if f<0.20 then "Teile bereitstellen" elseif f<0.42 then (if state.currentDesign=="orbit" then "Orbit montieren" else "Scout montieren") elseif f<0.72 then "Auf dem Förderband" elseif f<0.92 then "Verpacken" else "Fertig zum Versand"
        phase.Text=(if state.pausedAt then "Sicher pausiert" else label).."  ·  +"..state.cashPerRobot.." Cash / "..state.cycleSeconds.."s"
        progressFill.Size=UDim2.fromScale(f,1)
    end
    -- 30Hz presentation; one reused robot/carton per plot, no growing output list.
    if now-lastVisualTick<1/30 then return end
    lastVisualTick=now
    if shade.Visible and modal=="collection" then portraitBuilder.Pose(portraitBot,CFrame.Angles(0,-0.18,0),now,reduced,0) end
    for _,v in ipairs(visuals) do
        local owner=v.plot:GetAttribute("OwnerUserId")
        local ownerText=if owner==player.UserId then "DEINE WERKSTATT" elseif owner~=nil then "ANDERE WERKSTATT" else "WERKSTATT  /  FREI"
        if v.ownerLabel and v.ownerLabel.Text~=ownerText then v.ownerLabel.Text=ownerText end
        local active=v.plot:GetAttribute("Active")==true
        local start=v.plot:GetAttribute("CycleStart") or now
        local duration=v.plot:GetAttribute("CycleSeconds") or 9
        local visualNow=v.plot:GetAttribute("PausedAt") or now
        local f=math.clamp((visualNow-start)/duration,0,1)
        local design=v.plot:GetAttribute("DesignId") or "scout"
        if design~=v.design and builders[design] then
            v.bot.Model:Destroy();v.design=design;v.builder=builders[design];v.bot=v.builder.Build(v.container,1)
            v.crate.Mark.Text=string.upper(design).."\n↑  BOLT BOTS"
        end
        v.builder.Visible(v.bot,active and f>=0.18 and f<0.92)
        v.loose.Transparency=if active and f<0.20 then 0 else 1
        v.loose.CFrame=CFrame.new(v.origin+Vector3.new(-16+11*math.clamp(f/0.2,0,1),3.7,0))
        local x=if f<0.42 then -5 elseif f<0.72 then -5+18*(f-0.42)/0.30 elseif f<0.92 then 13 else 13+7*(f-0.92)/0.08
        local lift=if f<0.34 then (1-math.clamp((f-0.18)/0.16,0,1))*2.2 else 0
        v.builder.Pose(v.bot,CFrame.new(v.origin+Vector3.new(x,if f>=0.72 then 2.9 else 2.82,0))*CFrame.Angles(0,0.12,0),visualNow,reduced or f>=0.72,lift)
        poseCrate(v.crate,CFrame.new(v.origin+Vector3.new(x,2.70,0)),f,active and f>=0.72 and (not overview or v.origin==ownOrigin))
    end
end)
print("BOLTBOTS_CLIENT_BOOT", "development-b3", "view="..tostring(Workspace.CurrentCamera.ViewportSize))
