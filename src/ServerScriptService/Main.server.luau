--!strict
-- Authoritative factory session. Only the explicitly authorized private test universe can write.
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")
local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared:WaitForChild("GameConfig"))
local Rules = require(Shared:WaitForChild("EconomyRules"))
local WorldBuilder = require(script.Parent:WaitForChild("Services"):WaitForChild("WorldBuilder"))
local Schema = require(Shared:WaitForChild("ProfileSchema"))
local ProfileStore = require(script.Parent.Services:WaitForChild("ProfileStore"))
local HttpService = game:GetService("HttpService")
local LOCAL = game.GameId == 0
local TARGET = game.GameId == 10772906084 and game.PlaceId == 112662761038118
local backend = if TARGET then game:GetService("DataStoreService"):GetDataStore("BoltBots_B3_20261025") else nil
local transport = {}
function transport:UpdateAsync(key, transform)
    return backend:UpdateAsync(key,function(raw)
        local nextRecord=transform(raw)
        -- Explicit Studio-only fault probe. The real API rejects this unserializable value;
        -- no client remote can set this server attribute, and live servers ignore it.
        if nextRecord and game:GetService("RunService"):IsStudio() and Workspace:GetAttribute("B3RejectStoreWrites")==true then
            nextRecord.__diagnosticInvalidValue=function() end
        end
        return nextRecord
    end)
end
local store = if TARGET then ProfileStore.new(transport, os.time,
    function() return HttpService:GenerateGUID(false) end) else nil
local plots = WorldBuilder.Build()
local sessions: {[Player]: any} = {}

local remotes = Instance.new("Folder")
remotes.Name = "BoltBotsRemotes"
remotes.Parent = ReplicatedStorage
local stateChanged = Instance.new("RemoteEvent")
stateChanged.Name = "StateChanged"
stateChanged.Parent = remotes
local getSnapshot = Instance.new("RemoteFunction")
getSnapshot.Name = "GetSnapshot"
getSnapshot.Parent = remotes
local command = Instance.new("RemoteFunction")
command.Name = "Command"
command.Parent = remotes

local function snapshot(player: Player, notice: string?)
    local session = sessions[player]
    if not session then return {ready=false,stateVersion=0,saveStatus="loading",notice="Deine Werkstatt wird geladen …"} end
    session.version += 1
    local common={ready=session.profile~=nil,stateVersion=session.version,saveStatus=session.status,
        saveError=session.error,canRetry=not session.busy and not session.leaving,
        savedRevision=if session.handle then session.handle.revision else 0,
        notice=notice,version=Config.versionLabel}
    local profile=session.profile
    if not profile then return common end
    local cycle=profile.cycle
    common.unsaved=profile.stateVersion~=session.savedStateVersion
    common.cash=profile.cash;common.completed=profile.completed
    common.unlockedScout=profile.unlockedScout;common.unlockedOrbit=profile.unlockedOrbit;common.level=profile.level
    common.selectedDesign=profile.selectedDesign;common.currentDesign=if cycle then cycle.designId else profile.selectedDesign
    common.upgradePrice=Config.firstUpgradePrice;common.catalogVersion=Config.catalogVersion
    common.nextCycleSeconds=Rules.cycleSeconds(profile);common.upgradedCycleSeconds=Config.upgradedCycleSeconds
    common.plotIndex=if session.plot then session.plot.Index else 1
    common.cycleStart=if cycle then cycle.startedAt else 0;common.cycleId=if cycle then cycle.id else profile.lastCycleId
    common.cycleSeconds=if cycle then cycle.completesAt-cycle.startedAt else Rules.cycleSeconds(profile)
    common.cashPerRobot=Config.creditsPerRobot;common.productionActive=cycle~=nil;common.pausedAt=session.pausedAt
    return common
end
local function publish(player: Player, notice: string?)
    if player.Parent == Players then stateChanged:FireClient(player, snapshot(player, notice)) end
end
local function startCycle(session)
    local ok, reason = Rules.beginCycle(session.profile, Workspace:GetServerTimeNow())
    local cycle = session.profile.cycle
    if ok and cycle then
        session.plot.Model:SetAttribute("CycleStart", cycle.startedAt)
        session.plot.Model:SetAttribute("CycleSeconds", cycle.completesAt-cycle.startedAt)
        session.plot.Model:SetAttribute("DesignId", cycle.designId)
        session.plot.Model:SetAttribute("CycleId", cycle.id)
        session.plot.Model:SetAttribute("Active", true)
    else
        session.plot.Model:SetAttribute("Active", false)
        warn("BOLTBOTS_PRODUCTION_PAUSED", reason)
    end
