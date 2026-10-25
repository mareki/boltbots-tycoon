--!strict
-- Original Orbit: a slender, thoughtful companion with a tilted satellite halo.
-- Shared by the collection and the bounded live production; no downloaded assets.
local Orbit={}
local SHELL=Color3.fromRGB(226,218,239)
local PALE=Color3.fromRGB(248,238,250)
local VIOLET=Color3.fromRGB(165,118,240)
local DARK=Color3.fromRGB(32,30,57)
local JOINT=Color3.fromRGB(70,65,91)
local GLASS=Color3.fromRGB(15,20,43)
local function part(parent,name,size,cf,color,sphere,neon)
    local p=Instance.new("Part");p.Name=name;p.Size=size;p.CFrame=cf;p.Color=color
    p.Anchored=true;p.CanCollide=false;p.CanQuery=false;p.CanTouch=false
    p.Material=if neon then Enum.Material.Neon else Enum.Material.SmoothPlastic
    p.TopSurface=Enum.SurfaceType.Smooth;p.BottomSurface=Enum.SurfaceType.Smooth;p.Parent=parent
    if sphere then local m=Instance.new("SpecialMesh");m.MeshType=Enum.MeshType.Sphere;m.Parent=p end
    return p
end
local function ball(parent,name,pos,size,color,neon)
    return part(parent,name,size,CFrame.new(pos),color,true,neon)
end
local function rod(parent,name,a,b,width,color,neon)
    local p=part(parent,name,Vector3.new((b-a).Magnitude,width,width),CFrame.lookAt((a+b)/2,b)*CFrame.Angles(0,math.pi/2,0),color,false,neon)
    p.Shape=Enum.PartType.Cylinder;return p
