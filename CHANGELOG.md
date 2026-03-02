# Changelog

All significant changes to the Generals system. Reverse-chronological order.

---

## [2026-03-02] — XP Keeper Cache + Operation Parallel Pipeline

### Added
- **XP Keeper Cache System** (`bin/generate-roster-cache.py`) — Python script that reads all `profiles/service-records/*.yaml` files and generates `~/.claude/generals-roster-cache.json`. Eliminates need for Field Marshal to scan Markdown tables at spawn time.
- **`bin/generate-roster-cache.sh`** — Bash wrapper for the Python cache generator. Called by `~/.claude/refresh-generals-cache.sh` at session start.
- **`~/.claude/refresh-generals-cache.sh`** — Standalone refresh script for session-start hooks.
- **`profiles/service-records/eisenhower.yaml`** — Full service record for Operation Parallel Pipeline campaign: 550 XP, 4 deployments, Commendation Medal.
- **`profiles/service-records/bradley.yaml`** — Full service record: 350 XP, 3 deployments, ThreadPoolExecutor zero-regression integration.
- **`profiles/service-records/nimitz.yaml`** — Updated service record: 325 XP, 3 deployments, 12/12 tests for `bin/run-tier1-parallel.sh`.
- **`SERVICE-RECORD-OPERATION-PARALLEL-PIPELINE-2026-03-02.md`** — Campaign service record for clearwatch parallelization work.

### Changed
- New spawn pattern: Field Marshal reads JSON cache instead of COMMAND-ROSTER.md table for XP data.
- `clearwatch/CLAUDE.md` Commander Roster table replaced with cache-read reference (lean context).

### XP Updates (from service-record YAMLs)
- Eisenhower: 50 XP → 550 XP (4 deployments, campaign coordinator)
- Bradley: 75 XP → 350 XP (3 deployments, concurrent code specialist)
- Nimitz: 175 XP → 325 XP (3 deployments, parallel runner)
- Spruance: 225 XP → 525 XP (5 deployments, verified through multiple campaigns)

---

## [2026-02-26] — Operation Build-60 + Operation Warroom Viz

### Added
- **`profiles/service-records/spruance.yaml`** — Spruance service record updated for Operation Warroom Viz and Build-60 (5 SVGs: mitre_coverage_rebuke, independent_test_score_timeline, vendor_claim_vs_reality, detection_confidence_intervals, cost_per_true_positive).
- **`SERVICE-RECORD-OPERATION-WARROOM-VIZ-2026-02-26.md`** — Campaign service record.
- **`profiles/service-records/` entries** for Operation Build-60: 60 SVGs delivered in single campaign.
- `profiles/service-records/2026-02-26-operation-build-60.md` — Aggregate campaign record.
- `profiles/service-records/2026-02-26-operation-warroom-viz.md` — Campaign record for visualization sprint.

---

## [2026-02-23 / 2026-02-24] — Self-Learning Redesign + Journalist Profiles

### Added
- **Journalist profiles** — Hemingway, Heller, Murrow, Gellhorn, Higgins, Orwell, Pyle, Cronkite added to `profiles/`. Each includes voice samples and scoring methodology.
- **`profiles/hemingway.md`** and **`profiles/heller.md`** — Full voice profiles with writing samples.
- **`SERVICE-RECORD-SELF-LEARNING-REDESIGN-20260224.md`** — Campaign service record for system redesign.

### Changed
- **Skills updated** — GitHub as authoritative source of truth. Skills now explicitly prioritize underutilized commanders to balance deployment distribution.
- Campaign service record documents the self-learning system redesign pattern (AGENTS.md restructured, skills slimmed).

---

## [2026-02-22] — Security Fix

### Security
- **`security: replace hardcoded Cloudflare token`** — Replaced literal `${CF_TOKEN}` value with environment variable placeholder across skills and deployment templates.

---

## [2026-02-17] — Historical Accuracy Phase 2 (Thorough Standard Research)

### Added / Changed (Phase 2 Historical Audit)
This batch applied the "thorough standard" research methodology (Tier 1 primary sources + Tier 2 modern scholarship) to multiple commanders:

- **Montgomery** (`profiles/montgomery.md`) — Phase 2 upgrade complete. Clean Wehrmacht myth equivalent removed. Modern scholarship verified. Accuracy: 90/100.
- **LeMay** (`profiles/lemay.md`) — Phase 2 upgrade complete. Firebombing doctrine documented accurately. Accuracy: 88/100.
- **Harris** (`profiles/harris.md`) — Mission brief and Phase 2 research complete. Area bombing doctrine and Dresden documented.
- **Rommel** (`profiles/rommel.md`) — Phase 2 upgrade complete. "Desert Fox" mythology deconstructed. Clean Wehrmacht myth removed. Accuracy: 85-90/100.
- **Patton** (`profiles/patton.md`) — Phase 2 upgrade complete. Self-mythology patterns documented. Accuracy: 90/100.
- **Gellhorn analysis documents** — Four investigative analyses applied Gellhorn's BS-detection voice to Rommel, Patton, Harris area bombing propaganda, and LeMay strategic bombing doctrine.
- **Orwell analysis documents** — Orwell doctrine and ideology analyses applied to Harris (area bombing propaganda) and LeMay (strategic bombing doctrine).

