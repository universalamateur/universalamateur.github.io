---
title: "Building an Air-Gapped Pricing Calculator with Zero Backend"
date: 2026-04-05
draft: false
tags: ["architecture", "air-gapped", "JavaScript", "GitLab Pages"]
summary: "Two static HTML apps deployed to GitLab Pages, no server, no database, handling enterprise pricing workflows where data cannot leave the browser."
showtoc: true
---

Working with customers whose data cannot leave the building, I kept running into the same problem: every deal sizing tool assumes an internet connection. A SaaS spreadsheet, a web app with an API backend, a shared Google Sheet with formulas that phone home for exchange rates. For customers in automotive, defense, and financial services, where [air-gapped](https://en.wikipedia.org/wiki/Air_gap_(networking)) environments are not an edge case but the default operating condition, none of these work. Pricing data is sensitive (deal structure, seat counts, consumption patterns), and the moment you ask a field seller to paste that into a cloud-hosted tool, you have created a compliance conversation that nobody wants to have.

So I built two companion web apps for internal deal sizing, both deployed to [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/), both running entirely in the browser, both requiring exactly zero network calls after the initial page load.

## The Two-Tool Architecture

The first tool, the Field Collector, is what sales reps interact with directly. They upload a customer's [Service Ping](https://docs.gitlab.com/ee/development/internal_analytics/service_ping/) JSON (a structured telemetry payload that describes how an instance is being used) or enter the same data manually when no export is available. The tool validates every input, auto-fills persona breakdowns using a default ratio (31% creators, 16% verifiers, 49% reporters, a split that field sellers can override when they know the customer's actual distribution), and exports a structured [JSON](https://en.wikipedia.org/wiki/JSON) file that captures everything Deal Desk needs to build a quote.

The second tool, the ELA Calculator, takes that export file (or accepts direct input for quick scenarios) and does the actual math: annual pricing, credit consumption broken down by workflow, three pricing paths rendered side by side for comparison, and an ROI overlay that shows the customer what they are getting for their spend. Having worked through enough deal cycles to know that sellers need to show options rather than a single number, the three-path layout was a deliberate design choice from day one.

Both tools are vanilla HTML, CSS, and [JavaScript](https://en.wikipedia.org/wiki/JavaScript). No React, no Vue, no build step, no bundler. The constraint was specific: field sellers run this on any laptop, including customer-provided machines with restricted browsers, locked-down USB policies, and no ability to install anything. The browser is the runtime. The static files served by GitLab Pages are the entire infrastructure.

## One Parser, Two Repos

The Service Ping payload is the shared data contract between both tools. Extracting the right fields from a Service Ping JSON (active user counts, feature usage signals, CI minutes consumed) requires parsing logic that both tools must agree on. Rather than maintaining two copies of the same extraction code, both repos share a `parser.js` module synced via a version constant.

```javascript
// parser.js — shared between Field Collector and ELA Calculator
const PARSER_VERSION = "1.4";

function parseServicePing(payload) {
  const extract = (path, fallback = 0) =>
    path.split(".").reduce((obj, key) =>
      obj && obj[key] !== undefined ? obj[key] : fallback, payload);

  return {
    version: PARSER_VERSION,
    active_users: extract("usage_activity_by_stage.manage.events", 0),
    ci_pipelines: extract("usage_activity_by_stage.verify.ci_pipelines", 0),
    merge_requests: extract("usage_activity_by_stage.create.merge_requests", 0),
    deployments: extract("counts.deployments", 0),
    security_scans: extract("usage_activity_by_stage.secure.user_sast_jobs", 0),
    extracted_at: new Date().toISOString()
  };
}
```

The `PARSER_VERSION` constant is the coordination mechanism. When the extraction logic changes (a new field added, a path updated because the Service Ping schema evolved), the version bumps, and both repos know they need the update. Two repos, one parsing contract, no shared server required.

## The Export Schema as Documentation

Connecting the two tools without a server means the JSON export file is the API. Treating it with the same seriousness as a REST endpoint, I documented the schema in a `FIELD-EXPORT-SCHEMA.md` file (currently at v1.1) that specifies every field, its type, its validation rules, and its default value. When the Field Collector writes a file and the ELA Calculator reads it, both sides validate against the same contract. If a seller manually edits the JSON (which happens), the Calculator catches malformed fields before attempting any math.

This formality around a simple JSON file might seem excessive for an internal tool, but having discovered through experience that "it is just a JSON file" becomes "why does the calculator show NaN" within about two weeks of field use, the schema documentation paid for itself almost immediately.

## Security Without a Server

Deploying to GitLab Pages with [Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) headers means the tools are hardened even in their static form. The CSP rules prevent inline script injection, restrict resource loading to same-origin, and ensure that even if someone bookmarks the page on a shared machine, the tool cannot be tricked into loading external resources. For an air-gapped deployment, where the pages might be saved locally and opened from a file system, the same CSP discipline means the tools behave identically whether served over HTTPS or opened from disk.

No cookies, no local storage persistence (all state lives in the current session and the exported file), no analytics scripts, no font loading from CDNs. After the HTML, CSS, and JS files load, the network connection could be severed entirely and the tools would not notice.

## What This Pattern Teaches

Building for constrained environments, where there is no server, no database, no network after page load, forces a kind of architectural clarity that I found surprisingly liberating. Every feature request gets filtered through a simple question: can this run entirely in the browser? If the answer is no, the feature does not ship. That constraint eliminated entire categories of complexity (user accounts, session management, data synchronization, server provisioning) and left behind two tools that do exactly one thing each, do it well, and cannot leak data because there is nowhere for the data to go.

I found in this constraint a surprising freedom. The air-gapped requirement, which initially felt like a limitation, turned out to be the best architectural decision the project never had to make. It was given to us by the environment, and everything good about the design flows from accepting it rather than working around it.

For anyone building internal tools in regulated environments, the pattern is worth considering: static files, client-side processing, documented export schemas, and the browser as your only runtime. The infrastructure cost is a GitLab repo with Pages enabled. The maintenance burden is close to zero. And the compliance story writes itself, because the data never leaves the machine it was entered on.