end

getSnapshot.OnServerInvoke = function(player: Player, ...)
    if select("#", ...) ~= 0 then return { ready = false, notice = "Ungültige Anfrage." } end
    -- Query only. There is deliberately no client production-completion remote.
    return snapshot(player)
end

local function pause(session)
    if session.profile then
        session.profile.active=false
        if not session.pausedAt then session.pausedAt=Workspace:GetServerTimeNow() end
        if session.plot then session.plot.Model:SetAttribute("PausedAt",session.pausedAt) end
    end
end
local function resume(session)
    if session.leaving then return end
    local now=Workspace:GetServerTimeNow()
    local cycle=session.profile.cycle
    if cycle and session.pausedAt then
        local delay=now-session.pausedAt;cycle.startedAt+=delay;cycle.completesAt+=delay
        session.plot.Model:SetAttribute("CycleStart",cycle.startedAt)
    end
    session.pausedAt=nil;session.plot.Model:SetAttribute("PausedAt",nil)
    session.profile.active=true;session.status=if LOCAL then "local_session_only" else "saved";session.error=nil
    if not cycle then startCycle(session) end
end
local function saveSession(player,session,release)
    if session.busy or not session.profile or LOCAL then return false end
    session.busy=true;pause(session);session.status="saving";publish(player)
    local ok,code=store.save(session.handle,session.profile,release)
    -- A failed normal write is retried unchanged before a separate final release.
    if ok and release and session.handle.expiresAt>0 then ok,code=store.save(session.handle,session.profile,true) end
    session.busy=false;session.nextSave=os.clock()+ProfileStore.saveInterval
    if ok then
        session.status=if release then "released" else "saved";session.error=nil;session.savedStateVersion=session.profile.stateVersion
        print("BOLTBOTS_SAVE",code,"revision="..session.handle.revision,"cash="..session.profile.cash,
            "completed="..session.profile.completed,"level="..session.profile.level,"design="..session.profile.selectedDesign)
        if not release and not session.leaving then resume(session) end
    else
        session.status="save_failed";session.error=code
        warn("BOLTBOTS_SAVE_FAILED",code,"revision="..session.handle.revision)
    end
    publish(player)
    return ok
end
local function reservePlot(session,player)
    if session.plot then return true end
    for _,plot in ipairs(plots) do
        if not plot.Occupied then
            plot.Occupied=true;session.plot=plot;player.RespawnLocation=plot.Spawn
            WorldBuilder.SetOccupied(plot,true,player.UserId);WorldBuilder.SetLevel(plot,1)
            return true
        end
    end
    return false
end
local function freePlot(session)
    if session.plot then
        session.plot.Model:SetAttribute("Active",false);session.plot.Model:SetAttribute("PausedAt",nil)
        WorldBuilder.SetOccupied(session.plot,false);session.plot.Occupied=false;session.plot=nil
    end
end
local function loadSession(player,session)
    if session.busy or session.leaving then return end
    if not reservePlot(session,player) then session.status="load_failed";session.error="no_plot";publish(player);return end
    session.busy=true;session.status="loading";session.error=nil;publish(player)
    local ok,code,data
    if LOCAL then ok,code,data=true,"local_session_only",Schema.copyData(Rules.newProfile())
    elseif store then ok,code,data=store.open(session.handle)
    else ok,code=false,"wrong_environment" end
    if ok then
        session.profile=Rules.newProfile()
        for _,key in ipairs(Schema.fields) do session.profile[key]=data[key] end
        session.profile.active=false;session.savedStateVersion=session.profile.stateVersion
        session.nextSave=os.clock()+ProfileStore.saveInterval
        if not session.leaving then
            WorldBuilder.SetLevel(session.plot,session.profile.level);resume(session)
            if player.Character then player.Character:PivotTo(session.plot.SpawnCFrame) end
            print("BOLTBOTS_SESSION_START",code,"revision="..(if session.handle then session.handle.revision else 0),
                "cash="..session.profile.cash,"completed="..session.profile.completed,"level="..session.profile.level,"design="..session.profile.selectedDesign)
        end
    else
        session.status="load_failed";session.error=code;freePlot(session)
        warn("BOLTBOTS_LOAD_FAILED",code)
    end
    session.busy=false;publish(player)