### Architectural Note
Phase 2 research introduced a three-stage mythology framework for profiling controversial commanders:
1. Identify the mythology
2. Document the counter-evidence (primary sources)
3. Preserve the genuine contribution

---

## [2026-02-14 to 2026-02-16] — 14-Variant Stripe Deployment + Admiral Profile Expansion

### Added
- **`SERVICE-RECORD-14-VARIANT-STRIPE-DEPLOYMENT-2026-02-14.md`** — Campaign record for 14-variant business website deployment (42 pages, 17,000+ lines).
- **`SERVICE-RECORD-ADMIRAL-PROFILES-2026-02-10.md`** — Service record for Admiral profile build sprint.
- **`SERVICE-RECORD-AIR-POWER-VERIFICATION-2026-02-10.md`** — Air power doctrine verification results.
- **`SERVICE-RECORD-COMPREHENSIVE-VERIFICATION-2026-02-10.md`** — Comprehensive verification campaign record.
- **`SERVICE-RECORD-MILITARY-LEADERS-WAVE-2-2026-02-10.md`** — Wave 2 commander profile builds.
- **Dowding profile** (`profiles/dowding.md`) — Comprehensive primary sources methodology test. Accuracy: 88-92/100. Integrated Defense Architecture specialist.
- Service records for: `dowding.yaml`, `layton.yaml`, `mitchell.yaml`, `lemay.yaml`, `macarthur.yaml`, `slim.yaml`.

### Campaign Notes
- Operation Multi-Variant Deployment (2026-02-09): 14 parallel fronts, 24 commanders, Montgomery as supreme command.
- **HALT/RESUME coordination lesson** documented — methodical commanders (Spruance) held position 10 hours awaiting explicit RESUME; lesson now encoded in Montgomery's profile.

---

## [2026-02-11] — Complete Visual Roster + Journalist Voice Processing

### Added
- **`profiles/service-records/2026-02-11-operation-complete-visual-roster.md`** — Service record for visual roster build.
- **`SERVICE-RECORD-JOURNALIST-VOICE-PROCESSING-2026-02-11.md`** — Journalist voice consistency testing.
- **`SERVICE-RECORD-MODERN-SCHOLARSHIP-RESEARCH-2026-02-11.md`** — Modern scholarship research methodology.
- **`OPERATION-UX-TRANSFORMATION-2026-02-11.md`** — UX transformation operation notes.
- Service records for: `montgomery.yaml`, `spruance.yaml`, `zhukov.yaml`, `king.yaml`, `halsey.yaml`, `pyle.yaml`, `orwell.yaml`, `ogilvy.yaml`.

---

## [2026-02-07 to 2026-02-09] — Foundation Campaigns (System Origin)

### Added
- **Operation Stunning Charts** (2026-02-07) — First major multi-commander campaign.
  - 10 commanders, 14 inline SVG charts, 45-page security intelligence report.
  - Montgomery earned Order of Victory (highest honor in system).
  - King earned Medal of Honor (AI SIEM Readiness Radar).
  - Spruance earned Medal of Honor (Storage Cost Explosion with confidence bands).
- **ClearWatch Campaign** (2026-02-07) — Multi-version K8s deployment.
  - 15 Kubernetes manifests created with organizational excellence.
  - Nimitz earned ClearWatch Campaign ribbon.
- **Operation Quality Baseline** (2026-02-08) — Rickover established quality control architecture.
  - 925 XP in single campaign (highest single-deployment XP in system history).
  - Built systematic measurement pipeline with regression prevention.
- **Operation Pipeline Unblock** (2026-02-08) — Hopper debugged CLI pipeline failure.
  - "Forgiveness > permission" — bypassed committee approach, fixed directly.
  - Earned Commendation Medal.
- **Operation Multi-Variant Deployment** (2026-02-09) — 14 parallel business website variants.
  - 42/42 pages, ~17,000 lines of code, 100% quality gates.
  - First deployment of HALT/RESUME coordination protocol (failure documented, lesson captured).
- **`SERVICE-RECORD-OPERATION-MULTI-VARIANT-DEPLOYMENT.md`** — Foundation campaign record.

### Initial Profiles Created
- Core commanders: eisenhower, bradley, nimitz, spruance, montgomery, halsey, king, patton, rommel, hopper, rickover, marshall, macarthur, slim.
- Specialists: gordon-ramsay, ciso-validator, ernie-pyle.
- Extended roster: Multiple additional profiles (see `profiles/` directory).

### Architecture Established
- XP system with task-type base values (Research: 50, Visualization: 75, Integration: 100, Coordination: 150, Troubleshooting: 200).
- Competence stars (10/25/50/100/250 deployments per category).
- Campaign ribbons and medal hierarchy (Commendation → DSM → Medal of Honor → Order of Victory).
- Fork-based learning model (local by default, optional PR contribution).
- Sanitization protocol (no IPs/hostnames/tokens in committed service records).
- Civilian-Military Autonomy Doctrine established in PHILOSOPHY.md.

---

## [Unreleased]

- Profile stubs added for missing high-priority commanders: `nimitz.md`, `spruance.md`, `montgomery.md`, `king.md`, `zhukov.md`.
- COMMAND-ROSTER.md XP values updated to reflect current service-record YAML data.
- README.md: Added XP Keeper Cache System section with usage reference.
- CHANGELOG.md created (this file).
