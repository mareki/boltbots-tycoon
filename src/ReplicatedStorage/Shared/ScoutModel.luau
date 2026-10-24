--!strict
-- Original parts-based character, shared by the live production and collection portrait.
-- No external meshes, textures, asset downloads or gameplay authority.
local Scout = {}
local IVORY = Color3.fromRGB(225, 223, 210)
local EDGE = Color3.fromRGB(202, 215, 211)
local INK = Color3.fromRGB(18, 35, 51)
local JOINT = Color3.fromRGB(43, 63, 75)
local CYAN = Color3.fromRGB(64, 213, 235)
local GLASS = Color3.fromRGB(9, 24, 38)

local function part(parent, name, size, cf, color, sphere, neon)
    local p = Instance.new("Part")
    p.Name = name; p.Size = size; p.CFrame = cf
    p.Color = color; p.Material = if neon then Enum.Material.Neon else Enum.Material.SmoothPlastic
    p.Anchored = true; p.CanCollide = false; p.CanTouch = false; p.CanQuery = false
    p.TopSurface = Enum.SurfaceType.Smooth; p.BottomSurface = Enum.SurfaceType.Smooth
    if sphere then
        local mesh = Instance.new("SpecialMesh")
        mesh.MeshType = Enum.MeshType.Sphere; mesh.Parent = p
    end
    p.Parent = parent
    return p
end
local function ball(parent, name, pos, size, color, neon)
    return part(parent, name, size, CFrame.new(pos), color, true, neon)
end
local function rod(parent, name, a, b, width, color, neon)
    local p = part(parent, name, Vector3.new((b-a).Magnitude, width, width),
        CFrame.lookAt((a+b)/2,b) * CFrame.Angles(0,math.pi/2,0), color, false, neon)
    p.Shape = Enum.PartType.Cylinder
    return p
end
local function arc(parent, name, center, radius, startAngle, endAngle, color, width)
    local last = nil
    for i=0,16 do
        local angle = startAngle + (endAngle-startAngle)*i/16
        local point = center + Vector3.new(math.cos(angle)*radius, math.sin(angle)*radius, 0)
        if last then rod(parent,name,last,point,width,color,true) end
        last = point
    end
end

