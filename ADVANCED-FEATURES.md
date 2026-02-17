# Advanced Features

Deep dive into Generals' sophisticated features for power users.

---

## Table of Contents

1. [Memory System](#memory-system)
2. [Social Media Documentation](#social-media-documentation)
3. [Role Selection Framework](#role-selection-framework)
4. [Multi-Variable Testing](#multi-variable-testing)
5. [Sanitization Protocol](#sanitization-protocol)
6. [Context Management](#context-management)
7. [Campaign Coordination Patterns](#campaign-coordination-patterns)

---

## Memory System

Generals includes a tiered memory architecture that keeps context lean while preserving cross-session learning.

### The Problem

**Context window bloat kills performance.** If you load every lesson from every deployment into every spawn prompt, you'll hit token limits fast. But if you load nothing, commanders can't learn.

**Solution:** Tiered loading with smart retrieval.

### Memory Architecture

```
generals/memory/
├── CAMPAIGN_SUMMARY.md          (~200 lines, ALWAYS LOADED)
├── officer-knowledge/            (loaded ON-DEMAND when commander spawned)
│   ├── patton.md
│   ├── nimitz.md
│   ├── spruance.md
│   └── [general-name].md
└── deployments/                  (NEVER loaded, reference only)
    ├── 2026-02-07-operation-stunning-charts.md
    ├── 2026-02-08-quality-baseline.md
    └── [deployment-logs].md
```

### Tier 1: Campaign Summary (Always Loaded)

**File:** `memory/CAMPAIGN_SUMMARY.md`
**Size:** ~200 lines
**Loaded:** Every Claude Code session

**Contains:**

1. **Last 5 Problems Solved** — Recent high-level context
   ```markdown
   1. Embedded 14 charts in security report (Operation Stunning Charts)
   2. Built quality measurement pipeline (Operation Quality Baseline)
   3. Fixed CLI pipeline crash (Hopper emergency deployment)
   ```

2. **Officer Deployment Stats (Last 30 Days)**
   ```markdown
   Montgomery: 3 deployments, 725 XP, 100% success rate
   Nimitz: 5 deployments, 450 XP, 80% success rate (1 partial)
   Spruance: 4 deployments, 550 XP, 100% success rate
   ```

3. **Active Patterns** — What's working now
   ```markdown
   • Multi-axis radar charts earning user praise
   • Confidence bands on cost projections valued by CISOs
   • Inline SVG embedding preventing image hosting issues
   ```

4. **Critical Lessons (Top 10)** — Universal knowledge all commanders need
   ```markdown
   • Gartner URLs return 403 errors (use Wayback Machine)
   • Chart IDs must be namespaced to prevent SVG conflicts
   • CISO personas prioritize decision utility over technical depth
   ```

**Purpose:** Provides high-level situational awareness without drowning in detail.

### Tier 2: Officer Knowledge (On-Demand)

**Files:** `memory/officer-knowledge/{general-name}.md`
**Loaded:** Only when that specific commander is spawned

**Contains:**

1. **Technical Lessons Learned**
   ```markdown
   ### Chart Generation
   - SVG namespace IDs with `chart-[type]-` prefix (prevents conflicts)
   - Wrap in `<div style="page-break-inside: avoid;">` for PDF rendering
   - Dark theme: navy #0F172A, gold #D4A574, cream #f8fafc
   ```

2. **Behavioral Observations**
   ```markdown
   ### Coordination Under Pressure
   - Montgomery coordinates best with phased deployment (not all-at-once spawning)
   - Delegates clearly but checks progress every 30 minutes
   - "Commander's intent" style briefings reduce confusion
   ```

3. **Success/Failure Patterns**
   ```markdown
   ### What Works
   - Spruance's cost analysis with confidence bands (Medal of Honor earned)
   - Montgomery's 10-commander coordination (Order of Victory)

   ### What Doesn't Work
   - Patton rushing through validation (broke staging deployment)
   - Halsey's aggressive chart embedding (caused SVG conflicts)
   ```

**Purpose:** Commander-specific deep knowledge that's relevant only when that officer deploys.

### Tier 3: Deployment Logs (Reference Only)

**Files:** `memory/deployments/[operation-name].md`
**Loaded:** NEVER (too large, too detailed)

**Contains:**

- Full mission logs with timestamps
- Detailed technical commands executed
- Multi-page coordination transcripts
- Post-mission analysis

**Purpose:** Historical record for service record generation and manual review. Not for context loading.

### How It Works in Practice

**Example: Spawning Admiral Spruance**

```markdown
1. Load CAMPAIGN_SUMMARY.md (~200 lines)
   → Claude gets: Recent problems, active patterns, critical lessons

2. Load officer-knowledge/spruance.md (~150 lines)
   → Claude gets: Spruance's specific technical lessons, behavioral traits

3. Spawn Spruance with combined context (~350 lines total)
   → Lean enough for context window
   → Rich enough for informed decisions

4. Spruance completes mission

5. Update officer-knowledge/spruance.md with new lessons
   → Next spawn automatically includes today's learning
```

**Result:** Context stays under 500 lines while knowledge accumulates indefinitely.

---

## Social Media Documentation

Generals can automatically document campaigns for LinkedIn using historical war correspondents as journalists.

### Why War Correspondents?

**Technical documentation is boring.** "Deployed 14 charts to report generation pipeline" doesn't engage an audience.

**War correspondents know how to make operational work compelling:**

- Ernie Pyle wrote about the ground-level human experience
- Edward R. Murrow framed events with architectural authority
- George Orwell diagnosed systemic dysfunction with cutting clarity

**These voices make AI operations interesting to broader audiences.**

### The 6 Journalists

| Journalist | Voice Score | Style | Best For |
|------------|-------------|-------|----------|
| **Ernie Pyle** | 91/100 | Ground-level, human-interest, meticulous simplicity | Making tech operations accessible through individual narratives |
| **Edward R. Murrow** | 88/100 | Formal witness authority, architectural logic | Executive thought leadership, strategic trend analysis |
| **George Orwell** | 98/100 | Self-incriminating honesty, systemic diagnosis | Exposing dysfunction in tech/AI systems |
| **Martha Gellhorn** | 94/100 | Cutting through BS, first-person truth-telling | Vendor critique, authenticity over polish |
| **Walter Cronkite** | 88/100 | Authoritative industry commentary, measured analysis | Formal announcements, trusted perspective |
| **Marguerite Higgins** | 90/100 | Rapid deployment stories, proving doubters wrong | Breaking barriers, unconventional approaches |

**Voice Score:** Consistency metric (91/100 = 91% match to historical writing patterns across multiple samples)

### Directory Structure

```
social/linkedin/
├── TEMPLATE-DAY.md              (Template for daily posts)
├── day001/
│   ├── post.md                  (1000-1500 chars, journalist voice)
│   └── illustration.svg         (verified, error-free)
├── day002/
│   ├── post.md
│   └── illustration.svg
└── dayNNN/
    ├── post.md
    └── illustration.svg
```

### Post Format

**Every LinkedIn post follows this structure:**

```markdown
# Day [N]: [Headline]

[Hook - 1 sentence capturing attention]

[Body - 3-5 paragraphs building narrative]

[Insight - 1-2 sentences with takeaway]

—
[Journalist Name], War Correspondent AI
```

**Character limit:** 1000-1500 characters (LinkedIn optimal length)

### Voice Consistency

**Each journalist maintains voice across all posts:**

**Ernie Pyle (Ground-Level Narrative):**
```markdown
Admiral Spruance sat at his terminal at 0400, triple-checking the cost
projection model. He wasn't showing off. He just knew that if those
confidence bands were off by even 10%, some CISO in Cleveland would make
the wrong vendor decision based on his work.

That's the thing about the quiet ones. They don't trust luck.
```

**Edward R. Murrow (Architectural Authority):**
```markdown
What we witnessed this week was not merely a technical achievement. It was
a demonstration of coordinated intelligence at scale — 10 commanders, 14
distinct visualizations, zero conflicts. The architecture held because the
design anticipated failure modes before they materialized.

Good night, and good luck.
```

**George Orwell (Systemic Critique):**
```markdown
The vendor landscape operates on a simple principle: if the comparison
chart doesn't exist, the buyer can't make an informed choice. And if the
buyer can't make an informed choice, they default to the biggest name.

This is not an accident. This is the business model.
```

### Signature Requirements (CRITICAL)

**ALL LinkedIn posts MUST end with journalist attribution:**

```markdown
—
Ernie Pyle, War Correspondent AI
```

**Why this matters:**

1. **Transparency** — Readers know it's AI-generated content
2. **Honoring legacy** — Respects the journalist's historical work
3. **Professional ethics** — No deception about authorship
4. **Voice consistency** — Attribution reinforces the journalist persona

**See:** `journalists/SIGNATURE-REQUIREMENTS.md` for complete guidelines.

### Generating LinkedIn Content

**Workflow:**

1. Complete a significant campaign (Operation Stunning Charts, etc.)
2. Choose journalist based on audience/tone
3. Generate day-by-day narrative arc
4. Create accompanying illustrations (SVG, error-free)
5. Commit to `social/linkedin/dayNNN/`

**Example:**

```bash
/generals:document-campaign "Operation Stunning Charts" --journalist="ernie-pyle" --days=5
```

**Output:**

```
social/linkedin/
├── day001/
│   ├── post.md         "The 14-Chart Challenge"
│   └── illustration.svg
├── day002/
│   ├── post.md         "Montgomery's Coordination Test"
│   └── illustration.svg
├── day003/
│   ├── post.md         "The Quiet Warrior's Cost Model"
│   └── illustration.svg
├── day004/
│   ├── post.md         "When Ramsay Says 'IT'S RAW'"
│   └── illustration.svg
└── day005/
    ├── post.md         "The Order of Victory"
    └── illustration.svg
```

**Each post maintains Ernie Pyle's ground-level narrative voice across the 5-day arc.**

---

## Role Selection Framework

Matching the right commander to the right task is critical. Here's the systematic framework.

### By Task Type

| Task Type | Best Fit | Why |
|-----------|----------|-----|
| **Strategic Planning** | Eisenhower, Bradley, Marshall | Coalition building, systems design |
| **Crisis Response** | Patton, MacArthur, Halsey | Aggressive execution, no committees |
| **Technical Deep-Dive** | Hopper, Rickover, Groves | Domain expertise, quality obsession |
| **Routine Operations** | Junior officers | Development opportunity, low stakes |
| **Unknown Territory** | Mitchell, Halsey, LeMay | Experimental mindset, challenge assumptions |

### By Importance Level

**High-Importance Signals** (use ONLY best generals):

- User language: "CRITICAL", "URGENT", "PRODUCTION DOWN", "CUSTOMER WAITING"
- Emotional cues: "This is driving me crazy", "Tried everything"
- Timeline pressure: Hard deadlines, SLA violations
- Repeated failures: Same error 3+ times

**Example:**

```
User: "The authentication service has been down for 45 minutes and the
       customer is on the phone. I'm losing my mind."

→ Deploy Patton (aggressive crisis response)
→ Skip junior officers (too important)
→ Montgomery coordinates if multiple services affected
```

**Low-Stakes Signals** (good for rotation/junior officers):

- User language: "When you get a chance", "No rush", "Curious about"
- Exploratory work: "What if we tried...", research tasks
- Learning opportunities: Refactoring, documentation, test coverage

**Example:**

```
User: "When you have time, can we refactor the chart generation code?"

→ Good opportunity for junior officer development
→ Low risk if approach isn't optimal
→ Feedback loop for learning
```

### By Problem Stubbornness

**Stubborn Problem Signals** (rotate or multi-approach):

- "Stuck on this for hours"
- "Tried X, Y, Z — nothing works"
- Same error message 3+ times
- Multiple failed debugging attempts

**Strategy:** Deploy different personalities to test approaches

```
Problem: K8s networking issue, 2 hours stuck

Experiment 1: Patton (aggressive)
  → Try increasing resource limits, force pod restart

Experiment 2: Nimitz (systematic)
  → Methodically check DNS, network policies, service endpoints

Experiment 3: Hopper (innovative)
  → "Have we considered the CNI plugin might be outdated?"

→ First to succeed teaches lesson
→ Document which approach worked + why
```

### Multi-Commander Coordination

**When to use campaigns (2+ commanders):**

1. **Multiple skill domains required**
   - Example: Research + Analysis + Visualization
   - Deploy: Nimitz (research), Spruance (analysis), King (visuals)

2. **Quality gates needed**
   - Example: Technical work + presentation standards
   - Deploy: Hopper (technical), Ramsay (quality gate)

3. **Coordination complexity**
   - Example: 5+ commanders working in parallel
   - Deploy: Montgomery as supreme commander

**When to use single commander:**

1. **Single skill domain**
   - Example: "Fix authentication bug"
   - Deploy: Slim (disaster recovery)

2. **Speed matters more than perfection**
   - Example: Emergency hotfix
   - Deploy: Patton (aggressive execution)

3. **Exploratory/uncertain scope**
   - Example: "Investigate this weird log error"
   - Deploy: Nimitz (systematic investigation)

---

## Multi-Variable Testing

When problems get stubborn (>30 minutes stuck), deploy experimental problem-solving.

### The Pattern

**Standard debugging (linear):**

```
Try fix A → doesn't work
Try fix B → doesn't work
Try fix C → doesn't work
[3 hours wasted]
```

**Multi-variable testing (parallel):**

```
Hypothesis: 3 possible causes (network, DNS, resource limits)

Experiment A: Patton tests resource increase
Experiment B: Nimitz tests DNS debugging
Experiment C: Hopper tests network policy

→ All 3 run in parallel
→ First to succeed teaches lesson
→ 30 minutes vs. 3 hours
```

### The 5-Step Protocol

**1. Identify Variable Space**

What could be causing this problem?

```markdown
Problem: Service won't start

Possible causes:
- Network policy blocking traffic
- DNS resolution failure
- Resource limits too low
- Image pull authentication failure
- Config map missing required values
```

**2. Propose Experiments**

Test each variable in isolation.

```markdown
Experiment A: Test network policy
  → Deploy test pod in same namespace
  → Attempt connection to service
  → Check network policy rules

Experiment B: Test DNS
  → nslookup from within cluster
  → Check CoreDNS logs
  → Verify service exists

Experiment C: Test resource limits
  → Increase CPU/memory requests
  → Check OOMKilled status
  → Review kubelet logs
```

**3. Deploy Different Generals**

Match personalities to experiment types.

```markdown
Experiment A (Network) → Nimitz (systematic investigation)
Experiment B (DNS) → Hopper (technical debugging)
Experiment C (Resources) → Patton (aggressive resource increase)
```

**4. Define Success Criteria**

How do we know what worked?

```markdown
Success = Service responds to HTTP health check on port 8080
```

**5. Document Results**

Which approach won? Why?

```markdown
Result: Experiment B (DNS) succeeded

Root cause: Service name had typo in deployment manifest
Winner: Admiral Hopper (noticed typo in logs)
Lesson: Always verify service name matches selector labels

Updated profiles:
  - Hopper +200 XP (troubleshooting)
  - Lesson added to officer-knowledge/hopper.md
```

### When To Use Multi-Variable Testing

**Use when:**

- Stuck for >30 minutes on same problem
- Multiple possible causes
- Standard debugging approaches failing
- Time pressure (need answer fast)

**Don't use when:**

- Problem obvious (single clear cause)
- Already tried multiple approaches sequentially
- Low stakes (learning opportunity, not crisis)

---

## Sanitization Protocol (CRITICAL)

Before committing service records to GitHub, **ALL private details are stripped.**

### The Principle

**Enemy is listening everywhere. Share knowledge, not secrets.**

Your fork is private by default, but:
- You might make it public later
- You might submit a PR to origin
- GitHub repos can leak through misconfiguration
- Sanitization is insurance

**Rule:** If you wouldn't post it on LinkedIn, don't commit it to git.

### Include (Safe)

✓ **Technical lessons**
```markdown
Lesson: Check pod logs before assuming network issue
```

✓ **Architecture patterns**
```markdown
Pattern: Use sidecar containers for TLS termination
```

✓ **Debugging approaches**
```markdown
Approach: nslookup from within cluster revealed DNS failure
```

✓ **Personality traits**
```markdown
Observation: Patton moved too fast and skipped validation step
```

✓ **Success/failure patterns**
```markdown
Success: Rolling deploys safer than big-bang for production
```

### Remove (Dangerous)

✗ **IP addresses**
```markdown
# BAD
Fixed service at 192.168.0.131

# GOOD
Fixed K8s service networking issue
```

✗ **Hostnames**
```markdown
# BAD
Deployed to pve.petersimmons.com

# GOOD
Deployed to Proxmox infrastructure
```

✗ **Internal URLs**
```markdown
# BAD
https://registry.petersimmons.com/library/app:latest

# GOOD
Pulled image from internal container registry
```

✗ **API keys**
```markdown
# BAD
Used Cloudflare token: ${CF_TOKEN}

# GOOD
Authenticated to DNS provider API
```

✗ **Customer names**
```markdown
# BAD
Generated CrowdStrike vs SentinelOne report for Acme Corp

# GOOD
Generated competitive security intelligence report
```

✗ **Infrastructure specifics**
```markdown
# BAD
9-node K8s cluster (3 control plane, 6 workers), 192.168.0.131-139

# GOOD
Multi-node K8s cluster with HA control plane
```

### Sanitization Workflow

**Before committing service records:**

1. Read profile Markdown file
2. Search for patterns: IP addresses, domains, tokens, customer names
3. Replace with generic equivalents
4. Verify: Would I post this publicly on LinkedIn?
5. If yes → commit. If no → sanitize more.

**Example:**

```bash
# Review before commit
git diff profiles/patton.md

# If you see private details:
# Edit manually to remove IPs/hostnames/tokens

# Then commit
git add profiles/patton.md
git commit -m "Service record: K8s emergency deployment (sanitized)"
```

---

## Context Management

Keeping context lean while preserving learning is critical for performance.

### The Context Budget

**Claude Code context window:** ~200,000 tokens
**Optimal usage:** <20% for background (leaves 80% for active work)

**Budget allocation:**

| Item | Lines | Tokens (est) | Purpose |
|------|-------|-------------|----------|
| CAMPAIGN_SUMMARY.md | 200 | ~1,000 | High-level situational awareness |
| Commander profile | 150 | ~750 | Personality + accumulated lessons |
| Officer knowledge | 150 | ~750 | Commander-specific deep knowledge |
| **Total** | **500** | **~2,500** | **~1.25% of context window** |

**Result:** Lean context that fits easily while preserving rich learning.

### What NOT To Load

**Never load into context:**

1. **Full deployment logs** — Too large (1000+ lines per deployment)
2. **All commander profiles** — Only load the deployed commander
3. **All officer knowledge** — Only load knowledge for active commander
4. **Historical campaigns** — Reference only, not for active context

**Why:** Context bloat kills performance. Load only what's needed for the current mission.

### Dynamic Loading Pattern

**On spawn:**

```
1. Always load: CAMPAIGN_SUMMARY.md (200 lines)
2. Load for specific commander: profiles/{general}.md (150 lines)
3. Load for specific commander: officer-knowledge/{general}.md (150 lines)
4. Total: ~500 lines, ~2,500 tokens
```

**After mission:**

```
1. Update officer-knowledge/{general}.md with new lessons
2. Update CAMPAIGN_SUMMARY.md if mission was significant
3. Write detailed log to deployments/ (NOT loaded in future)
4. Commit updates to git
```

**Next spawn of same commander:**

```
1. Load updated officer-knowledge (now includes today's lesson)
2. Commander is automatically smarter
3. Context size unchanged (lesson replaces old content or appends)
```

### Garbage Collection

**When officer-knowledge files grow too large (>300 lines):**

1. Identify least-used lessons (no references in recent deployments)
2. Move to deployments/ archive (reference only)
3. Keep only top 20 most-valuable lessons in officer-knowledge
4. Context stays lean, historical record preserved

**Example:**

```markdown
# officer-knowledge/nimitz.md growing to 400 lines

ACTION:
  - Keep top 20 lessons (most referenced/recent)
  - Move older lessons to deployments/nimitz-archive-2026-Q1.md
  - officer-knowledge/nimitz.md back to ~150 lines
  - Context lean, history preserved
```

---

## Campaign Coordination Patterns

Multi-commander campaigns require coordination protocols.

### Campaign Types

**Type A: Parallel Execution (No Dependencies)**

```
Mission: Generate security report

Forces:
├── Nimitz (Research) — No dependencies, start immediately
├── Spruance (Analysis) — No dependencies, start immediately
└── King (Visuals) — No dependencies, start immediately

Coordination: None needed (all work independently)
Quality Gate: Gordon Ramsay reviews final output
```

**Type B: Sequential Execution (Dependencies)**

```
Mission: Deploy new service to production

Forces:
├── Step 1: Hopper (Write code) → must complete first
├── Step 2: Spruance (Test/validate) → depends on Step 1
└── Step 3: Patton (Deploy) → depends on Step 2

Coordination: Each step gates the next
Quality Gate: Rickover verifies no regressions
```

**Type C: Hybrid (Parallel + Sequential)**

```
Mission: Complex security report with coordination

Forces:
├── Phase 1 (Parallel):
│   ├── Nimitz (Research source A)
│   ├── Bradley (Research source B)
│   └── Halsey (Research source C)
├── Phase 2 (Sequential): Spruance (Synthesize research) → depends on Phase 1
├── Phase 3 (Parallel):
│   ├── King (Charts)
│   └── Zhukov (Diagrams)
└── Phase 4 (Sequential): Montgomery (Final coordination) → depends on Phase 3

Coordination: Montgomery as supreme commander
Quality Gate: Ramsay + CISO Validator
```

### Coordination Protocols

**Montgomery as Supreme Commander:**

When campaign involves 5+ commanders, deploy Montgomery to coordinate.

**His responsibilities:**

1. **Force assignment** — Which commander does what
2. **Phased deployment** — Spawn in logical order (not all-at-once)
3. **Progress tracking** — Check in every 30 minutes
4. **Blocker resolution** — Identify stuck commanders, reallocate
5. **Quality gate** — Final review before delivery

**Communication pattern:**

```
Montgomery → Nimitz: "Begin intelligence gathering on vendor A"
Nimitz → Montgomery: "Research complete, 15 sources synthesized"
Montgomery → Spruance: "Intelligence ready, begin analysis"
Spruance → Montgomery: "Analysis complete, cost model ready"
Montgomery → King: "Data ready, generate charts"
...
```

**Checkpoint protocol:**

```
Every 30 minutes, Montgomery broadcasts:
  "Status check. Report progress or blockers."

Commanders respond:
  - Nimitz: "Research 80% complete, no blockers"
  - Spruance: "Analysis complete, awaiting chart data"
  - King: "Blocker: SVG namespace conflict"

Montgomery addresses blocker:
  "King, use chart-[type]- prefix for IDs. Resume when resolved."
```

### Quality Gates

**Single-stage gate:**

```
Deployment completes → Gordon Ramsay reviews → Pass/fail
```

**Multi-stage gate:**

```
Phase 1 completes → Technical review (Rickover)
Phase 2 completes → Content review (CISO Validator)
Phase 3 completes → Presentation review (Ramsay)
```

**Gate criteria:**

```markdown
Technical Gate (Rickover):
  ✓ All tests pass
  ✓ No regressions
  ✓ Code quality standards met

Content Gate (CISO Validator):
  ✓ Decision utility > 7/10
  ✓ "$500 test" passed (would CISO pay?)
  ✓ Actionable recommendations

Presentation Gate (Ramsay):
  ✓ Charts render correctly
  ✓ Typography consistent
  ✓ No formatting errors
```

---

## Skill Reference

The 4 core skills are documented separately in [`SKILLS.md`](SKILLS.md), but here's a quick overview of advanced usage.

### Advanced: Custom Spawn Prompts

**Standard spawn:**

```bash
/generals:spawn-commander patton "Deploy hotfix to production"
```

**Custom spawn with constraints:**

```bash
/generals:spawn-commander patton "Deploy hotfix to production" \
  --constraints="No downtime, rollback plan required, verify in staging first" \
  --success-criteria="Service responds on port 8080 with HTTP 200"
```

**Custom spawn with historical parallel:**

```bash
/generals:spawn-commander patton "Deploy hotfix to production" \
  --parallel="Third Army's rapid advance across France (similar: speed + coordination + logistics)"
```

### Advanced: XP Calculation

**Manual XP award:**

```bash
/generals:award-experience patton 200 \
  "Emergency deployment completed successfully. Lesson: Always verify staging first."
```

**Automated XP calculation:**

```bash
/generals:award-experience patton --auto \
  --task-type="troubleshooting" \
  --complexity="high" \
  --outcome="success" \
  --bonus="User praised speed"
```

**Calculation logic:**

```
Base XP by task type:
  - Research: 50 XP
  - Visualization: 75 XP
  - Integration: 100 XP
  - Coordination: 150 XP
  - Troubleshooting: 200 XP

Multipliers:
  - Complexity: low (0.5x), medium (1x), high (1.5x)
  - Outcome: failure (0.5x), partial (0.75x), success (1x)
  - Bonus: user praise (+50 XP), exceptional performance (+100 XP)
```

---

## Conclusion

These advanced features unlock the full power of Generals:

- **Memory system** keeps context lean while learning compounds
- **Social media documentation** makes operational work engaging
- **Role selection framework** ensures right commander for right task
- **Multi-variable testing** solves stubborn problems fast
- **Sanitization protocol** protects secrets while sharing knowledge
- **Context management** prevents bloat while preserving value
- **Campaign coordination** orchestrates complex multi-agent work

**Master these, and Generals becomes a force multiplier for AI-assisted operations.**

---

*"The difficult we do immediately. The impossible takes a little longer."*
— US Army Corps of Engineers motto
