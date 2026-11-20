const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const api = require('../preview/population-genetics.js');

function setup() {
  class Element {
    constructor(tag = 'div') { this.tag = tag; this._text = ''; this.children = []; this.listeners = {}; this.attributes = {}; }
    set textContent(value) { this._text = value; this.children = []; }
    get textContent() { return this._text + this.children.map(child => child.textContent).join(''); }
    appendChild(child) { this.children.push(child); }
    setAttribute(key,value) { this.attributes[key] = String(value); }
    addEventListener(type, fn) { this.listeners[type] = fn; }
    click() { this.listeners.click(); }
  }
  const ids = ['run','clear','download-json','download-csv','result','equal-rows','different-rows','difference-rows','equal-summary','different-summary','pooled-difference','difference-summary','dashboard-runs','dashboard-equal-frequency','dashboard-equal-fitness','dashboard-different-frequency','dashboard-different-fitness','dashboard-difference','plot-equal','plot-different','plot-delta','plot-last-run','plot-status','plot-y0','plot-y1','plot-y2','plot-y3','plot-y4'];
  const elements = Object.fromEntries(ids.map(id => [id, new Element()]));
  const saved = [];
  class FakeBlob { constructor(parts, options) { this.content=parts.join(''); this.type=options.type; } }
  let currentBlob;
  const context = {evoEduApis:{populationGenetics:api}, Blob:FakeBlob,
    URL:{createObjectURL(blob){currentBlob=blob; return 'blob:test';}, revokeObjectURL(){}},
    setTimeout(fn){fn();},
    document:{getElementById(id){return elements[id];},
      body:{appendChild(){}},
      createElement(tag){
        if(tag==='a') return {click(){saved.push({name:this.download,blob:currentBlob});},remove(){}};
        return new Element(tag);
      }, createElementNS(ns,tag){return new Element(tag);}}};
  vm.runInNewContext(fs.readFileSync('preview/activity.js','utf8'),context);
  elements.saved = saved;
  elements.drawPlot = context.drawPlot;
  elements.buildExportRecord = context.buildExportRecord;
  elements.exportCsv = context.exportCsv;
  return elements;
}
function output(seed) {
  const base={seed,populationSize:40,numPop:5,generations:30,initFreq:.5,fitnessAA:1,fitnessAa:1,fitnessaa:1};
  return [api.alleleTracker.runSimulation(base).final,api.alleleTracker.runSimulation({...base,fitnessAa:.95,fitnessaa:.9}).final];
}
const mean = xs => xs.reduce((a,b)=>a+b,0)/xs.length;
const signed = x => (x>0?'+':'')+x.toFixed(3);

