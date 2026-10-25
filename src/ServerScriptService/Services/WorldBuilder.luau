--!strict
-- Original local workshop geometry. One compact station per session slot.
local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")
local Config = require(game:GetService("ReplicatedStorage"):WaitForChild("Shared"):WaitForChild("GameConfig"))
local World = {}
local C={ivory=Color3.fromRGB(218,215,201),white=Color3.fromRGB(249,246,229),navy=Color3.fromRGB(33,53,67),
    steel=Color3.fromRGB(76,99,108),cyan=Color3.fromRGB(64,213,235),amber=Color3.fromRGB(246,181,63),
    floor=Color3.fromRGB(185,200,195),dark=Color3.fromRGB(24,39,49),leaf=Color3.fromRGB(79,145,113),
    box=Color3.fromRGB(184,137,85)}
local function part(parent,name,size,cf,color,material,shape)
    local p=Instance.new("Part");p.Name=name;p.Size=size;p.CFrame=cf;p.Color=color
    p.Anchored=true;p.Material=material or Enum.Material.SmoothPlastic
    p.TopSurface=Enum.SurfaceType.Smooth;p.BottomSurface=Enum.SurfaceType.Smooth
    if shape then p.Shape=shape end
    p.Parent=parent;return p
end
local function label(p,text,color,textSize)
    local gui=Instance.new("SurfaceGui");gui.Face=Enum.NormalId.Back;gui.CanvasSize=Vector2.new(600,160)
    gui.LightInfluence=0;gui.Parent=p
    local t=Instance.new("TextLabel");t.Size=UDim2.fromScale(1,1);t.BackgroundTransparency=1
    t.Text=text;t.TextColor3=color or C.white;t.Font=Enum.Font.GothamBold;t.TextSize=textSize or 70;t.Parent=gui
    return t
end
local function beam(parent,name,a,b,width,color)
    return part(parent,name,Vector3.new(width,width,(b-a).Magnitude),CFrame.lookAt((a+b)/2,b),color)
end
local function cylinder(parent,name,pos,diameter,height,color)
    return part(parent,name,Vector3.new(height,diameter,diameter),CFrame.new(pos)*CFrame.Angles(0,0,math.pi/2),color,nil,Enum.PartType.Cylinder)
end
local function plant(parent,position,scale)
    cylinder(parent,"Ceramic planter",position+Vector3.new(0,0.8*scale,0),2.2*scale,1.6*scale,C.ivory)
    cylinder(parent,"Soil",position+Vector3.new(0,1.62*scale,0),1.9*scale,0.08,C.dark)
    for i=1,7 do
        local angle=i*2.399
        local pos=position+Vector3.new(math.cos(angle)*0.65*scale,(2.1+i*0.12)*scale,math.sin(angle)*0.65*scale)
        local leaf=part(parent,"Leaf",Vector3.new(0.7,2.4,0.45)*scale,CFrame.new(pos)*CFrame.Angles(0,angle,math.sin(angle)*0.4),C.leaf)
        local mesh=Instance.new("SpecialMesh");mesh.MeshType=Enum.MeshType.Sphere;mesh.Parent=leaf
    end
