"use strict";

const runs = [];
const firstSeed = 42;
const byId = id => document.getElementById(id);
const mean = values => values.reduce((sum, value) => sum + value, 0) / values.length;
const format = value => value.toFixed(3);
const signed = value => (value > 0 ? "+" : "") + format(value);
// Match the genotype-frequency assumption used by alleleTrackerStep.
const modelFitness = (p, heterozygote, recessive) =>
  p * p + 2 * p * (1 - p) * heterozygote + (1 - p) ** 2 * recessive;

function summary(values) {
  const average = mean(values);
  return {
    count: values.length,
    mean: average,
    sample_sd: values.length > 1
      ? Math.sqrt(values.reduce((sum, value) => sum + (value - average) ** 2, 0) / (values.length - 1))
      : null,
    min: Math.min(...values),
    max: Math.max(...values)
  };
}

function buildExportRecord() {
  if (!runs.length) return null;
  const equal = [], different = [], differences = [];
  const entries = runs.map((run, index) => {
    const paired = run.different.map((value, i) => value - run.equal[i]);
    equal.push(...run.equal);
    different.push(...run.different);
    differences.push(...paired);
    return {
      run: index + 1,
      seed: run.seed,
      equal_fitness_final_frequencies: [...run.equal],
      fitness_difference_final_frequencies: [...run.different],
      paired_differences: paired,
      equal_fitness_run_mean: mean(run.equal),
      fitness_difference_run_mean: mean(run.different),
      paired_difference_run_mean: mean(paired),
      cumulative_equal_fitness_mean: mean(equal),
      cumulative_fitness_difference_mean: mean(different),
      cumulative_difference: mean(different) - mean(equal)
    };
  });
  return {
    schema: "beacon.allele_tracker_runs.v1",
    exported_at_utc: new Date().toISOString(),
    description: "Final allele frequencies from a model; descriptive results, not a significance test.",
    settings: {
      population_size: 40, populations_per_treatment: 5, generations: 30,
      initial_allele_frequency: 0.5, mutation_a_to_A: 0, mutation_A_to_a: 0, migration_rate: 0,
      genotype_fitness: {equal_fitness: {AA: 1, Aa: 1, aa: 1}, fitness_difference: {AA: 1, Aa: 0.95, aa: 0.9}},
      seed_method: "Both treatments use the same seed for each run; seeds increase by one starting at 42.",
      difference_definition: "fitness difference minus equal fitness, paired by seed and population position"
    },
    runs: entries,
    pooled: {
      runs_per_treatment: runs.length,
      equal_fitness_final_frequency: summary(equal),
      fitness_difference_final_frequency: summary(different),
      paired_difference: summary(differences),
      difference_between_treatment_means: mean(different) - mean(equal),
      equal_fitness_model_mean_fitness: mean(equal.map(p => modelFitness(p, 1, 1))),
      fitness_difference_model_mean_fitness: mean(different.map(p => modelFitness(p, 0.95, 0.9)))
    }
  };
}

function exportCsv(record) {
  const headers = ["run", "seed", ...[1,2,3,4,5].map(i => `equal_pop_${i}`),
    ...[1,2,3,4,5].map(i => `different_pop_${i}`), ...[1,2,3,4,5].map(i => `difference_pop_${i}`),
    "equal_run_mean", "different_run_mean", "difference_run_mean", "equal_cumulative_mean",
    "different_cumulative_mean", "cumulative_difference", "population_size", "generations",
    "initial_allele_frequency", "mutation_A_to_a", "mutation_a_to_A", "migration_rate",
    "equal_fitness_AA", "equal_fitness_Aa", "equal_fitness_aa", "different_fitness_AA", "different_fitness_Aa", "different_fitness_aa"];
  const rows = record.runs.map(run => [run.run, run.seed, ...run.equal_fitness_final_frequencies,
    ...run.fitness_difference_final_frequencies, ...run.paired_differences, run.equal_fitness_run_mean,
    run.fitness_difference_run_mean, run.paired_difference_run_mean, run.cumulative_equal_fitness_mean,
    run.cumulative_fitness_difference_mean, run.cumulative_difference, 40, 30, 0.5, 0, 0, 0, 1, 1, 1, 1, 0.95, 0.9]);
  return [headers, ...rows].map(row => row.join(",")).join("\r\n") + "\r\n";
}

