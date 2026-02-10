# Generals - AI Commander Coordination System

**Self-learning multi-agent coordination using historical military commanders as personality templates.**

---

## What Is This?

Generals is a system for coordinating AI agents (Claude Code subagents) using historical military commanders as personality templates. Each commander has distinct traits, strengths, and weaknesses that influence how they approach tasks.

**Example:**
- Need aggressive, fast deployment? → Use General Patton
- Need methodical validation? → Use Admiral Spruance
- Need technical documentation? → Use Admiral Hopper
- Need multi-force coordination? → Use Field Marshal Montgomery

Each commander "learns" from deployments, accumulating experience (XP), lessons, and behavioral observations that inform future spawns.

---

## Quick Start

### **1. Clone This Repo**

```bash
git clone https://github.com/petersimmons1972/generals.git
cd generals
```

You now have:
- 24 commander profiles with accumulated knowledge
- Service records from past campaigns
- 4 coordination skills
- Templates for documentation

### **2. Install Skills** (Optional but Recommended)

```bash
# Symlink skills to your Claude Code skills directory
ln -s ~/projects/generals/skills ~/.claude/skills/generals

# Or copy them
cp -r ~/projects/generals/skills ~/.claude/skills/generals
```

### **3. Use a General**

**Simple usage (Claude auto-matches):**
```
User: "I need a technical white paper on enterprise security for CISOs"

Claude: [Internally matches task to Hopper, spawns her, executes]
```

**Explicit usage (you control):**
```
User: "/generals:match-commander-to-task 'Write technical white paper for CISOs'"

Claude: [Shows top 3 matches with rationale]

User: "/generals:spawn-commander hopper 'Write white paper...'"

Claude: [Spawns Hopper with personality-preserved prompt]
```

---

## How It Works

### **The Self-Learning Cycle**

```
┌───────────────────────────────────────────────────┐
│  1. MATCH: Analyze task → recommend commander    │
└────────────────┬──────────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────────┐
│  2. SPAWN: Generate personality-preserved         │
│     prompt from profile → launch agent            │
└────────────────┬──────────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────────┐
│  3. EXECUTE: Commander completes mission          │
│     using their personality traits                │
└────────────────┬──────────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────────┐
│  4. AWARD: Update profile with XP, lessons,       │
│     behavioral observations → commit to GitHub    │
└────────────────┬──────────────────────────────────┘
                 ↓
          Next spawn includes this experience
```

**Each deployment makes commanders more experienced.**

---

## Commander Personalities

### **Aggressive Executors** (Speed over caution)
- **Patton** - Bold breakthrough, "good plan violently executed now"
- **Halsey** - Aggressive strikes, "Hit hard, hit fast, hit often"
- **MacArthur** - Dramatic operations, strategic boldness

### **Methodical Validators** (Precision over speed)
- **Spruance** - Calculated risk, "The Quiet Warrior"
- **Bradley** - Steady reliability, logistics-focused
- **Nimitz** - Strategic patience, force preservation

### **Coordinators** (Multi-force management)
- **Montgomery** - Multi-force coordination, meticulous planning
- **Eisenhower** - Coalition management, diplomatic coordination
- **Marshall** - "The Organizer of Victory," strategic logistics

### **Technical Specialists**
- **Hopper** - Compiler inventor, makes complex concepts accessible
- **Rickover** - Quality obsession, technical standards
- **Groves** - Manhattan Project, large-scale technical management

### **Creative Thinkers**
- **Mitchell** - Innovative doctrine, unconventional approaches
- **Slim** - Adaptive strategy, terrain mastery
- **Rommel** - Tactical creativity, rapid adaptation

**Full roster:** 24 commanders, each with detailed profiles in `/profiles/`

---

## The Four Core Skills

### **1. match-commander-to-task**
Analyze task requirements → recommend best-fit commanders

**When to use:** Unsure which commander fits your task

**Output:** Top 3 matches with personality fit analysis, what to expect

### **2. spawn-commander**
Read profile → generate personality-preserved spawn prompt

**When to use:** Ready to deploy a specific commander

**Output:** Task tool invocation with full personality context

### **3. award-experience**
Update profile with XP, lessons learned, behavioral observations

**When to use:** After commander completes deployment

**Output:** Updated profile committed to GitHub (self-learning complete)

### **4. campaign-coordinator**
Multi-commander coordination patterns, protocols, quality gates

**When to use:** Coordinating 2+ commanders working together

**Output:** Team structures, communication protocols, lessons from past campaigns

---

## Self-Learning & Knowledge Evolution

### **How Learning Works**

This is a **living, self-learning system**. Commanders learn from deployments.

**When you clone this repo:**
- ✅ You get current commanders with accumulated knowledge
- ✅ Your campaigns teach YOUR generals new lessons
- ⚠️ Your lineage diverges from origin after cloning
- ⚠️ Your learning stays local unless you contribute back

