#!/usr/bin/env python3
"""Generate the self-contained WWDC Session Atlas HTML."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "session-atlas.json"
OUT = ROOT / "session-atlas.html"


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    payload = (
        json.dumps(data, ensure_ascii=False)
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )
    OUT.write_text(TEMPLATE.replace("__DATA__", payload), encoding="utf-8")
    print(OUT)


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WWDC Session Atlas</title>
<style>
:root {
  color-scheme: light dark;
  --bg: #f7f4ed;
  --ink: #1d1b17;
  --muted: #676057;
  --line: #d9d2c6;
  --panel: #fffdf8;
  --panel-2: #ece6da;
  --accent: #0f766e;
  --accent-2: #b84b2c;
  --blue: #27648d;
  --shadow: 0 20px 70px rgba(29, 27, 23, .12);
  --mono: "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  --serif: ui-serif, "Iowan Old Style", "Palatino Linotype", Georgia, serif;
  --sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
[data-theme="dark"] {
  color-scheme: dark;
  --bg: #121414;
  --ink: #f3efe4;
  --muted: #aaa397;
  --line: #343838;
  --panel: #191c1c;
  --panel-2: #222625;
  --accent: #54c2aa;
  --accent-2: #e18b69;
  --blue: #85b7d7;
  --shadow: 0 20px 80px rgba(0, 0, 0, .38);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #121414;
    --ink: #f3efe4;
    --muted: #aaa397;
    --line: #343838;
    --panel: #191c1c;
    --panel-2: #222625;
    --accent: #54c2aa;
    --accent-2: #e18b69;
    --blue: #85b7d7;
    --shadow: 0 20px 80px rgba(0, 0, 0, .38);
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; height: 100%; overflow: hidden; }
body {
  background:
    linear-gradient(90deg, color-mix(in srgb, var(--line) 36%, transparent) 1px, transparent 1px) 0 0 / 20px 20px,
    linear-gradient(0deg, color-mix(in srgb, var(--line) 28%, transparent) 1px, transparent 1px) 0 0 / 20px 20px,
    var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  letter-spacing: 0;
}
button, input, select { font: inherit; }
button {
  min-height: 34px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--panel);
  color: var(--ink);
  padding: 7px 10px;
  cursor: pointer;
}
button:hover { border-color: var(--accent); }
button.active { background: var(--ink); color: var(--bg); border-color: var(--ink); }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.app { display: grid; grid-template-rows: 60px 58px 1fr; height: 100vh; }
.topbar {
  display: grid;
  grid-template-columns: 330px minmax(320px, 1fr) auto auto;
  gap: 12px;
  align-items: center;
  padding: 10px 14px;
  border-bottom: 1px solid var(--line);
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  backdrop-filter: blur(16px);
}
.brand { min-width: 0; }
.brand h1 { font-family: var(--serif); font-size: 22px; line-height: 1; margin: 0; }
.brand p { margin: 4px 0 0; color: var(--muted); font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.search { display: grid; grid-template-columns: 1fr auto auto; gap: 8px; min-width: 0; }
.search input {
  min-width: 0;
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--panel);
  color: var(--ink);
  min-height: 38px;
  padding: 8px 10px;
}
.metrics { display: flex; gap: 6px; align-items: center; white-space: nowrap; }
.pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 26px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: color-mix(in srgb, var(--panel) 82%, transparent);
  padding: 5px 8px;
  color: var(--muted);
  font-size: 12px;
}
.layout { display: grid; grid-template-columns: minmax(540px, 1fr) 390px; min-height: 0; }
.main, .side { min-height: 0; overflow: auto; }
.topicbar {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  align-items: center;
  min-width: 0;
  border-bottom: 1px solid var(--line);
  background: color-mix(in srgb, var(--panel) 72%, transparent);
  padding: 8px 14px;
}
.topic-scroll, .tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: thin;
  min-width: 0;
}
.main { padding: 14px; }
.side {
  border-left: 1px solid var(--line);
  background: color-mix(in srgb, var(--panel) 70%, transparent);
  padding: 12px;
}
.section-title {
  margin: 16px 0 8px;
  color: var(--muted);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.topic-btn {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-align: left;
  background: transparent;
  white-space: nowrap;
}
.topic-btn b { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.topic-btn.active { background: var(--ink); color: var(--bg); }
.note {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px;
  background: var(--panel);
  color: var(--muted);
  font-size: 12px;
}
.insight {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 12px;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: color-mix(in srgb, var(--panel) 86%, transparent);
  padding: 10px;
  margin-bottom: 10px;
}
.insight p { margin: 0; color: var(--muted); font-size: 12px; }
.stat-grid { display: flex; gap: 6px; flex-wrap: wrap; }
.stat { border: 1px solid var(--line); border-radius: 999px; background: color-mix(in srgb, var(--panel) 88%, transparent); padding: 5px 8px; }
.stat b { font: 800 13px/1 var(--mono); margin-right: 4px; }
.stat span { color: var(--muted); font-size: 11px; }
.split { display: grid; grid-template-rows: auto minmax(0, 1fr); gap: 12px; min-height: 0; }
.session-list {
  display: flex;
  overflow-x: auto;
  min-height: 106px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: color-mix(in srgb, var(--panel) 78%, transparent);
}
.session-row {
  flex: 0 0 292px;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  border: 0;
  border-right: 1px solid var(--line);
  border-radius: 0;
  background: transparent;
  text-align: left;
  padding: 10px;
}
.session-row b { display: block; font-size: 13px; line-height: 1.25; }
.session-row span { display: block; margin-top: 4px; color: var(--muted); font-size: 11px; }
.badge {
  align-self: start;
  border-radius: 999px;
  border: 1px solid var(--line);
  padding: 4px 6px;
  color: var(--muted);
  font-size: 11px;
}
.selected {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  overflow: hidden;
}
.selected-head { padding: 14px; border-bottom: 1px solid var(--line); }
.selected-head h3 { margin: 6px 0 8px; font-size: 22px; line-height: 1.1; }
.selected-head p { margin: 0; color: var(--muted); }
.selected-body { padding: 14px; }
.finding-btn, .ask-btn {
  min-height: 26px;
  margin-top: 6px;
  padding: 4px 7px;
  font-size: 11px;
  color: var(--accent);
}
.ask-panel textarea {
  width: 100%;
  min-height: 96px;
  resize: vertical;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--panel);
  color: var(--ink);
  padding: 8px;
}
.ask-actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }
.grid2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
.card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: color-mix(in srgb, var(--panel) 84%, var(--panel-2));
  padding: 11px;
}
.card h4 { margin: 0 0 8px; font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
ul { margin: 0; padding-left: 18px; }
li { margin: 6px 0; line-height: 1.35; }
.tiny { color: var(--muted); font-size: 12px; }
.terms { display: flex; gap: 6px; flex-wrap: wrap; }
.term { border: 1px solid var(--line); border-radius: 999px; padding: 5px 7px; font: 11px/1 var(--mono); color: var(--blue); }
.rollup, .journey, .compare {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  padding: 11px;
  margin-bottom: 10px;
}
.rollup h4, .journey h4, .compare h4 { margin: 0 0 6px; font-size: 14px; }
.side details {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  padding: 10px;
  margin-bottom: 10px;
}
.side summary { cursor: pointer; font-weight: 800; }
.selected details {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: color-mix(in srgb, var(--panel) 84%, var(--panel-2));
  padding: 10px;
  margin-bottom: 10px;
}
.selected summary {
  cursor: pointer;
  font-weight: 800;
  color: var(--ink);
}
.toc {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 10px;
}
.toc a {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 5px 7px;
  font-size: 11px;
  color: var(--muted);
}
@media (max-width: 1100px) {
  html, body { overflow: auto; height: auto; }
  .app { height: auto; min-height: 100vh; }
  .topbar, .layout, .insight, .topicbar { grid-template-columns: 1fr; }
  .side { border: 0; }
  .stat-grid { grid-template-columns: repeat(4, minmax(90px, 1fr)); }
}
@media (max-width: 680px) {
  .topbar { grid-template-columns: 1fr; }
  .search { grid-template-columns: 1fr; }
  .metrics { flex-wrap: wrap; }
  .stat-grid, .grid2 { grid-template-columns: 1fr 1fr; }
  .session-row { flex-basis: 250px; }
}
</style>
</head>
<body>
<div class="app">
  <header class="topbar">
    <div class="brand">
      <h1>WWDC Session Atlas</h1>
      <p id="subtitle">Transcript-derived Apple platform research browser</p>
    </div>
    <div class="search">
      <input id="search" type="search" placeholder="Search videos, APIs, chapters, agent notes, docs">
      <button id="reset">Reset</button>
    </div>
    <button id="theme" aria-label="Toggle color theme">Theme</button>
    <div class="metrics" id="metrics"></div>
  </header>
  <nav class="topicbar">
    <div class="topic-scroll" id="topics"></div>
    <div class="tabs" id="tabs"></div>
  </nav>
  <div class="layout">
    <main class="main">
      <section class="insight">
        <div class="stat-grid" id="stats"></div>
        <p id="heroText"></p>
      </section>
      <section class="split">
        <div class="session-list" id="sessionList"></div>
        <article class="selected" id="selected"></article>
      </section>
    </main>
    <aside class="side">
      <details>
        <summary>Selected Session Agent Context</summary>
        <div id="selectedAgent"></div>
      </details>
      <details>
        <summary>Source Protocol</summary>
        <div class="note" id="policy"></div>
      </details>
      <details>
        <summary>Framework Rollups</summary>
        <div id="rollups"></div>
      </details>
      <details>
        <summary>User Journeys</summary>
        <div id="journeys"></div>
      </details>
      <details>
        <summary>Industry Compare</summary>
        <div id="industry"></div>
      </details>
      <details>
        <summary>Documentation Index</summary>
        <div id="docs"></div>
      </details>
    </aside>
  </div>
</div>
<script>
const atlas = __DATA__;
const state = { topic: "All", tab: "all", selected: null, query: "", finding: "" };
const $ = (id) => document.getElementById(id);
const esc = (s = "") => String(s).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
const displayTitle = (s = "") => String(s).replace(/\b([a-z])/g, ch => ch.toUpperCase()).replace(/\bAi\b/g, "AI").replace(/\bIos\b/g, "iOS").replace(/\bMacos\b/g, "macOS").replace(/\bSwiftui\b/g, "SwiftUI").replace(/\bUikit\b/g, "UIKit").replace(/\bAppkit\b/g, "AppKit").replace(/\bXcode\b/g, "Xcode").replace(/\bWwdc\b/g, "WWDC");
const list = (items) => items && items.length ? `<ul>${items.map(item => `<li>${esc(item)}</li>`).join("")}</ul>` : `<p class="tiny">No derived notes in this phase.</p>`;
const findingList = (items) => items && items.length ? `<ul>${items.map((item, index) => `<li>${esc(item)}<br><button class="finding-btn" data-finding="${index}">Ask about this</button></li>`).join("")}</ul>` : `<p class="tiny">No derived notes in this phase.</p>`;
const linkList = (items) => items && items.length ? `<ul>${items.map(item => `<li><a href="${esc(item.url)}" target="_blank" rel="noreferrer">${esc(item.title)}</a></li>`).join("")}</ul>` : `<p class="tiny">No linked resources on the Apple page.</p>`;
const topicEntries = Object.entries(atlas.topicGroups || {}).sort((a, b) => b[1].length - a[1].length);
const topicNames = ["All", ...topicEntries.map(([name]) => name)];

function applyTheme(mode) {
  if (mode) document.documentElement.dataset.theme = mode;
  if (mode) localStorage.setItem("wwdc-atlas-theme", document.documentElement.dataset.theme || "");
  const current = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  $("theme").textContent = current === "dark" ? "Light" : "Dark";
  $("theme").setAttribute("aria-label", `Switch to ${current === "dark" ? "light" : "dark"} theme`);
}

function sessionHaystack(s) {
  return [
    s.title, s.description, (s.topics || []).join(" "), (s.platforms || []).join(" "),
    (s.highlights || []).join(" "), (s.apiTerms || []).join(" "), (s.capabilityTerms || []).join(" "),
    (s.risksAndConstraints || []).join(" "), (s.agentNotes || []).join(" "), (s.chapterTopics || []).join(" "),
    (s.keywords || []).join(" "), (s.resourceTitles || []).join(" "), (s.resources || []).map(r => `${r.title} ${r.url}`).join(" ")
  ].join(" ").toLowerCase();
}

function filteredSessions() {
  const q = state.query.trim().toLowerCase();
  return atlas.sessions.filter(s => {
    const topicOk = state.topic === "All" || (s.topics || []).includes(state.topic);
    const tabOk = state.tab === "all" || (state.tab === "deep" ? s.analysisStatus === "transcript-derived" : s.year === state.tab);
    const queryOk = !q || sessionHaystack(s).includes(q);
    return topicOk && tabOk && queryOk;
  });
}

function renderShell() {
  const coverage = atlas.meta.coverage;
  $("subtitle").textContent = `${coverage.totalSessionCount} videos indexed - ${coverage.transcriptDerivedCount} transcript-derived analyses`;
  $("metrics").innerHTML = [
    ["WWDC26", coverage.wwdc26SessionCount],
    ["WWDC25 ctx", coverage.wwdc25RelevantSessionCount],
    ["Deep", coverage.transcriptDerivedCount]
  ].map(([label, value]) => `<span class="pill"><b>${value}</b>${label}</span>`).join("");
  $("stats").innerHTML = [
    ["WWDC26 videos", coverage.wwdc26SessionCount],
    ["WWDC25 context", coverage.wwdc25RelevantSessionCount],
    ["Deep analyses", coverage.transcriptDerivedCount],
    ["Topics", topicEntries.length]
  ].map(([label, value]) => `<div class="stat"><b>${value}</b><span>${label}</span></div>`).join("");
  $("heroText").textContent = atlas.meta.transcriptCachingPolicy;
  $("policy").textContent = atlas.meta.transcriptCachingPolicy + " Page HTML and Apple metadata may be cached for reproducible source inventory.";
  $("topics").innerHTML = topicNames.map(name => {
    const count = name === "All" ? atlas.sessions.length : (atlas.topicGroups[name] || []).length;
    return `<button class="topic-btn ${state.topic === name ? "active" : ""}" data-topic="${esc(name)}"><b>${esc(name)}</b><span>${count}</span></button>`;
  }).join("");
  $("topics").querySelectorAll("button").forEach(btn => btn.addEventListener("click", () => {
    state.topic = btn.dataset.topic;
    state.selected = null;
    render();
  }));
  const tabs = [["all", "All"], ["deep", "Deep researched"], ["2026", "WWDC26"], ["2025", "WWDC25 context"]];
  $("tabs").innerHTML = tabs.map(([id, label]) => `<button class="${state.tab === id ? "active" : ""}" data-tab="${id}">${label}</button>`).join("");
  $("tabs").querySelectorAll("button").forEach(btn => btn.addEventListener("click", () => {
    state.tab = btn.dataset.tab;
    state.selected = null;
    state.finding = "";
    render();
  }));
}

function renderSessions() {
  const sessions = filteredSessions();
  if (!state.selected || !sessions.find(s => key(s) === state.selected)) state.selected = sessions[0] ? key(sessions[0]) : null;
  $("sessionList").innerHTML = sessions.length ? sessions.map(s => `
    <button class="session-row ${key(s) === state.selected ? "active" : ""}" data-key="${key(s)}">
      <span><b>${esc(displayTitle(s.title))}</b><span>${esc(topicLine(s))} - ${esc(s.duration || "duration n/a")}</span></span>
      <span class="badge">${s.year}${s.analysisStatus === "transcript-derived" ? " deep" : ""}</span>
    </button>`).join("") : `<div class="note">No sessions match this filter.</div>`;
  $("sessionList").querySelectorAll("button").forEach(btn => btn.addEventListener("click", () => {
    state.selected = btn.dataset.key;
    state.finding = "";
    renderSelected();
  }));
  renderSelected();
}

function topicLine(s) {
  const topics = s.topics || [];
  if (topics.length <= 2) return topics.join(" / ");
  return `${topics.slice(0, 2).join(" / ")} +${topics.length - 2}`;
}

function key(s) { return `${s.year}-${s.id}`; }

function renderSelected() {
  const s = atlas.sessions.find(item => key(item) === state.selected);
  if (!s) {
    $("selected").innerHTML = `<div class="selected-body"><p class="tiny">Select a session.</p></div>`;
    return;
  }
  $("selected").innerHTML = `
    <div class="selected-head">
      <span class="pill">${s.year} - ${esc(s.analysisStatus)}</span>
      <span class="pill">${esc((s.platforms || []).slice(0, 3).join(", ") || "Apple platforms")}</span>
      <h3>${esc(displayTitle(s.title))}</h3>
      <p>${esc(s.description || "No Apple description captured.")}</p>
      <p class="tiny"><a href="${esc(s.url)}" target="_blank" rel="noreferrer">Open Apple video</a>${s.published ? " - Published " + esc(s.published) : ""}</p>
      <div class="toc">
      ${["findings", "risks", "resources", "terms", "chapters"].map(id => `<a href="#${id}">${id}</a>`).join("")}
      <button class="ask-btn" id="askSession">Ask about session</button>
      </div>
    </div>
    <div class="selected-body">
      <details id="findings" open><summary>Important Findings</summary>${findingList(s.highlights)}</details>
      <details id="risks" open><summary>Risks</summary>${list(s.risksAndConstraints)}</details>
      <details id="resources"><summary>Apple Resources</summary>${linkList(s.resources)}</details>
      <details id="terms" open><summary>API / Capability Tags</summary><div class="terms">${[...(s.apiTerms || []), ...(s.capabilityTerms || [])].slice(0, 38).map(term => `<span class="term">${esc(term)}</span>`).join("") || `<span class="tiny">No terms extracted.</span>`}</div></details>
      <details id="chapters"><summary>Chapters</summary>${list(s.chapterTopics || (s.chapters || []).map(c => c.title))}</details>
      <p class="tiny">Transcript characters read ephemerally: ${esc(s.transcriptStats?.charactersReadEphemerally || 0)}. Full transcript characters stored: ${esc(s.transcriptStats?.storedCharacters || 0)}.</p>
    </div>`;
  $("selected").querySelectorAll("[data-finding]").forEach(btn => btn.addEventListener("click", () => {
    state.finding = s.highlights[Number(btn.dataset.finding)] || "";
    renderSide();
  }));
  $("askSession").addEventListener("click", () => {
    state.finding = "";
    renderSide();
    document.querySelector(".side").scrollTo({ top: 0, behavior: "smooth" });
  });
  renderSelectedAgent(s);
}

function renderSide() {
  const selected = atlas.sessions.find(item => key(item) === state.selected);
  renderSelectedAgent(selected);
  $("rollups").innerHTML = atlas.frameworkRollups.map(r => `
    <div class="rollup">
      <h4>${esc(r.title)}</h4>
      <p class="tiny">${r.videoCount} videos - ${r.transcriptDerivedCount} deep analyses</p>
      ${list(r.agentUse)}
      <div class="terms">${(r.topApiTerms || []).slice(0, 12).map(t => `<span class="term">${esc(t)}</span>`).join("")}</div>
    </div>`).join("");
  $("journeys").innerHTML = atlas.userJourneys.map(j => `
    <div class="journey">
      <h4>${esc(j.title)}</h4>
      <p>${esc(j.scenario)}</p>
      <p class="tiny">${esc(j.agentPromptUse)}</p>
      <div class="terms">${j.buildingBlocks.map(t => `<span class="term">${esc(t)}</span>`).join("")}</div>
    </div>`).join("");
  $("industry").innerHTML = atlas.industryComparisons.map(c => `
    <div class="compare">
      <h4>${esc(c.area)}</h4>
      <p>${esc(c.agentUse)}</p>
      ${linkList(c.sources.map((url, i) => ({ title: `Industry source ${i + 1}`, url })))}
    </div>`).join("");
  $("docs").innerHTML = Object.entries(atlas.documentationIndex).map(([name, url]) => `<p><a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(name)}</a></p>`).join("");
}

function renderSelectedAgent(s) {
  if (!s) {
    $("selectedAgent").innerHTML = `<p class="tiny">Select a session.</p>`;
    return;
  }
  $("selectedAgent").innerHTML = `
    <div class="rollup">
      <h4>${esc(displayTitle(s.title))}</h4>
      <p class="tiny">${esc(s.year)} - ${esc(s.analysisStatus)} - ${esc((s.topics || []).join(", "))}</p>
      <h4>Agent Use</h4>
      ${list(s.agentNotes)}
      <h4>Selected Finding</h4>
      <p class="tiny">${esc(state.finding || "No specific finding selected.")}</p>
    </div>`;
}

function render() {
  renderShell();
  renderSessions();
  renderSide();
}

$("search").addEventListener("input", (event) => { state.query = event.target.value; state.selected = null; renderSessions(); });
$("reset").addEventListener("click", () => { state.topic = "All"; state.tab = "all"; state.query = ""; $("search").value = ""; render(); });
$("theme").addEventListener("click", () => {
  const current = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  applyTheme(current === "dark" ? "light" : "dark");
});
const savedTheme = localStorage.getItem("wwdc-atlas-theme");
if (savedTheme) document.documentElement.dataset.theme = savedTheme;
applyTheme("");
render();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    main()
