/* design_reference_only / non_promotable. Render the same SVG used by index.html. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const sharp=require('sharp'),design=require('./design.js');
const out=path.resolve(__dirname,'../../reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const matrix=[['world',1280,800],['upgrade',1280,800],['upgraded',1280,800],['collection',1280,800],['save_error',1280,800],['upgrade',390,844],['collection',390,844],['save_error',390,844]];
(async()=>{fs.mkdirSync(out,{recursive:true});const manifest={kind:'design_reference_only',revision:1,renderer:{node:process.version,sharp:sharp.versions.sharp},source:[],images:[],baselines:[],claims:'Native SVG PNG rendering and source inspection only; no browser or Studio execution.'};
 for(const name of ['index.html','design.js','render.cjs']){const b=fs.readFileSync(path.join(__dirname,name));manifest.source.push({path:'docs/design/reference/'+name,sha256:hash(b)});}
 for(const [state,w,h] of matrix){const model=design.render(state,w,h),name=`${state}-${w}x${h}.png`;await sharp(Buffer.from(model.svg)).png().toFile(path.join(out,name));manifest.images.push({id:`${state}-${w}`,surface:state==='collection'?'S-COLLECTION':state==='save_error'?'S-ERROR':state==='world'?'S-WORLD':state==='upgraded'?'S-RESULT':'S-UPGRADE',state,viewport:`${w}x${h}`,fixture:'fixed-r1',path:'docs/reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/'+name,sha256:hash(fs.readFileSync(path.join(out,name))),svg_sha256:hash(model.svg)});}
 for(const name of ['01_factory_world_concept.png','02_hud_concept.png','03_robot_shop_concept.png']){const source=path.resolve(__dirname,'../../product/reference/boltbots-v0.2/assets/mockups',name),dest='baseline-'+name;fs.copyFileSync(source,path.join(out,dest));manifest.baselines.push({id:dest,surface:name.startsWith('01')?'world':name.startsWith('02')?'HUD':'robots',state:'source-concept',viewport:'original native size',path:'docs/reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/'+dest,source:'docs/product/reference/boltbots-v0.2/assets/mockups/'+name,sha256:hash(fs.readFileSync(source))});}
 fs.writeFileSync(path.join(out,'render-manifest.json'),JSON.stringify(manifest,null,2)+'\n');console.log(`Rendered ${manifest.images.length} candidate PNGs; ${manifest.baselines.length} exact baseline copies.`);
})().catch(e=>{console.error(e.message);process.exitCode=1;});
