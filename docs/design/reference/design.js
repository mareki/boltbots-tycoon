/* design_reference_only · non_promotable · deterministic fixtures, no game/backend calls. */
(function (root) {
  'use strict';
  const C = {ink:'#101B35',panel:'#172B4D',cyan:'#48D8F4',amber:'#FFCE53',coral:'#FF956B',violet:'#A784F7',ok:'#5AD9A6',danger:'#F4747B',text:'#F4F8FF',muted:'#B9C8DB',light:'#E7F3FF'};
  const states = ['world','upgrade','upgraded','collection','save_error','orbit_selected','collection_initial'];
  const esc = s => String(s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
  function rect(x,y,w,h,fill,r=16,extra=''){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}" ${extra}/>`;}
  function text(x,y,t,size=16,fill=C.text,weight=400,extra=''){return `<text x="${x}" y="${y}" font-size="${size}" fill="${fill}" font-weight="${weight}" ${extra}>${esc(t)}</text>`;}
  function line(x1,y1,x2,y2,col,width=2){return `<path d="M${x1} ${y1}L${x2} ${y2}" stroke="${col}" stroke-width="${width}" fill="none"/>`;}
  function robot(x,y,s,col=C.cyan,family=0){
    return `<g transform="translate(${x} ${y}) scale(${s})">${rect(-29,49,22,19,'#233C59',7)}${rect(8,49,22,19,'#233C59',7)}${rect(-30,10,60,47,col,16)}${rect(-43,16,15,32,col,7)}${rect(28,16,15,32,col,7)}${rect(-34,-42,68,60,col,19)}${rect(-27,-32,54,36,C.ink,12)}<ellipse cx="-12" cy="-15" rx="5" ry="8" fill="${C.light}"/><ellipse cx="12" cy="-15" rx="5" ry="8" fill="${C.light}"/>${rect(-11,24,22,13,'#F4F8FF',5)}${line(0,-42,0,-53,'#35546B',5)}<circle cx="0" cy="-57" r="7" fill="${family===2?C.violet:C.amber}"/>${family===2?'<ellipse cx="0" cy="-14" rx="47" ry="15" stroke="#A784F7" stroke-width="5" fill="none" transform="rotate(-20)"/>':''}${family===1?'<path d="M-12 -45 L1 -67 L16 -45" fill="#FFCE53"/>':''}${family===3?'<path d="M-35 -29 L-48 -13 L-35 3 M35 -29 L48 -13 L35 3" fill="#FF956B"/>':''}${family===4?rect(-42,9,84,14,C.amber,5):''}${line(-18,-36,15,-36,'#FFFFFF',3)}</g>`;
  }
  function scene(x,y,w,h){
    return `<svg x="${x}" y="${y}" width="${w}" height="${h}" viewBox="0 0 820 470" preserveAspectRatio="xMidYMid meet"><defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="#BDEAFF"/><stop offset="1" stop-color="#EAF7FF"/></linearGradient><linearGradient id="floor" x2="0" y2="1"><stop stop-color="#E9F4FA"/><stop offset="1" stop-color="#BCD3E1"/></linearGradient></defs>${rect(0,0,820,470,'url(#sky)',0)}<circle cx="705" cy="55" r="85" fill="#FFF8D9"/><g opacity=".5">${rect(20,45,90,170,'#A6CDD9',8)}${rect(129,85,80,128,'#B5D7E3',8)}${rect(622,80,60,130,'#C0DDE5',8)}${rect(713,110,75,120,'#A9D0DF',8)}</g><path d="M0 185L820 130V470H0Z" fill="url(#floor)"/>${[0,1,2,3,4,5,6].map(i=>line(i*160-250,470,i*160+55,165,'#A6C4D3',1)).join('')}${[225,300,395].map(t=>line(0,t,820,t-45,'#C3D9E4',1)).join('')}<path d="M50 350L646 289L792 354L195 431Z" fill="#8AAFC1" opacity=".28"/><path d="M49 304L629 241L773 308L194 374Z" fill="#365976"/><path d="M194 374L773 308V337L194 402Z" fill="#233E5C"/><path d="M49 304L194 374V402L49 332Z" fill="#466B86"/><path d="M71 303L628 256L746 307L194 357Z" fill="#78CEE5"/>${Array.from({length:16},(_,i)=>line(91+i*35,305-i*3,200+i*35,351-i*3,'#315B75',5)).join('')}${line(194,367,764,313,C.cyan,5)}<path d="M90 247L191 237L245 262L144 277Z" fill="#FFDA77"/><path d="M90 247L144 277V322L90 293Z" fill="#D69934"/><path d="M144 277L245 262V306L144 322Z" fill="#F4BB4D"/>${robot(205,277,.43,C.cyan)}<path d="M304 148L424 135L493 168L373 182Z" fill="#FFFFFF"/><path d="M304 148L373 182V306L304 273Z" fill="#8BAABD"/><path d="M373 182L493 168V293L373 306Z" fill="#E7F3FF"/>${rect(389,193,82,57,C.ink,9)}${text(404,217,'ASSEMBLER',9,C.muted,700)}${rect(404,228,52,7,C.cyan,3)}<path d="M354 157L367 85L411 68L461 96" stroke="#9A7B3C" stroke-width="24" fill="none" stroke-linejoin="round"/><path d="M354 151L367 80L411 65L461 92" stroke="#FFCE53" stroke-width="18" fill="none" stroke-linejoin="round"/><circle cx="367" cy="80" r="14" fill="#FFF0A6"/><circle cx="411" cy="65" r="12" fill="#F8B63E"/>${line(461,92,466,124,'#31536F',9)}${line(458,124,449,144,'#31536F',5)}${line(474,123,483,140,'#31536F',5)}${robot(511,256,.52,C.cyan)}<path d="M584 209L672 200L718 222L631 234Z" fill="#FFDA82"/><path d="M584 209L631 234V283L584 258Z" fill="#CC9240"/><path d="M631 234L718 222V271L631 283Z" fill="#EFB85C"/>${line(628,214,671,207,'#A97838',4)}${robot(675,312,.57,C.ok)}<ellipse cx="660" cy="410" rx="64" ry="18" fill="#7BA3B7" opacity=".35"/><ellipse cx="660" cy="396" rx="61" ry="18" fill="#456D89"/><path d="M599 385V396C599 420 721 420 721 396V385Z" fill="#B2D5E4"/><ellipse cx="660" cy="385" rx="61" ry="18" fill="#F4FBFF"/>${robot(660,343,.64,C.cyan)}${text(22,441,'TEILE',12,'#31536F',700)}${text(326,431,'ASSEMBLER',12,'#31536F',700)}${text(563,451,'VERPACKUNG → CASH',12,'#31536F',700)}<g opacity=".8">${rect(24,182,70,12,'#88B8C7',6)}${rect(39,160,40,27,'#70A883',10)}</g></svg>`;
  }
  function render(state='world', width=1280, height=800){
    if(!states.includes(state)) throw new Error('Unknown fixture');
    const mobile=width<650, success=['upgraded','collection','save_error','orbit_selected'].includes(state), collection=['collection','orbit_selected','collection_initial'].includes(state), error=state==='save_error';
    const cash=success?100:150, level=success?2:1, rate=success?'30 Cash / 6 s':'25 Cash / 7 s';
    const a=[];let body='';
    function button(id,x,y,w,h,label,next,fill=C.cyan,disabled=false){
      a.push({id,x,y,w,h,label,next,disabled});
      return rect(x,y,w,h,disabled?'#38516A':fill,12)+text(x+w/2,y+h/2+6,label,16,disabled?C.muted:(fill===C.panel?C.text:C.ink),700,'text-anchor="middle"');
    }
    function nav(y){const gap=8,margin=mobile?16:32,bw=mobile?(width-48)/3:150;return ['Fabrik','Ausbauen','Sammlung'].map((label,i)=>button('nav'+i,margin+i*(bw+gap),y,bw,48,label,[success?'upgraded':'world',success?'upgraded':'upgrade',success?'collection':'collection_initial'][i],((collection&&i===2)||(!collection&&state==='upgrade'&&i===1)||state==='world'&&i===0)?C.cyan:C.panel,error)).join('');}
    function status(){return text(mobile?24:width-210,mobile?105:46,error?'! Speichern unbestätigt':'● Beispiel: gespeichert',14,error?C.danger:C.ok,600);}
    function machineCard(x,y,w){
      let b=rect(x,y,w,error?220:286,C.panel,20)+text(x+20,y+32,'STARTER-ASSEMBLER',14,C.muted,700)+text(x+20,y+64,`Level ${level}`,28,C.text,750);
      if(error){return b+text(x+20,y+99,'Fortschritt pausiert',20,C.danger,700)+text(x+20,y+127,'Dein letzter bestätigter Stand bleibt.',14,C.muted)+text(x+20,y+150,'Produktion und Käufe warten.',14,C.muted)+button('retry',x+20,y+170,w-40,44,'Erneut versuchen','upgraded',C.amber);}
      if(success){return b+text(x+20,y+100,'✓ Ausbau geschafft',20,C.ok,700)+text(x+20,y+132,'Orbit ist jetzt freigeschaltet.',15,C.text)+text(x+20,y+157,'Wähle dein nächstes Design.',15,C.muted)+button('go-collection',x+20,y+185,w-40,48,'Sammlung öffnen','collection',C.amber);}
      b+=text(x+20,y+97,'Schneller produzieren',20,C.text,700)+text(x+20,y+128,'Level 1 → Level 2',16,C.muted)+text(x+20,y+153,'Danach: Orbit freigeschaltet',14,C.cyan);
      if(state==='upgrade')b+=button('buy',x+20,y+174,w-40,46,'Für 50 Cash verbessern','upgraded',C.amber)+button('cancel',x+20,y+226,w-40,44,'Abbrechen','world',C.panel);
      else b+=button('open',x+20,y+185,w-40,48,'Ausbau ansehen','upgrade',C.amber);
      return b;
    }
    function collectionCards(x,y,w){
      const names=['Scout','Orbit','Bolt','Luma','Atlas'],cols=[C.cyan,C.violet,C.amber,C.coral,C.ok];
      const cw=mobile?(w-12)/2:(w-48)/5,ch=mobile?181:280,gap=12;
      return names.map((name,i)=>{
        const cx=x+(i%(mobile?2:5))*(cw+gap),cy=y+Math.floor(i/(mobile?2:5))*(ch+gap),free=i<(success?2:1);
        let card=rect(cx,cy,cw,ch,C.panel,16)+robot(cx+cw/2,cy+(mobile?52:99),mobile?.5:.95,cols[i],[0,2,1,3,4][i])+text(cx+14,cy+(mobile?105:183),name,mobile?18:22,C.text,700)+text(cx+14,cy+(mobile?126:208),free?'Freigeschaltet':'Noch gesperrt',14,free?C.ok:C.muted);
        if(free)card+=button('select-'+i,cx+8,cy+ch-50,cw-16,44,name==='Orbit'?'Orbit wählen':'Scout wählen',name==='Orbit'?'orbit_selected':success?'upgraded':'world',C.cyan);
        return card;
      }).join('');
    }
    body+=rect(0,0,width,height,C.ink,0);
    body+=rect(mobile?16:32,20,32,32,C.cyan,9)+text(mobile?32:48,44,'B',23,C.ink,800,'text-anchor="middle"')+text(mobile?58:78,44,'BOLTBOTS',mobile?21:24,C.text,800);
    if(!mobile) body+=text(248,44,'DEINE KLEINE ROBOTERFABRIK',14,C.muted,600);
    const cx=mobile?width-123:width-425;body+=rect(cx,17,mobile?107:190,42,C.panel,14)+text(cx+15,44,`${cash} Cash`,mobile?18:22,C.amber,750);body+=status();
    if(mobile){
      body+=text(20,83,rate,14,C.muted,500);
      if(collection){
        body+=text(20,143,'Deine Roboter',28,C.text,750)+text(20,170,state==='orbit_selected'?'Orbit startet im nächsten Durchlauf.':`${success?2:1} von 5 Designs freigeschaltet`,14,C.muted)+collectionCards(16,190,width-32);
        body+=nav(height-64);
      } else {
        body+=rect(16,122,width-32,66,error?'#3E2B40':C.panel,16)+text(30,146,error?'SPEICHERPROBLEM':success?'NEUES DESIGN':'DEIN NÄCHSTES ZIEL',14,error?C.danger:C.cyan,700)+text(30,174,error?'Dein Fortschritt wartet sicher.':success?'Entdecke Orbit in der Sammlung.':'Verbessere deinen Assembler.',17,C.text,650);
        body+=scene(0,202,width,239)+machineCard(16,449,width-32)+nav(height-64);
        body+=text(20,755,error?'Keine neuen Änderungen, bis Speichern bestätigt ist.':success?'✓ Orbit freigeschaltet':'Scout entsteht automatisch. Cash kommt von selbst.',14,error?C.muted:C.cyan);
      }
    } else {
      body+=text(35,100,collection?'Deine Robotersammlung':'Ein kleiner Scout. Dein großer Anfang.',30,C.text,750)+text(35,129,collection?(state==='orbit_selected'?'Orbit produziert ab dem nächsten Durchlauf.':'Fünf Designs. Jedes mit einem eigenen Charakter.'):'Produzieren, verbessern und deine Lieblingsroboter sammeln.',16,C.muted);
      if(collection){body+=collectionCards(32,180,width-64)+rect(32,483,width-64,100,C.panel,20)+text(56,521,'DEIN NÄCHSTES ZIEL',14,C.cyan,700)+text(56,553,'Baue deine Fabrik weiter aus und entdecke neue Designs.',22,C.text,650);}
      else {
        body+=rect(32,160,830,502,'#BDEAFF',24)+scene(37,177,820,470)+rect(52,179,329,73,C.ink,16)+text(70,204,error?'FORTSCHRITT PAUSIERT':success?'ORBIT FREIGESCHALTET':'DEIN NÄCHSTES ZIEL',14,error?C.danger:C.cyan,700)+text(70,233,error?'Speichern erneut versuchen':success?'Öffne deine Sammlung':'Starter-Assembler auf Level 2',18,C.text,650);
        body+=machineCard(886,160,362)+rect(886,454,362,115,C.panel,20)+text(906,488,'PRODUKTION',14,C.muted,700)+text(906,522,rate,25,C.cyan,700)+text(906,548,error?'Pausiert, bis Speichern bestätigt ist.':'Cash wird automatisch gutgeschrieben.',14,C.muted);
        body+=rect(886,591,362,71,error?'#3E2B40':C.panel,18)+text(906,620,error?'! Speichern nicht bestätigt':'✓ Deine Fabrik, dein Fortschritt',16,error?C.danger:C.ok,650)+text(906,645,error?'Bestätigter Stand bleibt erhalten.':'Hier kann nur dein Konto ausbauen.',14,C.muted);
      }
      body+=nav(height-80)+text(width-320,height-50,'FREIE PROGRESSION · OHNE ROBUX',14,C.muted,600);
    }
    const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="BoltBots Designreferenz ${esc(state)}"><g font-family="Arial, Helvetica, sans-serif">${body}</g></svg>`;
    return {svg,actions:a,summary:`Designfixture ${state}. ${cash} Cash. Assembler Level ${level}. ${error?'Speichern nicht bestätigt; Fortschritt pausiert.':''}`,state,width,height};
  }
  const api={render,states,colors:C};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.BoltBotsDesign=api;
})(typeof globalThis!=='undefined'?globalThis:this);