end
function Orbit.Build(parent: Instance,scale: number?)
    local model=Instance.new("Model");model.Name="Orbit";model.Parent=parent
    local head=Instance.new("Model");head.Name="Head";head.Parent=model
    local hand=Instance.new("Model");hand.Name="ThoughtfulHand";hand.Parent=model
    for _,side in ipairs({-1,1}) do
        local x=side*0.53
        ball(model,"Narrow sole",Vector3.new(x,0.19,0.19),Vector3.new(0.86,0.34,1.32),DARK,false)
        ball(model,"Moon boot",Vector3.new(x,0.49,0.13),Vector3.new(0.79,0.78,1.15),SHELL,false)
        ball(model,"Violet toe",Vector3.new(x,0.35,0.65),Vector3.new(0.60,0.22,0.21),VIOLET,false)
        rod(model,"Long shin",Vector3.new(x,0.76,0),Vector3.new(x*0.90,1.49,-0.06),0.49,SHELL,false)
        ball(model,"Knee joint",Vector3.new(x*0.90,1.42,0),Vector3.new(0.43,0.43,0.49),JOINT,false)
        rod(model,"Thigh shell",Vector3.new(x*0.90,1.49,-0.06),Vector3.new(x*0.70,2.05,0),0.61,SHELL,false)
        ball(model,"Hip bearing",Vector3.new(x*0.72,2.03,0),Vector3.new(0.43,0.43,0.49),VIOLET,false)
    end
    ball(model,"Slender waist",Vector3.new(0,2.21,0),Vector3.new(0.91,0.59,0.80),DARK,false)
    ball(model,"Pear torso",Vector3.new(0,2.87,0),Vector3.new(1.65,1.55,1.20),SHELL,false)
    ball(model,"Chest bezel",Vector3.new(0,2.98,0.59),Vector3.new(0.69,0.69,0.23),JOINT,false)
    ball(model,"Orbit core",Vector3.new(0,2.98,0.73),Vector3.new(0.48,0.48,0.14),VIOLET,true)
    ball(model,"Core gleam",Vector3.new(-0.08,3.08,0.82),Vector3.new(0.12,0.12,0.04),PALE,false)
    rod(model,"Slim collar",Vector3.new(0,3.46,0),Vector3.new(0,3.90,0),0.55,JOINT,false)
    ball(head,"Round lunar helmet",Vector3.new(0,4.85,0),Vector3.new(2.94,2.77,2.35),SHELL,false)
    ball(head,"Visor rim",Vector3.new(0,4.80,0.98),Vector3.new(2.50,2.12,0.74),VIOLET,false)
    ball(head,"Visor",Vector3.new(0,4.80,1.12),Vector3.new(2.29,1.89,0.63),GLASS,false)
    for _,side in ipairs({-1,1}) do
        ball(head,"Round curious eye",Vector3.new(side*0.57,4.85,1.435),Vector3.new(0.43,0.52,0.08),VIOLET,true)
        ball(head,"Eye glint",Vector3.new(side*0.57-0.07,4.98,1.485),Vector3.new(0.12,0.15,0.035),PALE,false)
        ball(head,"Ear mount",Vector3.new(side*1.42,4.72,0),Vector3.new(0.46,1.10,1.18),JOINT,false)
        ball(head,"Ear disk",Vector3.new(side*1.61,4.72,0.02),Vector3.new(0.16,0.85,0.88),VIOLET,false)
    end
    local last=nil
    for i=0,12 do
        local a=math.pi*1.12+math.pi*0.76*i/12
        local point=Vector3.new(math.cos(a)*0.19,4.48+math.sin(a)*0.19,1.455)
        if last then rod(head,"Quiet smile",last,point,0.045,Color3.fromRGB(125,100,177),false) end
        last=point
    end
    -- A diagonal oval wraps around the helmet; its front arc stays above the eyes.
    local ringCF=CFrame.new(0,5.02,0)*CFrame.Angles(math.rad(53),0,math.rad(28))
    last=nil
    for i=0,48 do
        local a=i*math.pi*2/48
        local point=ringCF:PointToWorldSpace(Vector3.new(2.08*math.cos(a),1.62*math.sin(a),0))
        if last then rod(head,"Satellite ring",last,point,0.11,DARK,false) end
        last=point
    end
    local satellite=ringCF:PointToWorldSpace(Vector3.new(2.08*math.cos(0.45),1.62*math.sin(0.45),0))
    ball(head,"Tiny moon",satellite,Vector3.new(0.35,0.35,0.35),VIOLET,true)
    -- One hand rests by the cheek; the other opens in a gentle invitation.
    for _,side in ipairs({-1,1}) do
        local target=if side==1 then hand else model
        local shoulder=Vector3.new(side*0.91,3.16,0)
        local elbow=Vector3.new(side*1.18,if side==1 then 2.85 else 2.52,0.13)
        local wrist=Vector3.new(side*(if side==1 then 1.19 else 1.53),if side==1 then 3.73 else 2.10,if side==1 then 0.88 else 0.28)
        ball(target,"Shoulder",shoulder,Vector3.new(0.57,0.57,0.57),JOINT,false)
        rod(target,"Upper arm",shoulder,elbow,0.44,SHELL,false)
        ball(target,"Elbow",elbow,Vector3.new(0.38,0.38,0.38),JOINT,false)
        rod(target,"Forearm",elbow,wrist,0.48,SHELL,false)
        ball(target,"Wrist cuff",wrist,Vector3.new(0.36,0.36,0.36),VIOLET,false)
        local palm=wrist+Vector3.new(side*0.02,if side==1 then 0.15 else -0.10,0.09)
        ball(target,"Hand",palm,Vector3.new(0.42,0.42,0.28),PALE,false)
        for finger=1,3 do
            local start=palm+Vector3.new((finger-2)*0.13,if side==1 then 0.13 else -0.10,0)
            local finish=start+Vector3.new(if side==1 then -0.07 else -0.05,if side==1 then 0.23 else -0.18,0.06)
            rod(target,"Finger",start,finish,0.10,PALE,false)
        end
        ball(target,"Thumb",palm+Vector3.new(-side*0.22,0,0.03),Vector3.new(0.16,0.23,0.18),JOINT,false)
    end
    model.WorldPivot=CFrame.new();local size=scale or 1;model:ScaleTo(size)
    local parts={}
    for _,p in ipairs(model:GetDescendants()) do
        if p:IsA("BasePart") then table.insert(parts,{part=p,localCF=p.CFrame,head=p:IsDescendantOf(head)}) end
    end
    return {Model=model,Parts=parts,Scale=size}
end
function Orbit.Pose(bot,base: CFrame,time: number,reduced: boolean,headLift: number?)
    local s=bot.Scale
    local tilt=if reduced then 0 else math.sin(time*1.25)*0.025
    local headCF=CFrame.new(0,(headLift or 0)*s,0)*CFrame.new(0,4.0*s,0)*CFrame.Angles(0,tilt,-0.045+tilt)*CFrame.new(0,-4.0*s,0)
    for _,entry in ipairs(bot.Parts) do entry.part.CFrame=base*(if entry.head then headCF else CFrame.new())*entry.localCF end
end
function Orbit.Visible(bot,visible: boolean)
    for _,entry in ipairs(bot.Parts) do entry.part.Transparency=if visible then 0 else 1 end
end
return Orbit