function download(content, type, filename) {
  const url = URL.createObjectURL(new Blob([content], {type}));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function describe(values, showSign = false) {
  const average = mean(values);
  const sd = values.length > 1
    ? Math.sqrt(values.reduce((sum, value) => sum + (value - average) ** 2, 0) / (values.length - 1))
    : null;
  const display = showSign ? signed : format;
  return `n = ${values.length} · mean = ${display(average)} · sample SD = ${sd === null ? "—" : format(sd)} · range = ${display(Math.min(...values))} to ${display(Math.max(...values))}`;
}

function addRow(body, runNumber, seed, values, showSign = false) {
  const row = document.createElement("tr");
  const display = showSign ? signed : format;
  [String(runNumber), String(seed), ...values.map(display), display(mean(values))].forEach((value, index) => {
    const cell = document.createElement(index === 0 ? "th" : "td");
    if (index === 0) cell.scope = "row";
    cell.textContent = value;
    row.appendChild(cell);
  });
  body.appendChild(row);
}

function drawPlot(points) {
  const series = ["equal", "different", "delta"];
  const x = i => points.length === 1 ? 70 : 70 + 705 * i / (points.length - 1);
  const values = points.flatMap(point => series.map(key => point[key]));
  const dataMin = Math.min(0, ...values);
  const dataMax = Math.max(0, ...values);
  const span = dataMax - dataMin;
  // Include zero and a little breathing room; fall back when there is no spread.
  const lower = span > 1e-12 && dataMin < 0 ? Math.max(-1, dataMin - span * 0.05) : 0;
  const upper = span > 1e-12 && dataMax > 0 ? Math.min(1, dataMax + span * 0.05) : (span > 1e-12 ? 0 : 1);
  const y = value => 25 + 240 * (upper - value) / (upper - lower);
  for (let i = 0; i < 5; i++) {
    const tick = upper - (upper - lower) * i / 4;
    byId(`plot-y${i}`).textContent = Math.abs(tick) < 0.0005 ? "0.000" : tick.toFixed(3);
  }
  const names = {equal: "Equal fitness", different: "Fitness difference", delta: "Pooled difference"};
  series.forEach(key => {
    const group = byId(`plot-${key}`);
    group.textContent = "";
    points.forEach((point, i) => {
      const marker = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      marker.setAttribute("cx", x(i));
      marker.setAttribute("cy", y(point[key]));
      marker.setAttribute("r", 5);
      const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
      title.textContent = `Run ${i + 1}: ${names[key]} ${format(point[key])}`;
      marker.appendChild(title);
      group.appendChild(marker);
    });
  });
  byId("plot-last-run").textContent = points.length > 1 ? String(points.length) : "";
  if (!points.length) {
    byId("plot-status").textContent = "No runs yet. Add a run to show the pooled results.";
  } else {
    const last = points[points.length - 1];
    byId("plot-status").textContent = `After ${points.length} ${points.length === 1 ? "run" : "runs"}: equal fitness ${format(last.equal)}, fitness difference ${format(last.different)}, pooled difference ${signed(last.delta)}.`;
  }
}

function render() {
  byId("download-json").disabled = runs.length === 0;
  byId("download-csv").disabled = runs.length === 0;
  const bodies = [byId("equal-rows"), byId("different-rows"), byId("difference-rows")];
  bodies.forEach(body => { body.textContent = ""; });
  if (!runs.length) {
    bodies.forEach(body => {
      const row = document.createElement("tr");
      const cell = document.createElement("td");
      cell.colSpan = 8;
      cell.textContent = "No runs yet.";
      row.appendChild(cell);
      body.appendChild(row);
    });
    byId("equal-summary").textContent = "No pooled results yet.";
    byId("different-summary").textContent = "No pooled results yet.";
    byId("pooled-difference").textContent = "—";
    byId("difference-summary").textContent = "Add a run to calculate differences.";
    byId("result").textContent = `No runs yet. The first run uses seed ${firstSeed}.`;
    byId("dashboard-runs").textContent = "0";
    ["dashboard-equal-frequency", "dashboard-equal-fitness", "dashboard-different-frequency", "dashboard-different-fitness", "dashboard-difference"].forEach(id => { byId(id).textContent = "—"; });
    drawPlot([]);
    return;
  }
  const equal = [], different = [], differences = [];
  const plotPoints = [];
  runs.forEach((run, i) => {
    const delta = run.different.map((value, j) => value - run.equal[j]);
    equal.push(...run.equal);
    different.push(...run.different);
    differences.push(...delta);
    plotPoints.push({equal: mean(equal), different: mean(different), delta: mean(different) - mean(equal)});
    addRow(bodies[0], i + 1, run.seed, run.equal);
    addRow(bodies[1], i + 1, run.seed, run.different);
    addRow(bodies[2], i + 1, run.seed, delta, true);
  });
  drawPlot(plotPoints);
  byId("equal-summary").textContent = `Pooled: ${describe(equal)}`;
  byId("different-summary").textContent = `Pooled: ${describe(different)}`;
  byId("pooled-difference").textContent = `${signed(mean(different) - mean(equal))} allele-frequency units`;
  byId("dashboard-runs").textContent = String(runs.length);
  byId("dashboard-equal-frequency").textContent = format(mean(equal));
  byId("dashboard-different-frequency").textContent = format(mean(different));
  byId("dashboard-equal-fitness").textContent = format(mean(equal.map(p => modelFitness(p, 1, 1))));
  byId("dashboard-different-fitness").textContent = format(mean(different.map(p => modelFitness(p, 0.95, 0.9))));
  byId("dashboard-difference").textContent = signed(mean(different) - mean(equal));
  byId("difference-summary").textContent = `Pooled paired differences: ${describe(differences, true)}. Means and SD use unrounded values; displayed values are rounded to three decimals.`;
  byId("result").textContent = `${runs.length} ${runs.length === 1 ? "run" : "runs"} · latest seed ${runs[runs.length - 1].seed} · ${equal.length} population results per treatment.`;
}

byId("run").addEventListener("click", () => {
  const seed = firstSeed + runs.length;
  const base = {seed, populationSize: 40, numPop: 5, generations: 30, initFreq: 0.5, fitnessAA: 1, fitnessAa: 1, fitnessaa: 1};
  const equal = evoEduApis.populationGenetics.alleleTracker.runSimulation(base).final;
  const different = evoEduApis.populationGenetics.alleleTracker.runSimulation({...base, fitnessAa: 0.95, fitnessaa: 0.9}).final;
  runs.push({seed, equal, different});
  render();
});
byId("clear").addEventListener("click", () => { runs.length = 0; render(); });
byId("download-json").addEventListener("click", () => {
  const record = buildExportRecord();
  if (record) download(JSON.stringify(record, null, 2) + "\n", "application/json", "allele-tracker-runs.json");
});
byId("download-csv").addEventListener("click", () => {
  const record = buildExportRecord();
  if (record) download(exportCsv(record), "text/csv;charset=utf-8", "allele-tracker-runs.csv");
});