test('runs append all treatments, calculate pooled differences and clear', () => {
  const el=setup();
  assert.equal(el.buildExportRecord(),null);
  el.run.click();
  assert.equal(el['download-json'].disabled,false);
  assert.equal(el['download-csv'].disabled,false);
  assert.equal(el['equal-rows'].children.length,1);
  assert.equal(el['different-rows'].children.length,1);
  assert.equal(el['difference-rows'].children.length,1);
  assert.match(el.result.textContent,/1 run · latest seed 42 · 5 population/);
  const [a,b]=output(42);
  assert.equal(el['pooled-difference'].textContent,`${signed(mean(b)-mean(a))} allele-frequency units`);
  assert.match(el['equal-summary'].textContent,/n = 5/);
  assert.equal(el['dashboard-runs'].textContent,'1');
  assert.equal(el['dashboard-equal-frequency'].textContent,mean(a).toFixed(3));
  assert.equal(el['dashboard-equal-fitness'].textContent,'1.000');
  const fitness = p => p*p + 2*p*(1-p)*.95 + (1-p)**2*.9;
  assert.equal(el['dashboard-different-fitness'].textContent,mean(b.map(fitness)).toFixed(3));
  assert.equal(el['dashboard-difference'].textContent,signed(mean(b)-mean(a)));
  const firstTop=Number(el['plot-y0'].textContent);
  assert.ok(firstTop > mean(b) && firstTop < 1);
  assert.equal(el['plot-y4'].textContent,'0.000');
  assert.equal(el['plot-equal'].children.length,1);
  const firstY=Number(el['plot-equal'].children[0].attributes.cy);
  assert.ok(firstY>25 && firstY<265);
  assert.equal(el['plot-delta'].children.length,1);
  assert.match(el['plot-delta'].children[0].textContent,/Run 1: Pooled difference/);
  el.run.click();
  const [c,d]=output(43);
  assert.equal(el['equal-rows'].children.length,2);
  assert.equal(el['different-rows'].children.length,2);
  assert.equal(el['difference-rows'].children.length,2);
  assert.equal(el['equal-rows'].children[1].children[1].textContent,'43');
  assert.equal(el['pooled-difference'].textContent,`${signed(mean([...b,...d])-mean([...a,...c]))} allele-frequency units`);
  assert.match(el['difference-summary'].textContent,/n = 10/);
  assert.equal(el['dashboard-runs'].textContent,'2');
  assert.equal(el['dashboard-different-frequency'].textContent,mean([...b,...d]).toFixed(3));
  assert.equal(el['plot-last-run'].textContent,'2');
  const points=el['plot-delta'].children;
  assert.equal(points.length,2);
  assert.equal(Number(points[1].attributes.cx),775);
  const secondY=Number(points[1].attributes.cy);
  const top=Number(el['plot-y0'].textContent);
  const expectedY=25+240*(top-(mean([...b,...d])-mean([...a,...c])))/top;
  assert.ok(Math.abs(secondY-expectedY)<0.3);
  assert.match(el['plot-status'].textContent,/After 2 runs/);
  const exported=el.buildExportRecord();
  assert.equal(exported.settings.population_size,40);
  assert.equal(exported.settings.genotype_fitness.fitness_difference.Aa,.95);
  assert.equal(exported.runs.length,2);
  assert.equal(exported.runs[1].seed,43);
  assert.equal(exported.runs[0].equal_fitness_final_frequencies[0],a[0]);
  assert.equal(exported.pooled.equal_fitness_final_frequency.count,10);
  assert.equal(exported.pooled.difference_between_treatment_means,mean([...b,...d])-mean([...a,...c]));
  el['download-json'].click();
  el['download-csv'].click();
  assert.equal(el.saved[0].name,'allele-tracker-runs.json');
  assert.equal(JSON.parse(el.saved[0].blob.content).runs.length,2);
  assert.equal(el.saved[1].name,'allele-tracker-runs.csv');
  const csv=el.saved[1].blob.content.trim().split('\r\n').map(line=>line.split(','));
  assert.equal(csv.length,3);
  assert.equal(csv[0].length,csv[1].length);
  assert.equal(csv[0].length,csv[2].length);
  assert.equal(csv[1][csv[0].indexOf('equal_pop_1')],String(a[0]));
  assert.equal(csv[2][csv[0].indexOf('seed')],'43');
  const delta=b[0]-a[0];
  assert.equal(el['difference-rows'].children[0].children[2].textContent,signed(delta));
  el.clear.click();
  assert.equal(el['download-json'].disabled,true);
  assert.equal(el['download-csv'].disabled,true);
  assert.equal(el.buildExportRecord(),null);
  assert.equal(el['equal-rows'].children[0].textContent,'No runs yet.');
  assert.equal(el['pooled-difference'].textContent,'—');
  assert.equal(el['dashboard-runs'].textContent,'0');
  assert.equal(el['dashboard-different-fitness'].textContent,'—');
  assert.equal(el['plot-equal'].children.length,0);
  assert.equal(el['plot-delta'].children.length,0);
  assert.equal(el['plot-y0'].textContent,'1.000');
  assert.equal(el['plot-y4'].textContent,'0.000');
  el.run.click();
  assert.match(el.result.textContent,/seed 42/);
});


test('plot rescales for negative differences and handles identical zero values', () => {
  const el=setup();
  el.drawPlot([{equal:.2,different:.1,delta:-.1}]);
  assert.ok(Number(el['plot-y0'].textContent)>.2);
  assert.ok(Number(el['plot-y4'].textContent)<-.1);
  for(const id of ['plot-equal','plot-different','plot-delta']) {
    const y=Number(el[id].children[0].attributes.cy);
    assert.ok(y>=25 && y<=265, `${id} is in the plotting area`);
  }
  el.drawPlot([{equal:0,different:0,delta:0}]);
  assert.equal(el['plot-y0'].textContent,'1.000');
  assert.equal(el['plot-y4'].textContent,'0.000');
  assert.equal(el['plot-delta'].children[0].attributes.cy,'265');
});
