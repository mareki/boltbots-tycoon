/* BoltBots design r3 — design_reference_only / non_promotable. Synthetic UI states, no game/backend. */
(function(root){
'use strict';
const C={ink:'#101B35',panel:'#172B4D',cyan:'#48D8F4',amber:'#FFCE53',coral:'#FF956B',violet:'#A784F7',ok:'#5AD9A6',danger:'#F4747B',text:'#F4F8FF',muted:'#B9C8DB'};
const names=['Scout','Orbit','Bolt','Luma','Atlas'],colors=[C.cyan,C.violet,C.amber,C.coral,C.ok];
const portraits=[[0,380],[380,354],[734,380],[1114,348],[1462,521]];
const presets={world:{page:'factory',profile:'before',selected:0,focus:0},upgrade:{page:'upgrade',profile:'before',selected:0,focus:0},upgraded:{page:'celebrate',profile:'after',selected:0,focus:1},collection:{page:'collection',profile:'after',selected:0,focus:1},save_error:{page:'error',profile:'after',selected:0,focus:0},orbit_selected:{page:'collection',profile:'after',selected:1,focus:1},collection_initial:{page:'collection',profile:'before',selected:0,focus:0}};
const fixture=name=>{if(!presets[name])throw Error('Unknown fixture');return {...presets[name]};};
function step(current,id){const s={...current};if(s.page==='error'){if(id==='retry')s.page='factory';return s;}if(id==='factory'||id==='cancel')s.page='factory';else if(id==='upgrade')s.page='upgrade';else if(id==='collection'){s.page='collection';s.focus=s.profile==='after'?1:0;}else if(id==='buy'&&s.page==='upgrade'&&s.profile==='before'){s.profile='after';s.page='celebrate';s.focus=1;}else if(id.startsWith('detail-')){s.focus=Number(id.slice(7));}else if(id.startsWith('select-')){const n=Number(id.slice(7));if(n===0||(n===1&&s.profile==='after')){s.selected=n;s.focus=n;s.page='collection';}}return s;}
const esc=t=>String(t).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
const rect=(x,y,w,h,fill,r=16,extra='')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}" ${extra}/>`;
const text=(x,y,t,size=16,fill=C.text,weight=500,extra='')=>`<text x="${x}" y="${y}" font-size="${size}" fill="${fill}" font-weight="${weight}" ${extra}>${esc(t)}</text>`;
const line=(x1,y1,x2,y2,color,opacity=1)=>`<path d="M${x1} ${y1}L${x2} ${y2}" stroke="${color}" stroke-opacity="${opacity}"/>`;
function render(input='world',width=1280,height=800,assets={world:'assets/factory-r3.png',robots:'assets/robots-r3.png'}){
 const s=typeof input==='string'?fixture(input):{...input},mobile=width<650,after=s.profile==='after',error=s.page==='error',collection=s.page==='collection',cash=after?100:150,level=after?2:1;
 const actions=[];let out='',uid=0;
 const label=(x,y,t,color=C.muted)=>text(x,y,t,14,color,650);
 const panel=(x,y,w,h,fill='url(#glass)',r=22)=>rect(x,y,w,h,fill,r,`stroke="#B9D9F5" stroke-opacity=".2" filter="url(#shadow)"`);
 function button(id,x,y,w,h,caption,fill=C.amber,disabled=false,small=false){actions.push({id,x,y,w,h,label:caption,disabled});return rect(x,y+3,w,h,disabled?'#243650':'#050C19',14)+rect(x,y,w,h,disabled?'#31455F':fill,14,`stroke="#FFFFFF" stroke-opacity="${disabled?.06:.22}"`)+text(x+w/2,y+h/2+6,caption,small?14:16,disabled?C.muted:fill===C.panel?C.text:C.ink,750,'text-anchor="middle"');}
 function robot(i,x,y,w,h){const [sx,sw]=portraits[i];const id='portrait'+(++uid);return rect(x,y,w,h,'#101E36',14)+`<svg x="${x}" y="${y}" width="${w}" height="${h}" viewBox="0 0 ${sw} 793" preserveAspectRatio="xMidYMid meet"><defs><clipPath id="${id}"><rect width="${sw}" height="793"/></clipPath><linearGradient id="${id}-fade"><stop stop-color="black"/><stop offset=".025" stop-color="white"/><stop offset=".975" stop-color="white"/><stop offset="1" stop-color="black"/></linearGradient><mask id="${id}-mask"><rect width="${sw}" height="793" fill="url(#${id}-fade)"/></mask></defs><g clip-path="url(#${id})" mask="url(#${id}-mask)"><image href="${assets.robots}" x="${-sx}" width="1983" height="793"/></g></svg>`;}
 function nav(){const y=height-(mobile?72:84),w=mobile?width-32:456,x=(width-w)/2,bw=(w-16)/3;let b=panel(x,y,w,60,'#0B172BEF',20);for(let i=0;i<3;i++){const id=['factory','upgrade','collection'][i],active=(i===0&&s.page==='factory')||(i===1&&s.page==='upgrade')||(i===2&&collection);b+=button(id,x+8+i*bw,y+7,bw-4,44,['Fabrik','Ausbauen','Sammlung'][i],active?C.cyan:C.panel,error,mobile);}return b;}
 const defs=`<defs><linearGradient id="glass" x2="0" y2="1"><stop stop-color="#172B4D" stop-opacity=".98"/><stop offset="1" stop-color="#0B172D" stop-opacity=".98"/></linearGradient><linearGradient id="topShade" x2="0" y2="1"><stop stop-color="#071427" stop-opacity=".92"/><stop offset="1" stop-color="#071427" stop-opacity="0"/></linearGradient><linearGradient id="bottomShade" x2="0" y2="1"><stop stop-color="#071427" stop-opacity="0"/><stop offset="1" stop-color="#071427" stop-opacity=".94"/></linearGradient><linearGradient id="gold" x2="0" y2="1"><stop stop-color="#FFE697"/><stop offset="1" stop-color="#FFBD35"/></linearGradient><filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#020918" flood-opacity=".35"/></filter></defs>`;
 out+=rect(0,0,width,height,C.ink,0);
 if(!collection){
  if(mobile)out+=`<image href="${assets.world}" x="-130" y="137" width="942" height="530" preserveAspectRatio="xMidYMid slice"/>`;
  else out+=`<image href="${assets.world}" width="${width}" height="${height}" preserveAspectRatio="xMidYMid slice"/>`;
  out+=rect(0,0,width,mobile?205:225,'url(#topShade)',0)+rect(0,mobile?480:height-275,width,mobile?364:275,'url(#bottomShade)',0);
 }else{
  out+=`<image href="${assets.world}" width="${width}" height="${height}" preserveAspectRatio="xMidYMid slice" opacity=".13"/>`+rect(0,0,width,height,'#101B35',0,'opacity=".85"');
 }
 // Compact game HUD; the workshop remains the main visual surface.
 out+=panel(mobile?14:28,18,mobile?176:219,52,'#0B172BF2',17)+rect(mobile?26:42,30,29,29,C.cyan,8)+text(mobile?40.5:56.5,51,'B',22,C.ink,850,'text-anchor="middle"')+text(mobile?64:84,51,'BOLTBOTS',mobile?19:22,C.text,800);
 const moneyX=mobile?width-184:width-237;
 out+=panel(moneyX,18,mobile?170:209,52,'#0B172BF2',17)+`<circle cx="${moneyX+26}" cy="44" r="13" fill="url(#gold)" stroke="#FFE49A"/>`+text(moneyX+26,49,'C',14,'#946319',800,'text-anchor="middle"')+text(moneyX+49,51,`${cash} Cash`,mobile?20:24,C.amber,750);
 if(!mobile)out+=panel(width-438,18,183,52,'#0B172BF2',17)+text(width-418,51,error?'Produktion pausiert':after?'30 Cash / 6 s':'25 Cash / 7 s',16,error?C.danger:C.text,600);
 if(mobile&&!collection)out+=text(18,94,error?'! Speichern nicht bestätigt':after?'30 Cash / 6 s · Assembler Level 2':'25 Cash / 7 s · Assembler Level 1',14,error?C.danger:C.muted,600);
 function mission(){const x=mobile?14:28,y=mobile?110:94,w=mobile?width-28:337;return panel(x,y,w,mobile?83:100,'#0B172BED',19)+label(x+18,y+26,error?'FORTSCHRITT PAUSIERT':after?'DEIN NÄCHSTES DESIGN':'DEIN NÄCHSTER SCHRITT',error?C.danger:C.cyan)+text(x+18,y+54,error?'Dein Stand bleibt erhalten.':after?'Orbit wartet auf dich.':'Assembler auf Level 2',mobile?19:22,C.text,750)+(mobile?'':text(x+18,y+80,error?'Versuche das Speichern erneut.':after?'Öffne deine Sammlung.':'Schalte den kleinen Orbit frei.',16,C.muted));}
 if(!collection)out+=mission();
 if(s.page==='factory'){
  const x=mobile?14:width-357,y=mobile?582:height-297,w=mobile?width-28:329,h=mobile?165:181;
  out+=panel(x,y,w,h)+label(x+20,y+28,after?'DEINE PRODUKTION':'STARTER-ASSEMBLER')+text(x+20,y+61,after?`${names[s.selected]} ist bereit`:'Mehr Tempo. Mehr Freunde.',20,C.text,750)+text(x+20,y+88,after?'Auswahl gilt ab nächstem Durchlauf.':'Verbessere deinen Assembler.',14,C.muted);
  out+=button(after?'collection':'upgrade',x+20,y+106,w-40,48,after?'Roboter auswählen':'Ausbau ansehen');
  if(!mobile)out+=panel(28,height-163,294,58,'#0B172BEF',18)+text(46,height-129,after?'✓ Level 2 · Fortschritt bestätigt':'✓ Scout produziert automatisch',16,C.text,600);
 }else if(s.page==='upgrade'){
  const x=mobile?14:width-408,y=mobile?437:247,w=mobile?width-28:380,h=mobile?310:394;
  out+=panel(x,y,w,h)+label(x+22,y+31,'STARTER-ASSEMBLER',C.cyan)+text(x+22,y+66,after?'Dein Assembler ist Level 2':'Mach Platz für neue Ideen.',mobile?22:25,C.text,750);
  if(!after){
   out+=rect(x+22,y+86,w-44,66,'#233B58',14)+text(x+40,y+113,'LEVEL 1',14,C.muted,650)+text(x+40,y+139,'25 Cash / 7 s',16,C.text,650)+text(x+w/2,y+126,'→',23,C.cyan,750,'text-anchor="middle"')+text(x+w-40,y+113,'LEVEL 2',14,C.amber,650,'text-anchor="end"')+text(x+w-40,y+139,'30 Cash / 6 s',16,C.text,650,'text-anchor="end"');
   out+=text(x+22,y+179,'Außerdem freigeschaltet: Orbit',16,C.text,650);
   if(!mobile)out+=text(x+22,y+207,'Klein, neugierig und voller Möglichkeiten.',14,C.muted)+text(x+22,y+236,'Nach dem Kauf bleiben dir 100 Cash.',14,C.muted);
   const by=mobile?y+202:y+265;out+=button('buy',x+22,by,w-44,48,'Für 50 Cash verbessern')+button('cancel',x+22,by+57,w-44,44,'Abbrechen',C.panel);
  }else out+=text(x+22,y+106,'Orbit gehört jetzt zu deiner Sammlung.',16,C.muted)+button('collection',x+22,y+150,w-44,48,'Zur Sammlung')+button('cancel',x+22,y+209,w-44,44,'Zur Fabrik',C.panel);
 }else if(s.page==='celebrate'){
  const x=mobile?28:width-394,y=mobile?218:181,w=mobile?width-56:356;
  out+=panel(x,y,w,mobile?528:480)+label(x+w/2,y+30,'NEUES DESIGN',C.amber).replace('<text ','<text text-anchor="middle" ')+text(x+w/2,y+68,'Hallo, Orbit!',32,C.text,800,'text-anchor="middle"')+robot(1,x+50,y+84,w-100,mobile?280:252)+text(x+w/2,y+(mobile?386:365),'Dein nächster kleiner Fortschritt.',14,C.muted,500,'text-anchor="middle"')+button('collection',x+22,y+(mobile?415:393),w-44,48,'Orbit in der Sammlung ansehen');
 }else if(error){
  const x=mobile?14:width-425,y=mobile?454:281,w=mobile?width-28:397;
  out+=panel(x,y,w,mobile?289:300,'#18283FF7')+rect(x+22,y+20,37,37,'#582C40',12)+text(x+40.5,y+47,'!',24,C.danger,800,'text-anchor="middle"')+text(x+22,y+88,'Wir halten deinen Platz.',mobile?23:26,C.text,750)+text(x+22,y+121,'Speichern wurde nicht bestätigt.',16,C.danger,650)+text(x+22,y+153,'Produktion und Käufe pausieren.',16,C.muted)+text(x+22,y+178,'Dein bestätigter Stand bleibt erhalten.',14,C.muted)+button('retry',x+22,y+214,w-44,48,'Speichern erneut versuchen');
 }else if(collection){
  if(mobile){
   out+=text(19,115,'Deine Sammlung',28,C.text,800)+text(20,143,`${after?2:1} von 5 Designs freigeschaltet`,14,C.muted);
   const i=s.focus,free=i===0||(i===1&&after),chosen=s.selected===i;
   out+=panel(14,163,width-28,425,'#101B35',24)+robot(i,55,173,width-110,304)+text(width/2,508,names[i],31,C.text,800,'text-anchor="middle"')+text(width/2,538,free?(chosen?'Für den nächsten Durchlauf gewählt':'Bereit für deine Fabrik'):'Dieses Design ist noch gesperrt.',14,free?C.cyan:C.muted,600,'text-anchor="middle"');
   for(let j=0;j<5;j++){const x=14+j*73;out+=rect(x,602,69,78,j===i?'#27435E':'#14243E',12,`stroke="${j===i?colors[j]:'#30445B'}"`)+robot(j,x+8,606,53,48)+text(x+34.5,674,names[j],14,j===i?C.text:C.muted,650,'text-anchor="middle"');actions.push({id:'detail-'+j,x,y:602,w:69,h:78,label:names[j]+' ansehen',disabled:false});}
   out+=button('select-'+i,14,703,width-28,48,free?(chosen?'Für Produktion ausgewählt':`${names[i]} produzieren`):'Noch gesperrt',free?colors[i]:C.panel,!free||chosen);
  }else{
   out+=text(32,130,'Kleine Roboter. Große Persönlichkeiten.',36,C.text,800)+text(34,165,`${after?2:1} von 5 Designs freigeschaltet · Wähle, wer als Nächstes vom Band rollt.`,18,C.muted);
   const gap=14,cw=(width-64-4*gap)/5;
   for(let i=0;i<5;i++){const x=32+i*(cw+gap),free=i===0||(i===1&&after),chosen=s.selected===i;out+=panel(x,207,cw,438,'#101B35',20)+rect(x+16,220,cw-32,3,colors[i],1)+robot(i,x+8,235,cw-16,260)+text(x+18,529,names[i],25,C.text,750)+text(x+18,556,free?(chosen?'Produktion ausgewählt':'Freigeschaltet'):'Noch gesperrt',14,free?C.ok:C.muted,600)+button('select-'+i,x+14,580,cw-28,46,free?(chosen?'Ausgewählt':'Produzieren'):'Gesperrt',colors[i],!free||chosen);}
   out+=text(35,684,'Jedes Design bleibt in deiner Sammlung. Die Auswahl gilt ab dem nächsten Durchlauf.',16,C.muted);
  }
 }
 out+=nav();
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="BoltBots Designreferenz"><style>text{font-family:'Avenir Next',Arial,Helvetica,sans-serif}</style>${defs}${out}</svg>`;
 return {svg,actions,state:s,width,height,summary:`Designbeispiel: ${cash} Cash, Assembler Level ${level}, ${names[s.selected]} ausgewählt. ${error?'Speichern unbestätigt; Fortschritt pausiert.':''}`};
}
const api={render,step,fixture,states:Object.keys(presets),colors:C,names};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.BoltBotsDesign=api;
})(typeof globalThis!=='undefined'?globalThis:this);