end
local function buildPlot(root,index,origin)
    local model=Instance.new("Model");model.Name="FactoryPlot_"..index;model.Parent=root
    model:SetAttribute("Origin",origin);model:SetAttribute("Active",false)
    local function p(name,size,pos,color,material,shape)
        return part(model,name,size,CFrame.new(origin+pos),color,material,shape)
    end
    p("Foundation",Vector3.new(49,1.1,36),Vector3.new(0,-0.1,0),C.navy)
    p("Floor",Vector3.new(48,0.6,35),Vector3.new(0,0.7,0),C.floor,Enum.Material.Concrete)
    for x=-23,23,5.75 do p("Floor grout",Vector3.new(0.035,0.015,34),Vector3.new(x,1.012,0),Color3.fromRGB(145,165,163)) end
    for z=-16,16,5.33 do p("Floor grout",Vector3.new(47,0.015,0.035),Vector3.new(0,1.013,z),Color3.fromRGB(145,165,163)) end
    p("Entry stripe",Vector3.new(18,0.025,0.34),Vector3.new(0,1.025,16.5),C.amber)
    p("Front skirt",Vector3.new(46,0.55,0.20),Vector3.new(0,0.35,18.06),C.ivory)
    for _,x in ipairs({-23,23}) do
        p("Rear column",Vector3.new(1.1,18,1.1),Vector3.new(x,9.5,-15),C.ivory)
        p("Column foot",Vector3.new(2,1.7,2),Vector3.new(x,1.5,-15),C.navy)
        if x<0 then
            p("Side rail",Vector3.new(0.25,0.25,26),Vector3.new(x,3.4,-2),C.amber)
        else
            -- The dispatch opening is a real gap, never a rail across the carton path.
            p("Rear side rail",Vector3.new(0.25,0.25,9),Vector3.new(x,3.4,-10.5),C.amber)
            p("Front side rail",Vector3.new(0.25,0.25,5),Vector3.new(x,3.4,8.5),C.amber)
        end
        for z=-14,10,8 do
            if x<0 or math.abs(z)>5 then p("Rail post",Vector3.new(0.22,2.5,0.22),Vector3.new(x,2.25,z),C.steel) end
        end
    end
    p("Back sill",Vector3.new(47,2.3,0.65),Vector3.new(0,2.0,-15),C.ivory)
    p("Window header",Vector3.new(47,1.2,1.1),Vector3.new(0,16.8,-15),C.ivory)
    for x=-16,16,8 do
        p("Window mullion",Vector3.new(0.32,13.2,0.32),Vector3.new(x,9.5,-15),C.steel)
    end
    p("Window crossbar",Vector3.new(46,0.25,0.3),Vector3.new(0,10,-15),C.steel)
    -- Open daylight windows; no opaque wall hides the workshop silhouette.
    p("Overhead golden beam",Vector3.new(47,0.5,0.6),Vector3.new(0,15.5,-9),C.amber)
    for _,x in ipairs({-16,15}) do
        p("Pendant cable",Vector3.new(0.08,3,0.08),Vector3.new(x,13.8,-8),C.navy)
        p("Pendant housing",Vector3.new(5.5,0.35,2.2),Vector3.new(x,12.2,-8),C.navy)
        p("Warm task light",Vector3.new(4.7,0.12,1.5),Vector3.new(x,11.98,-8),Color3.fromRGB(255,219,151),Enum.Material.Neon)
    end
    local brand=p("Workshop identity",Vector3.new(17,3.6,0.5),Vector3.new(-0.5,13.8,-14.4),C.navy)
    label(brand,"B O L T B O T S",C.white,64)
    local number=p("Bay number",Vector3.new(4,2,0.42),Vector3.new(-20,14,-14.2),C.amber)
    label(number,string.format("0%d",index),C.dark,100)
    -- Conveyor: rubber slats, metal rollers, cyan guide edges and visible supports.
    p("Belt chassis",Vector3.new(34,1.15,6.2),Vector3.new(0,1.75,0),C.navy)
    p("Rubber belt",Vector3.new(33,0.3,5.4),Vector3.new(0,2.42,0),C.dark)
    for x=-16,16,0.85 do
        p("Belt slat",Vector3.new(0.64,0.12,5.25),Vector3.new(x,2.64,0),C.steel,Enum.Material.Metal)
    end
    for _,z in ipairs({-3.05,3.05}) do
        p("Belt rail",Vector3.new(34.8,0.38,0.34),Vector3.new(0,2.52,z),C.ivory)
        p("Cyan guide",Vector3.new(33.6,0.09,0.12),Vector3.new(0,2.79,z),C.cyan,Enum.Material.Neon)
    end
    for x=-14,14,7 do
        p("Conveyor support",Vector3.new(1.5,1.1,5.4),Vector3.new(x,1.45,0),C.navy)
        local bolt=p("Front hub",Vector3.new(0.14,0.48,0.48),Vector3.new(x,1.8,3.2),C.cyan,Enum.Material.Neon,Enum.PartType.Cylinder)
        bolt.CFrame=CFrame.new(origin+Vector3.new(x,1.8,3.2))*CFrame.Angles(0,math.pi/2,0)
    end
    -- Parts rack behind the intake; repeated ivory shells imply the next build.
    p("Parts cabinet",Vector3.new(7,3,3.8),Vector3.new(-17,2.5,-5.8),C.navy)
    for shelf=0,1 do
        p("Parts shelf",Vector3.new(7.3,0.25,4),Vector3.new(-17,3.0+shelf*2.2,-5.8),C.steel)
        for column=0,2 do
            local shell=p("Spare helmet",Vector3.new(1.5,1.25,1.35),Vector3.new(-19+column*2,3.7+shelf*2.2,-5.6),C.ivory)
            local mesh=Instance.new("SpecialMesh");mesh.MeshType=Enum.MeshType.Sphere;mesh.Parent=shell
            local visor=p("Spare visor",Vector3.new(1.1,0.55,0.22),Vector3.new(-19+column*2,3.7+shelf*2.2,-4.98),C.dark)
            local vm=Instance.new("SpecialMesh");vm.MeshType=Enum.MeshType.Sphere;vm.Parent=visor
        end
    end
    local intake=p("Parts label",Vector3.new(6,1.0,0.25),Vector3.new(-17,2.4,-3.75),C.navy)
    label(intake,"01  TEILE",C.white,68)
    -- Open assembler arch frames the actual Scout; articulated tools remain readable.
    local ax=-5
    for _,side in ipairs({-1,1}) do
        local x=ax+side*4.5
        p("Assembler foot",Vector3.new(2.7,1.0,4.8),Vector3.new(x,1.55,-2.7),C.ivory)
        cylinder(model,"Steel upright",origin+Vector3.new(x,5.2,-2.8),1.0,7,C.navy)
        cylinder(model,"Piston",origin+Vector3.new(x,5.8,-2.3),0.33,6,C.steel)
        p("Upright shell",Vector3.new(1.5,4.2,1.3),Vector3.new(x,4.0,-2.8),C.ivory)
        p("Upright trim",Vector3.new(0.3,3.1,0.15),Vector3.new(x,4.3,-2.07),C.amber)
        local a=origin+Vector3.new(x,5,-1.5)
        local b=origin+Vector3.new(x-side*0.8,7.2,-0.9)
        local c=origin+Vector3.new(ax+side*1.8,6.0,-0.4)
        beam(model,"Tool upper arm",a,b,0.65,C.amber)
        beam(model,"Tool forearm",b,c,0.52,C.amber)
        for _,point in ipairs({a,b,c}) do
            local joint=part(model,"Tool joint",Vector3.new(0.55,0.95,0.95),CFrame.new(point)*CFrame.Angles(0,math.pi/2,0),C.navy,nil,Enum.PartType.Cylinder)
            joint.CanCollide=false
        end
        beam(model,"Gripper",c,c+Vector3.new(-side*0.4,-0.55,0),0.18,C.steel)
    end
    p("Assembler crown",Vector3.new(9,1.8,3.8),Vector3.new(ax,9.3,-2.6),C.ivory)
    for _,side in ipairs({-1,1}) do cylinder(model,"Crown rounded end",origin+Vector3.new(ax+side*4.4,9.3,-2.6),3.8,1.8,C.ivory) end
    p("Crown seam",Vector3.new(8.8,0.13,0.12),Vector3.new(ax,8.65,-0.65),C.amber,Enum.Material.Neon)
    local machineLabel=p("Assembler label",Vector3.new(7,0.85,0.12),Vector3.new(ax,9.5,-0.65),C.navy)
    local levelLabel=label(machineLabel,"ASSEMBLER  /  L1",C.white,60)
    local upgradeParts={}
    -- L2 adds a real rear power module and paired cooling fins, within the existing station.
    local power=p("L2 power core",Vector3.new(5.4,2.8,2.2),Vector3.new(ax,5.2,-5.2),C.navy)
    table.insert(upgradeParts,power)
    for i=-2,2 do
        table.insert(upgradeParts,p("L2 cooling fin",Vector3.new(0.38,2.4,2.7),Vector3.new(ax+i*0.85,5.2,-5.2),C.steel,Enum.Material.Metal))
    end
    table.insert(upgradeParts,p("L2 violet rail",Vector3.new(7.4,0.28,0.34),Vector3.new(ax,10.35,-2.2),Color3.fromRGB(167,132,247),Enum.Material.Neon))
    for _,side in ipairs({-1,1}) do
        table.insert(upgradeParts,p("L2 status beacon",Vector3.new(0.65,1.1,0.65),Vector3.new(ax+side*3.1,10.7,-2.6),Color3.fromRGB(167,132,247),Enum.Material.Neon))
    end
    p("Tool spindle",Vector3.new(0.6,1.2,0.6),Vector3.new(ax,7.95,-1.8),C.steel,Enum.Material.Metal)
    local stage=p("Assembly stage",Vector3.new(5.4,0.15,5.2),Vector3.new(ax,2.72,0),C.navy)
    stage.CanCollide=false
    -- An open gantry spans ACROSS the belt; no post stands in the moving robot's path.
    -- Belt top 2.7 + Scout 6.6 / carton 7.2 fit below the 10.4-stud opening.
    for _,z in ipairs({-3.7,3.7}) do
        for _,x in ipairs({10,16}) do
            p("Packager post",Vector3.new(0.7,9.4,0.7),Vector3.new(x,5.7,z),C.ivory)
            p("Packager post foot",Vector3.new(1.2,0.6,1.2),Vector3.new(x,1.3,z),C.navy)
        end
        p("Packager side beam",Vector3.new(7.4,0.8,0.9),Vector3.new(13,10.8,z),C.ivory)
    end
    p("Packager crossbeam",Vector3.new(0.8,0.8,8.2),Vector3.new(13,10.8,0),C.ivory)
    p("Packager warm strip",Vector3.new(5.5,0.12,0.13),Vector3.new(13,10.38,4.17),C.amber,Enum.Material.Neon)
    local shipping=p("Packaging label",Vector3.new(6,0.72,0.15),Vector3.new(13,10.8,4.18),C.navy)
    label(shipping,"03  VERPACKEN",C.white,58)
    p("Outfeed chassis",Vector3.new(13.6,1.15,6.2),Vector3.new(23.7,1.75,0),C.navy)
    for x=17.4,30,0.8 do p("Outfeed slat",Vector3.new(0.64,0.12,5.25),Vector3.new(x,2.64,0),C.steel,Enum.Material.Metal) end
    for _,z in ipairs({-3.05,3.05}) do
        p("Outfeed rail",Vector3.new(13.6,0.38,0.34),Vector3.new(23.7,2.52,z),C.ivory)
        p("Outfeed guide",Vector3.new(13.4,0.09,0.12),Vector3.new(23.7,2.79,z),C.cyan,Enum.Material.Neon)
    end
    -- A bounded dispatch bay receives the sealed carton. Its rolling door closes
    -- before the client reuses the carton, including when viewed from the inlet.
    p("Dispatch plinth",Vector3.new(10.5,1.1,10.4),Vector3.new(25.8,0.55,0),C.navy)
    for _,z in ipairs({-3.65,3.65}) do
        p("Dispatch wall",Vector3.new(9.4,8.5,0.55),Vector3.new(26.1,6.8,z),C.ivory)
        p("Dispatch lower trim",Vector3.new(9.6,0.6,0.65),Vector3.new(26.1,3.05,z),C.navy)
        p("Dispatch top trim",Vector3.new(9.6,0.35,0.65),Vector3.new(26.1,10.7,z),C.navy)
    end
    p("Dispatch back",Vector3.new(0.5,8.5,7.8),Vector3.new(30.8,6.8,0),C.dark)
    p("Dispatch roof",Vector3.new(10,0.7,8.2),Vector3.new(26,11.25,0),C.ivory)
    p("Dispatch door hood",Vector3.new(0.85,1.0,8.1),Vector3.new(21.25,11.25,0),C.navy)
    local shutter=p("DispatchShutter",Vector3.new(0.22,8.1,6.7),Vector3.new(21.5,6.85,0),C.steel,Enum.Material.Metal)
    shutter.CanCollide=false
    local sill=p("DispatchShutterEdge",Vector3.new(0.3,0.16,6.7),Vector3.new(21.5,2.88,0),C.amber)
    sill.CanCollide=false
    local guard=p("Dispatch safety boundary",Vector3.new(0.25,8.2,7.2),Vector3.new(21.7,6.8,0),C.dark)
    guard.Transparency=1 -- Keeps walking avatars out of the operating machine.
    local dispatch=p("Dispatch label",Vector3.new(8.2,1.55,0.18),Vector3.new(26,8.9,3.96),C.navy)
    label(dispatch,"04  VERSAND",C.white,68)
    p("Dispatch ready light",Vector3.new(7.8,0.15,0.12),Vector3.new(26,7.85,4.07),C.cyan,Enum.Material.Neon)
    for x=22,29,1.5 do
        p("Dispatch warning mark",Vector3.new(0.65,0.04,0.85),Vector3.new(x,1.13,4.5),C.amber)
    end
    for i=1,3 do
        p("Waiting carton",Vector3.new(2.2,1.6,2.1),Vector3.new(18+(i%2)*2.3,1.8+math.floor(i/3)*1.65,-6),C.box)
    end
    -- Warm workbench and plants give scale and a lived-in workshop character.
    p("Workbench top",Vector3.new(9,0.4,3),Vector3.new(8,3.6,-10.5),C.ivory)
    for _,x in ipairs({4.5,11.5}) do p("Bench leg",Vector3.new(0.4,2.4,2.7),Vector3.new(x,2.2,-10.5),C.navy) end
    p("Tool tray",Vector3.new(3,0.18,1.8),Vector3.new(7,3.9,-10.5),C.navy)
    for x=6,8,0.7 do p("Spare pin",Vector3.new(0.2,0.25,1.2),Vector3.new(x,4.1,-10.4),C.amber) end
    plant(model,origin+Vector3.new(-20,1,10),1)
    plant(model,origin+Vector3.new(20,1,-12),1.1)
    local info=p("Workshop front plaque",Vector3.new(10,1.2,0.25),Vector3.new(-12,1.9,15),C.navy)
    local ownerLabel=label(info,"WERKSTATT  /  FREI",C.white,55);ownerLabel.Name="OwnerLabel"
    local spawn=Instance.new("SpawnLocation");spawn.Name="OwnerSpawn";spawn.Size=Vector3.new(6,0.2,4)
    spawn.Position=origin+Vector3.new(0,1.2,12);spawn.Anchored=true;spawn.Transparency=1
    spawn.CanCollide=false;spawn.Neutral=true;spawn.Duration=0;spawn.Parent=model
    return {Index=index,Model=model,Origin=origin,OwnerLabel=ownerLabel,Occupied=false,Spawn=spawn,
        LevelLabel=levelLabel,UpgradeParts=upgradeParts,SpawnCFrame=CFrame.new(origin+Vector3.new(0,4.5,12))}
