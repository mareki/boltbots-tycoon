-- Temporary Studio-only B4 measurement; removed before candidate/build/cloud save.
local R=game:GetService('RunService')
if not R:IsStudio() or game.GameId~=10772906084 or game.PlaceId~=112662761038118 then return end
local P=game:GetService('Players');local S=game:GetService('Stats');local H=game:GetService('HttpService')
local run=workspace:GetAttribute('B4ProbeRun');local expected=workspace:GetAttribute('B4ProbeClients')
local outputSequence=0
local function out(tag,data)
 outputSequence+=1
 local payload=H:JSONEncode(data)
 if #payload<=700 then print('B4_'..tag,payload);return end
 local id=tostring(run)..'-'..tostring(data.user or 'server')..'-'..outputSequence
 local total=math.ceil(#payload/650)
 for i=1,total do print('B4_CHUNK',id,tag,i,total,string.sub(payload,(i-1)*650+1,i*650)) end
end
local function counts()
 local active=0;local cycles={}
 local world=workspace:FindFirstChild('BoltBotsWorld')
 if world then for _,plot in ipairs(world:GetChildren()) do if plot:GetAttribute('Origin') then
  if plot:GetAttribute('Active') then active+=1 end
  cycles[plot.Name]={cycle=plot:GetAttribute('CycleId'),active=plot:GetAttribute('Active'),level=plot:GetAttribute('Level')}
 end end end
 local ids={};for _,p in ipairs(P:GetPlayers()) do table.insert(ids,p.UserId) end;table.sort(ids)
 return {players=ids,active=active,cycles=cycles,instances=S.InstanceCount,memoryMB=S:GetTotalMemoryUsageMb()}
end
local untilTime=os.clock()+160
repeat task.wait(0.5) until #P:GetPlayers()>=expected or os.clock()>untilTime
task.wait(15)
local before=counts();local samples={};local started=os.clock()
local connection=R.Heartbeat:Connect(function(dt) table.insert(samples,dt*1000) end)
task.wait(60);connection:Disconnect();table.sort(samples)
local function pct(p) return samples[math.max(1,math.ceil(#samples*p))] end
out('SERVER_METRICS',{run=run,gameId=game.GameId,placeId=game.PlaceId,elapsed=os.clock()-started,samples=#samples,p50=pct(.5),p95=pct(.95),max=pct(1),before=before,after=counts()})
if expected==5 then
 local chosen=nil
 for _,plot in ipairs(workspace.BoltBotsWorld:GetChildren()) do
  local owner=plot:GetAttribute('OwnerUserId')
  if owner and plot:GetAttribute('Active') then chosen=P:GetPlayerByUserId(owner);if chosen then break end end
 end
 -- Diagnostic disconnect of a proven active owner, never normal human leave.
 if chosen then out('CAPACITY_FREE_SLOT',{run=run,user=chosen.UserId,before=counts()});chosen:Kick('B4 diagnostic: release one active test slot') end
 task.wait(45);out('CAPACITY_AFTER_RETRY',{run=run,after=counts()})
end