function Scout.Build(parent: Instance, scale: number?)
    local model = Instance.new("Model"); model.Name = "Scout"; model.Parent = parent
    local head = Instance.new("Model"); head.Name = "Head"; head.Parent = model
    local arm = Instance.new("Model"); arm.Name = "WavingArm"; arm.Parent = model
    -- Slightly splayed chunky boots ground the large, inquisitive head.
    for _,side in ipairs({-1,1}) do
        local x=side*0.64
        ball(model,"Sole",Vector3.new(x,0.22,0.22),Vector3.new(1.18,0.42,1.65),INK,false)
        ball(model,"Boot",Vector3.new(x,0.57,0.18),Vector3.new(1.08,1.02,1.38),IVORY,false)
        ball(model,"Toe",Vector3.new(x,0.43,0.70),Vector3.new(0.84,0.36,0.42),EDGE,false)
        ball(model,"Knee",Vector3.new(x,1.19,-0.02),Vector3.new(0.56,0.62,0.60),JOINT,false)
        ball(model,"KneeLight",Vector3.new(x,1.20,0.30),Vector3.new(0.28,0.28,0.11),CYAN,true)
        ball(model,"Thigh",Vector3.new(x*0.76,1.53,-0.04),Vector3.new(0.77,0.88,0.83),IVORY,false)
    end
    ball(model,"Waist",Vector3.new(0,1.97,0),Vector3.new(1.34,0.59,1.00),INK,false)
    ball(model,"BodyShell",Vector3.new(0,2.68,0),Vector3.new(2.08,1.83,1.55),IVORY,false)
    ball(model,"ChestInset",Vector3.new(0,2.75,0.76),Vector3.new(0.77,0.77,0.22),JOINT,false)
    ball(model,"ChestRing",Vector3.new(0,2.75,0.89),Vector3.new(0.57,0.57,0.12),CYAN,true)
    ball(model,"ChestCore",Vector3.new(0,2.75,0.97),Vector3.new(0.30,0.30,0.10),Color3.fromRGB(202,250,251),false)
    ball(model,"Collar",Vector3.new(0,3.53,0),Vector3.new(1.07,0.34,0.94),JOINT,false)
    ball(head,"Helmet",Vector3.new(0,4.67,0),Vector3.new(3.30,2.55,2.36),IVORY,false)
    ball(head,"VisorSeal",Vector3.new(0,4.61,0.99),Vector3.new(2.85,1.95,0.77),EDGE,false)
    ball(head,"Visor",Vector3.new(0,4.64,1.12),Vector3.new(2.66,1.77,0.65),GLASS,false)
    -- Curved eyes and a small smile read as a face even with bloom disabled.
    for _,side in ipairs({-1,1}) do
        arc(head,"HappyEye",Vector3.new(side*0.64,4.55,1.467),0.30,0.05,math.pi-0.05,CYAN,0.145)
        ball(head,"Cheek",Vector3.new(side*0.91,4.27,1.39),Vector3.new(0.19,0.08,0.04),Color3.fromRGB(41,99,121),false)
        local ear=part(head,"EarHousing",Vector3.new(0.34,1.32,1.32),CFrame.new(side*1.57,4.64,0.02),JOINT,false,false)
        ear.Shape=Enum.PartType.Cylinder
        local rim=part(head,"EarLight",Vector3.new(0.10,1.02,1.02),CFrame.new(side*1.78,4.64,0.02),CYAN,false,true)
        rim.Shape=Enum.PartType.Cylinder
        local cap=part(head,"EarCap",Vector3.new(0.13,0.76,0.76),CFrame.new(side*1.85,4.64,0.02),INK,false,false)
        cap.Shape=Enum.PartType.Cylinder
    end
    arc(head,"Smile",Vector3.new(0,4.31,1.458),0.20,math.pi*1.10,math.pi*1.90,Color3.fromRGB(45,117,137),0.045)
    ball(head,"ForeheadAccent",Vector3.new(0,5.84,-0.10),Vector3.new(0.92,0.20,0.90),JOINT,false)
    rod(head,"Antenna",Vector3.new(0,5.83,-0.10),Vector3.new(0.16,6.39,-0.12),0.10,JOINT,false)
    ball(head,"AntennaTip",Vector3.new(0.16,6.43,-0.12),Vector3.new(0.32,0.32,0.32),CYAN,true)
    -- The relaxed hand and raised greeting have different silhouettes.
    for _,side in ipairs({-1,1}) do
        local parentArm = if side == -1 then arm else model
        ball(parentArm,"Shoulder",Vector3.new(side*1.06,3.02,0),Vector3.new(0.71,0.71,0.71),JOINT,false)
        local elbow = Vector3.new(side*1.43,if side==-1 then 3.16 else 2.43,0.04)
        rod(parentArm,"UpperArm",Vector3.new(side*1.12,2.97,0),elbow,0.55,IVORY,false)
        ball(parentArm,"Elbow",elbow,Vector3.new(0.46,0.46,0.46),JOINT,false)
        local wrist = Vector3.new(side*1.76,if side==-1 then 3.77 else 1.99,0.19)
        rod(parentArm,"Forearm",elbow,wrist,0.61,IVORY,false)
        ball(parentArm,"Wrist",wrist,Vector3.new(0.40,0.40,0.40),CYAN,false)
        local palm = wrist+Vector3.new(side*0.06,if side==-1 then 0.22 else -0.17,0.07)
        ball(parentArm,"Palm",palm,Vector3.new(0.55,0.58,0.33),JOINT,false)
        for finger=1,3 do
            local x=palm.X+(finger-2)*0.19
            local start=Vector3.new(x,palm.Y+(if side==-1 then 0.16 else -0.12),palm.Z)
            local finish=start+Vector3.new((finger-2)*0.035,if side==-1 then 0.34 else -0.22,0.05)
            rod(parentArm,"Finger",start,finish,0.14,INK,false)
            ball(parentArm,"Fingertip",finish,Vector3.new(0.15,0.15,0.15),EDGE,false)
        end
        ball(parentArm,"Thumb",palm+Vector3.new(-side*0.31,0.01,0.06),Vector3.new(0.21,0.32,0.24),JOINT,false)
    end
    model.WorldPivot=CFrame.new()
    local size=scale or 1
    model:ScaleTo(size)
    local parts={}
    for _,descendant in ipairs(model:GetDescendants()) do
        if descendant:IsA("BasePart") then
            table.insert(parts,{part=descendant,localCF=descendant.CFrame,head=descendant:IsDescendantOf(head),arm=descendant:IsDescendantOf(arm)})
        end
    end
    return {Model=model,Parts=parts,Scale=size}
end

function Scout.Pose(bot, base: CFrame, time: number, reduced: boolean, headLift: number?)
    local s=bot.Scale
    local tilt=if reduced then 0 else math.sin(time*1.7)*0.055
    local wave=if reduced then 0 else math.sin(time*3.4)*0.11
    local headTransform=CFrame.new(0,(headLift or 0)*s,0)*CFrame.new(0,4.1*s,0)*CFrame.Angles(0,tilt,tilt)*CFrame.new(0,-4.1*s,0)
    local armTransform=CFrame.new(-1.06*s,3.02*s,0)*CFrame.Angles(0,0,wave)*CFrame.new(1.06*s,-3.02*s,0)
    for _,entry in ipairs(bot.Parts) do
        entry.part.CFrame=base*(if entry.head then headTransform elseif entry.arm then armTransform else CFrame.new())*entry.localCF
    end
end

function Scout.Visible(bot, visible: boolean)
    for _,entry in ipairs(bot.Parts) do entry.part.Transparency=if visible then 0 else 1 end
end
return Scout
