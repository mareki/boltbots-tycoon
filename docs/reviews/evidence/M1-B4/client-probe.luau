-- Temporary Studio-only B4 diagnostic. Direct remotes are NOT normal GUI actions.
local R=game:GetService('RunService')
if not R:IsStudio() or game.GameId~=10772906084 or game.PlaceId~=112662761038118 then return end
local P=game:GetService('Players');local me=P.LocalPlayer
local H=game:GetService('HttpService');local S=game:GetService('Stats')
local rem=game:GetService('ReplicatedStorage'):WaitForChild('BoltBotsRemotes',30)
if not rem then warn('B4_PROBE_ERROR no_remotes');return end
local run=workspace:GetAttribute('B4ProbeRun')
local expected=workspace:GetAttribute('B4ProbeClients')
local outputSequence=0
local function out(tag,data)
 outputSequence+=1
 local payload=H:JSONEncode(data)
 if #payload<=700 then print('B4_'..tag,payload);return end
 local id=tostring(run)..'-'..tostring(data.user or 'server')..'-'..outputSequence
 local total=math.ceil(#payload/650)
 for i=1,total do print('B4_CHUNK',id,tag,i,total,string.sub(payload,(i-1)*650+1,i*650)) end
end
local function view() return rem.GetSnapshot:InvokeServer() end
local function counts()
 local containers,bots,crates=0,0,0
 for _,p in ipairs(workspace.BoltBotsWorld:GetChildren()) do
  local f=p:FindFirstChild('LocalProductionVisual')
  if f then containers+=1;for _,o in ipairs(f:GetChildren()) do if o:IsA('Model') then bots+=1 end end;crates+=#f:GetChildren() end
 end
 return {instances=S.InstanceCount,memoryMB=S:GetTotalMemoryUsageMb(),containers=containers,models=bots,children=crates}
end
local function snapshot(tag)
 local v=view();out(tag,{run=run,user=me.UserId,gameId=game.GameId,placeId=game.PlaceId,view=v,players=#P:GetPlayers()});return v
end
local deadline=os.clock()+65
local v=view()
repeat task.wait(0.5);v=view() until v.ready or v.saveError=='no_plot' or os.clock()>deadline
snapshot('CLIENT_READY')
local gui=me.PlayerGui:WaitForChild('BoltBotsHUD');local card=gui.RecoveryOverlay.RecoveryCard
out('RECOVERY_UI',{run=run,user=me.UserId,visible=gui.RecoveryOverlay.Visible,title=card.RecoveryTitle.Text,body=card.RecoveryText.Text,titleFits=card.RecoveryTitle.TextFits,bodyFits=card.RecoveryText.TextFits})
if not v.ready then
 if v.saveError=='no_plot' then
  task.wait(105)
  local a=view();local answer=rem.Command:InvokeServer('retry',{});local b=view()
  out('CAPACITY_RETRY',{run=run,user=me.UserId,before=a,response=answer,after=b})
 end
 return
end
-- Wait for the intended client population and then warm another 15 seconds.
local populationDeadline=os.clock()+70
repeat task.wait(0.5) until #P:GetPlayers()>=expected or os.clock()>populationDeadline
task.wait(15)
local first=counts();local samples={};local started=os.clock()
local connection=R.RenderStepped:Connect(function(dt) table.insert(samples,dt*1000) end)
task.wait(60);connection:Disconnect();local elapsed=os.clock()-started
local last=counts();table.sort(samples)
local function pct(p) return samples[math.max(1,math.ceil(#samples*p))] end
out('CLIENT_METRICS',{run=run,user=me.UserId,elapsed=elapsed,samples=#samples,p50=pct(.5),p95=pct(.95),max=pct(1),before=first,after=last,viewport=tostring(workspace.CurrentCamera.ViewportSize),quality='Studio child; parent Automatic, no privileged client settings read',players=#P:GetPlayers()})
if expected~=4 then return end
if me.UserId~=-3 and me.UserId~=-4 then task.wait(28);snapshot('CONTROL_AFTER_OTHER_COMMANDS');return end
-- Bounded integration probes against this real authenticated client's session.
local seq=100
local function request(label,kind,payload,extra)
 seq+=1;payload=payload or {};if kind~='retry' then payload.requestId=tostring(seq) end
 local before=view();local result
 if extra then result=rem.Command:InvokeServer(kind,payload,'unexpected') else result=rem.Command:InvokeServer(kind,payload) end
 local after=view();out('REMOTE',{run=run,user=me.UserId,label=label,request={kind=kind,payload=payload,extra=extra},before=before,response=result,after=after})
 task.wait(1.1)
 return result
end
request('foreign_player','upgrade',{machineId='starter',expectedLevel=v.level,catalogVersion=1,playerId=-999})
request('foreign_plot','upgrade',{machineId='starter',expectedLevel=v.level,catalogVersion=1,plotIndex=if v.plotIndex==1 then 2 else 1})
request('foreign_machine','upgrade',{machineId='FactoryPlot_2/starter',expectedLevel=v.level,catalogVersion=1})
request('negative_level','upgrade',{machineId='starter',expectedLevel=-1,catalogVersion=1})
request('string_level','upgrade',{machineId='starter',expectedLevel='1',catalogVersion=1})
-- JSON cannot represent NaN/Inf: record semantic label while sending the actual value.
for _,case in ipairs({{'nan',0/0},{'infinity',math.huge}}) do
 seq+=1;local before=view();local answer=rem.Command:InvokeServer('upgrade',{requestId=tostring(seq),machineId='starter',expectedLevel=case[2],catalogVersion=1});out('NUMERIC_GUARD',{run=run,user=me.UserId,label=case[1],before=before,response=answer,after=view()});task.wait(1.1)
end
request('unknown_design','select',{designId='admin_robot'})
request('client_complete','complete',{cycleId=v.cycleId})
request('extra_argument','select',{designId='scout'},true)
local before=view();seq+=1;local id=tostring(seq);local replies={};local ids={};local done=0
for i=1,3 do
 local requestId=if me.UserId==-3 then id else tostring(seq+i)
 ids[i]=requestId
 task.spawn(function() replies[i]=rem.Command:InvokeServer('upgrade',{requestId=requestId,machineId='starter',expectedLevel=before.level,catalogVersion=1});done+=1 end)
end
seq+=3
repeat task.wait() until done==3
out(if me.UserId==-3 then 'PARALLEL_DUPLICATE' else 'PARALLEL_DISTINCT',{run=run,user=me.UserId,before=before,requestIds=ids,replies=replies,after=view()})
task.wait(1.2)
local prior=view();local replies2={}
for i=1,12 do seq+=1;replies2[i]=rem.Command:InvokeServer('select',{requestId=tostring(seq),designId='scout'}) end
out('RATE_BURST',{run=run,user=me.UserId,before=prior,replies=replies2,after=view()})
local polluted=rem.GetSnapshot:InvokeServer(me.UserId);out('QUERY_EXTRA',{run=run,user=me.UserId,response=polluted})
-- All clients observe every replicated plot's public attributes, no private session token.
local plots={};for _,p in ipairs(workspace.BoltBotsWorld:GetChildren()) do if p:GetAttribute('Origin') then plots[p.Name]=p:GetAttributes() end end
for _,p in pairs(plots) do p.Origin=tostring(p.Origin) end
out('PUBLIC_WORLD',{run=run,user=me.UserId,plots=plots,own=view()})
task.wait(1.2);request('select_orbit','select',{designId='orbit'});task.wait(8);snapshot('NEXT_ORBIT_CYCLE')
