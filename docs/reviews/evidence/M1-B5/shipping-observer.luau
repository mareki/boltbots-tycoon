-- Read-only observation of the real client animation. No clock, state, pose or input injection.
assert(game:GetService("RunService"):IsClient())
local player=game.Players.LocalPlayer
local plot
for _,p in ipairs(workspace.BoltBotsWorld:GetChildren()) do
    if p:GetAttribute("OwnerUserId")==player.UserId then plot=p end
end
assert(plot)
local origin=plot:GetAttribute("Origin")
local carton=plot.LocalProductionVisual.ShippingCarton
local started=os.clock()
local phase,lastPhase,lastX,lastVisible,lastHeight
local events,failures,recycles=0,0,0
local connection
connection=game:GetService("RunService").RenderStepped:Connect(function()
    local f=math.clamp(((plot:GetAttribute("PausedAt") or workspace:GetServerTimeNow())-plot:GetAttribute("CycleStart"))/plot:GetAttribute("CycleSeconds"),0,1)
    local base=carton["Carton base"]
    local x=base.Position.X-origin.X
    local visible=base.Transparency==0
    local height=plot.DispatchShutter.Size.Y
    phase=if visible and x>24 then "received" elseif f>=0.92 then "entry" elseif f>=0.86 then "seal" elseif f>=0.72 then "pack" else "produce"
    if phase~=lastPhase then
        events+=1
        print("BOLTBOTS_B5_SHIPPING",plot:GetAttribute("DesignId"),phase,string.format("f=%.3f x=%.2f door=%.2f visible=%s",f,x,height,tostring(visible)))
        lastPhase=phase
    end
    if lastX and lastX>24 and x<20 and lastVisible then
        local hidden=not visible and lastHeight>=7.9
        recycles+=1
        if not hidden then failures+=1 end
        print("BOLTBOTS_B5_RECYCLE",hidden and "occluded" or "FAIL",string.format("previousDoor=%.2f",lastHeight))
    end
    lastX,lastVisible,lastHeight=x,visible,height
    if os.clock()-started>15 then
        connection:Disconnect()
        print("BOLTBOTS_B5_SHIPPING_END",events,failures,recycles,settings().Rendering.QualityLevel,workspace.CurrentCamera.ViewportSize)
    end
end)