**Think of it like forking a codebase:**
- **Origin repo** = blessed lineage curated by @petersimmons1972
- **Your fork** = your personal lineage with your campaign lessons
- **No automatic sync** = divergent evolution after clone

### **Contributing Learning (Optional)**

Discovered valuable lessons? Share with the community:

1. Document in service records (`SERVICE-RECORD-*.md`)
2. Commit to your fork
3. Submit PR to origin with lesson summary
4. Community review → merge if valuable

This enables **collective learning** while preserving **privacy**.

---

## Superpowers Integration (Optional)

Generals work **standalone** with only core Claude Code tools, but integrate well with **superpowers** skills:

### **Recommended (Not Required):**
- `superpowers:brainstorming` - Campaign design and planning
- `superpowers:writing-plans` - Implementation planning
- `superpowers:subagent-driven-development` - Parallel execution framework

**Benefits of superpowers:**
- Enhanced team coordination patterns
- Proven planning workflows
- Parallel execution with quality gates

**But:** Generals work fine without them. No hard dependencies.

---

## Privacy & Data

Generals is a **completely local system**:
- ✅ All learning happens on your machine
- ✅ Profiles stored in your filesystem
- ✅ No data sent to external servers
- ✅ No telemetry, analytics, or tracking
- ✅ Your campaigns stay private

**Your generals learn from YOUR campaigns, stored in YOUR repo.**

---

## Requirements

### **Minimum:**
- Claude Code (core tools: Task, Read, Edit, Write, Bash, TeamCreate)
- Git (for committing service records)
- This repository cloned locally
- **Experimental Agent Teams flag enabled** (see below)

### **Required: Agent Teams Flag**

Generals uses Claude Code's **Agent Teams** feature (introduced with Opus 4.6, February 2026) to spawn and coordinate multiple commander instances in parallel. This feature is currently a **research preview** and requires an experimental flag.

**You must enable this before using Generals.** Claude Code cannot enable it automatically — it requires manual configuration.

**Option A: Environment variable (per-session)**
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
claude
```

**Option B: Shell profile (persistent)**
```bash
# Add to your ~/.bashrc, ~/.zshrc, or equivalent:
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```
Then restart your terminal or run `source ~/.bashrc`.

**Without this flag**, TeamCreate, SendMessage, and multi-agent coordination will not be available, and Generals will fail to spawn commander teams.

### **Recommended:**
- Superpowers skills (optional, enhances coordination)
- GitHub account (for contributing lessons back)

### **No Other Dependencies**
- No external APIs
- No server infrastructure
- No data collection
- Completely standalone

---

## Installation

### **Option 1: Quick Start** (Use without skills)
```bash
git clone https://github.com/petersimmons1972/generals.git
cd generals

# Claude can read profiles directly and coordinate
# Skills make it easier but aren't required
```

### **Option 2: Full Install** (With skills)
```bash
git clone https://github.com/petersimmons1972/generals.git
cd generals

# Symlink skills to Claude Code
ln -s $(pwd)/skills ~/.claude/skills/generals

# Now you can use /generals:* commands
```

---

## Philosophy

### **Why Historical Commanders?**

1. **Rich personality data**: WWII commanders have well-documented traits, decisions, and outcomes
2. **Proven under pressure**: These personalities succeeded (or failed) in high-stakes coordination
3. **Distinct characteristics**: Patton ≠ Spruance ≠ Hopper - real diversity in approaches
4. **Cultural knowledge**: Most people understand "Patton = aggressive" without reading profiles
5. **Educational value**: Learning about historical figures while coordinating AI agents

### **Why Self-Learning?**

Traditional agent systems start from zero each time. Generals **accumulate experience**:
- Deployment 1: Hopper learns "postal system analogies work"
- Deployment 2: That lesson informs her spawn prompt
- Deployment 3: She builds on both previous experiences

**Each campaign makes the system better.**

### **Why Fork-Based Learning?**

Centralized learning requires servers, privacy policies, and trust. Fork-based learning:
- ✅ Preserves privacy (local by default)
- ✅ Enables community contribution (optional PRs)
- ✅ Git-native (familiar workflow)
- ✅ No infrastructure (GitHub hosts it)

**Distributed learning with optional community curation.**

---

## Contributing

We welcome community contributions. See `CONTRIBUTING.md` for guidelines.

---

## License

MIT License

---

## Credits

**Created by:** @petersimmons1972
**Inspired by:** Operation Multi-Variant Deployment (Feb 8-9, 2026)
**Built with:** Claude Code (Anthropic)

---

*"The most dangerous phrase in the language is, 'We've always done it this way.'"* - Admiral Grace Hopper