end

function World.Build()
    local old=Workspace:FindFirstChild("BoltBotsWorld");if old then old:Destroy() end
    local root=Instance.new("Folder");root.Name="BoltBotsWorld";root.Parent=Workspace
    part(root,"Courtyard",Vector3.new(180,1,170),CFrame.new(30,-1.2,20),Color3.fromRGB(142,175,161),Enum.Material.Grass)
    local locations={Vector3.new(0,0,0),Vector3.new(65,0,0),Vector3.new(0,0,55),Vector3.new(65,0,55)}
    local plots={};for i=1,Config.maxPlots do
        local plot=buildPlot(root,i,locations[i]);World.SetLevel(plot,1);table.insert(plots,plot)
    end
    -- Distant low-detail garden, with no imported asset dependency.
    for i=0,10 do
        local pos=Vector3.new(-35+i*13,0,-32-math.sin(i)*5)
        cylinder(root,"Garden trunk",pos+Vector3.new(0,3,0),0.75,6,Color3.fromRGB(118,103,76))
        local tree=part(root,"Garden canopy",Vector3.new(8,9,8),CFrame.new(pos+Vector3.new(0,8,0)),Color3.fromRGB(95+i*3,154+i*2,118))
        tree.Shape=Enum.PartType.Ball
    end
    Lighting.ClockTime=14.3;Lighting.Brightness=1.8;Lighting.GlobalShadows=true
    Lighting.Ambient=Color3.fromRGB(94,112,125);Lighting.OutdoorAmbient=Color3.fromRGB(150,166,170)
    Lighting.EnvironmentDiffuseScale=0.55;Lighting.EnvironmentSpecularScale=0.45
    for _,effect in ipairs(Lighting:GetChildren()) do
        if effect.Name=="BoltBotsAtmosphere" or effect.Name=="BoltBotsColor" then effect:Destroy() end
    end
    local atmosphere=Instance.new("Atmosphere");atmosphere.Name="BoltBotsAtmosphere"
    atmosphere.Density=0.23;atmosphere.Offset=0.2;atmosphere.Color=Color3.fromRGB(211,232,237)
    atmosphere.Decay=Color3.fromRGB(155,184,190);atmosphere.Haze=1;atmosphere.Parent=Lighting
    local grade=Instance.new("ColorCorrectionEffect");grade.Name="BoltBotsColor"
    grade.Brightness=-0.035;grade.Contrast=0.06;grade.Saturation=0.02;grade.TintColor=Color3.fromRGB(255,248,231);grade.Parent=Lighting
    return plots
end
function World.SetLevel(plot,level)
    plot.Model:SetAttribute("Level",level)
    plot.LevelLabel.Text="ASSEMBLER  /  L"..level
    for _,p in ipairs(plot.UpgradeParts) do p.Transparency=if level>=2 then 0 else 1;p.CanCollide=level>=2 end
end
function World.SetOccupied(plot,occupied,ownerUserId)
    plot.Model:SetAttribute("Active",false)
    plot.Model:SetAttribute("OwnerUserId",if occupied then ownerUserId else nil)
    plot.OwnerLabel.Text=if occupied then "WERKSTATT  /  BELEGT" else "WERKSTATT  /  FREI"
end
return World