end
command.OnServerInvoke = function(player: Player, kind, payload, ...)
    local session=sessions[player]
    if not session then return {ok=false,code="inactive",view=snapshot(player)} end
    local now=os.clock()
    if now-session.commandWindow>=1 then session.commandWindow=now;session.commandCount=0 end
    session.commandCount+=1
    if session.commandCount>6 then return {ok=false,code="rate_limited",view=snapshot(player)} end
    if select("#",...)~=0 then return {ok=false,code="invalid_request",view=snapshot(player)} end
    if kind=="retry" then
        if type(payload)~="table" or next(payload)~=nil or session.busy or session.leaving or now-session.lastRetry<3 then
            return {ok=false,code="rate_limited",view=snapshot(player)}
        end
        session.lastRetry=now
        if session.status=="load_failed" then loadSession(player,session)
        elseif session.status=="save_failed" then saveSession(player,session,false) end
        return {ok=session.status=="saved" or LOCAL,code=session.status,view=snapshot(player)}
    end
    if session.busy or session.leaving or not session.profile or not session.profile.active then
        return {ok=false,code="inactive",view=snapshot(player)}
    end
    local previousLevel=session.profile.level
    local result=Rules.command(session.profile,kind,payload)
    if session.profile.level~=previousLevel then
        WorldBuilder.SetLevel(session.plot,session.profile.level)
        print("BOLTBOTS_MACHINE_PURCHASE","starter","level=2","price="..Config.firstUpgradePrice,"cash="..session.profile.cash)
        print("BOLTBOTS_ROBOT_UNLOCKED","orbit");publish(player,"L2 ist da! Orbit freigeschaltet.")
    elseif result.ok and kind=="select" then publish(player) end
    return {requestId=result.requestId,ok=result.ok,code=result.code,view=snapshot(player)}
end
local function assignPlayer(player: Player)
    if sessions[player] then return end
    local session={profile=nil,plot=nil,commandWindow=0,commandCount=0,lastRetry=-10,
        version=0,status="loading",busy=false,leaving=false,nextSave=0,
        handle=if store then store.handle("player_"..player.UserId) else nil}
    sessions[player]=session
    session.characterConnection=player.CharacterAdded:Connect(function(character)
        local root=character:WaitForChild("HumanoidRootPart",10)
        if root and session.plot and not session.leaving then character:PivotTo(session.plot.SpawnCFrame) end
    end)
    loadSession(player,session)
end
local function removePlayer(player: Player)
    local session=sessions[player]
    if not session or session.leaving then return end
    session.leaving=true;pause(session)
    session.characterConnection:Disconnect()
    task.spawn(function()
        local deadline=os.clock()+25
        while session.busy and os.clock()<deadline do task.wait(0.1) end
        if not session.busy and session.profile and not LOCAL then saveSession(player,session,true) end
        freePlot(session);sessions[player]=nil
        print("BOLTBOTS_SESSION_END",session.status)
    end)
end
Players.PlayerAdded:Connect(assignPlayer)
Players.PlayerRemoving:Connect(removePlayer)
for _,player in ipairs(Players:GetPlayers()) do task.spawn(assignPlayer,player) end
game:BindToClose(function()
    for player in pairs(sessions) do removePlayer(player) end
    local deadline=os.clock()+25
    while next(sessions) and os.clock()<deadline do task.wait(0.1) end
end)

task.spawn(function()
    while true do
        local now = Workspace:GetServerTimeNow()
        for player, session in pairs(sessions) do
            local profile=session.profile
            if profile and profile.active and not LOCAL and not session.leaving
                and (os.clock()>=session.nextSave or os.time()>=session.handle.expiresAt-ProfileStore.safetySeconds) then
                pause(session);task.spawn(saveSession,player,session,false)
            end
            local cycle = profile and profile.cycle
            if profile and profile.active and cycle and now >= cycle.completesAt then
                local ok, reason = Rules.completeCycle(session.profile, cycle.id, now)
                if ok then
                    local profile = session.profile
                    if profile.completed <= 3 or profile.completed % 10 == 0 then
                        print("BOLTBOTS_COMPLETE", "cycle=" .. cycle.id, "cash=" .. profile.cash,
                            "completed=" .. profile.completed, "scout=" .. tostring(profile.unlockedScout), "design="..cycle.designId, "seconds="..(cycle.completesAt-cycle.startedAt))
                    end
                    if profile.completed == 1 then print("BOLTBOTS_ROBOT_UNLOCKED", "scout") end
                    startCycle(session)
                    publish(player, if profile.completed == 1 then "Scout entdeckt! +25 Factory Cash" else nil)
                else
                    Rules.stop(session.profile)
                    session.plot.Model:SetAttribute("Active", false)
                    publish(player, "Produktion pausiert: " .. reason)
                end
            end
        end
        task.wait(0.1)
    end
end)
print("BOLTBOTS_SERVER_BOOT", Config.project, Config.versionLabel)
