# Project Organization Guide

<!-- NOTE FOR OTHER SESSIONS: This file is a navigation guide for Claude sessions working with the generals project.
     If you're new to this codebase, START HERE to understand the file structure.
     Do NOT reorganize files without reading this document first. -->

## Quick Navigation

**Looking for...** | **Check this file**
---|---
Commander roster with current XP/ribbons | [COMMAND-ROSTER.md](COMMAND-ROSTER.md)
Why Gordon Ramsay & CISO exist | [SPECIALISTS.md](SPECIALISTS.md)
XP system, medals, competence stars | [PROGRESSION-SYSTEM.md](PROGRESSION-SYSTEM.md)
Character portraits & narratives | [COMMAND-NARRATIVES.md](COMMAND-NARRATIVES.md)
Individual commander profiles | [profiles/](profiles/) directory
Deployment mission records | [deployments/](deployments/) directory
Project overview & quick start | [README.md](README.md)
**THIS navigation guide** | [ORGANIZATION.md](ORGANIZATION.md) *(you are here)*

---

## File Structure

```
generals/
├── README.md                    # Project overview, core concept, quick start
├── ORGANIZATION.md              # THIS FILE - navigation guide for sessions
├── COMMAND-ROSTER.md            # Full roster with XP, ribbons, medals
├── SPECIALISTS.md               # Why non-military specialists exist
├── PROGRESSION-SYSTEM.md        # XP, stars, ribbons, medals explained
├── COMMAND-NARRATIVES.md        # Atmospheric character portraits
│
├── profiles/                    # Individual commander profiles
│   ├── nimitz.md               # Fleet Admiral Nimitz full profile
│   ├── king.md                 # Fleet Admiral King full profile
│   ├── halsey.md               # Fleet Admiral Halsey full profile
│   ├── marshall.md             # General Marshall full profile
│   ├── spruance.md             # Admiral Spruance full profile
│   ├── montgomery.md           # Field Marshal Montgomery full profile
│   ├── eisenhower.md           # General Eisenhower full profile
│   ├── macarthur.md            # General MacArthur full profile
│   ├── rommel.md               # Generalfeldmarschall Rommel full profile
│   ├── zhukov.md               # Marshal Zhukov full profile
│   ├── bradley.md              # General Bradley full profile
│   ├── rickover.md             # Admiral Rickover full profile
│   ├── gordon-ramsay.md        # Gordon Ramsay specialist profile
│   ├── ciso-validator.md       # CISO Validator specialist profile
│   └── ernie-pyle.md           # Ernie Pyle specialist profile
│
├── deployments/                 # Mission records by date
│   ├── 2026-02-07-clearwatch/
│   │   ├── roster.md           # Who was deployed
│   │   ├── timeline.md         # What happened when
│   │   └── lessons.md          # What was learned
│   └── 2026-02-07-stunning-charts/
│       ├── roster.md
│       ├── timeline.md
│       └── lessons.md
│
├── specializations/             # Task-specific expertise docs (TODO)
├── patterns/                    # Reusable coordination patterns (TODO)
└── exports/                     # Exportable agent personas (TODO)
```

---

## File Purposes

### Core Documentation

#### README.md
**Purpose**: First file visitors see - project overview, core concept, quick start

**Contents**:
- What the Generals system is and why it exists
- Core concept (named personalities vs generic agents)
- Summary roster table (name, rank, specialization, XP only)
- How the system works (deployment, task assignment, experience accumulation)
- Project structure overview
- Core philosophy and self-learning mechanism

**Keep this file**:
- ✅ Concise and scannable
- ✅ High-level overview only
- ✅ Links to detailed docs (COMMAND-ROSTER, SPECIALISTS, PROGRESSION-SYSTEM)
- ❌ NO detailed roster (that's in COMMAND-ROSTER.md)
- ❌ NO lengthy explanations (link to dedicated files instead)

---

#### COMMAND-ROSTER.md
**Purpose**: Complete roster with all commander stats, ribbons, medals

**Contents**:
- Full 15-commander roster with personality traits
- XP leaderboard
- Medal of Honor recipients
- Competence progress tracking
- Statistical breakdown

**Update this file when**:
- Commander earns XP from deployment
- Campaign ribbon awarded
- Medal earned
- Competence star achieved
- New commander added to roster

**Synchronized with**: Individual profiles in `profiles/` directory (update both!)

---

#### SPECIALISTS.md
**Purpose**: Explain why non-military specialists (Gordon Ramsay, CISO, Ernie Pyle) exist

**Contents**:
- Why non-military specialists are necessary
- Current specialist roster with detailed rationales
- Integration with military command structure
- When to deploy specialists vs. commanders
- Criteria for adding new specialists

**This file answers**: "Why is Gordon Ramsay in a military-themed system?"

---

#### PROGRESSION-SYSTEM.md
**Purpose**: Complete reference for XP, competence stars, ribbons, medals

**Contents**:
- XP award criteria and bonuses
- Competence star progression (5/10/20/50/100 deployments)
- Campaign ribbon types and award criteria
- Medal hierarchy (Commendation → Distinguished Service → Medal of Honor → Order of Victory)
- Rank progression system
- Service record format
- Philosophy on earned expertise

**This file is**: The definitive reference for "How does progression work?"

---

#### COMMAND-NARRATIVES.md
**Purpose**: Atmospheric character portraits showing commanders "at work"

**Contents**:
- "War Room" narrative framing
- Character vignettes for each commander
- Personality traits demonstrated through narrative
- Post-deployment status updates
- Atmospheric world-building

**This file is**: The creative/narrative layer showing personalities in action

**Style**: Rich prose, atmospheric descriptions, character-driven storytelling

---

#### ORGANIZATION.md (THIS FILE)
**Purpose**: Navigation guide for Claude sessions working with this project

**Contents**:
- File structure map
- "Looking for X? Check Y" quick reference
- File purposes and update triggers
- Organization principles
- Notes for other sessions

**This file is**: The "README for Claude sessions" - start here if you're new

---

### Commander Profiles (`profiles/`)

Each commander has a detailed profile:

**Structure**:
1. Historical photo (Wikipedia public domain link)
2. Historical service record (birth, death, rank, commands)
3. WWII achievements and campaigns
4. Leadership style & personality traits
5. Historical quotes
6. Strengths and weaknesses
7. **AI Agent Service Record** (current specialization, XP, ribbons, medals)
8. Deployment history with behavioral observations
9. Integration of historical achievement with AI service
10. Path to next achievements

**Update profiles when**:
- Commander completes deployment (add to deployment history)
- XP earned (update total XP)
- Ribbon awarded (add to ribbons list)
- Medal earned (add with citation)
- Competence star achieved (update progress)
- Behavioral observations noted during deployment

---

### Deployment Records (`deployments/`)

Each deployment creates a directory: `YYYY-MM-DD-project-name/`

**Required files**:
- `roster.md` - Who was deployed, what roles
- `timeline.md` - Chronological mission timeline
- `lessons.md` - What was learned, what worked, what didn't

**Purpose**: Historical record of missions for learning and reference

---

## Organization Principles

### 1. README is the Front Door

README.md should be **scannable in 2 minutes**. If something requires detailed explanation, it goes in a dedicated file (COMMAND-ROSTER, SPECIALISTS, PROGRESSION-SYSTEM, etc.) and README links to it.

**Why**: Public visitors need quick understanding, not overwhelming detail.

---

### 2. Single Source of Truth for Stats

Commander XP, ribbons, and medals exist in **two places only**:
1. `COMMAND-ROSTER.md` - roster-level view
2. `profiles/{commander}.md` - individual profile

**Update both when stats change**. Do NOT let them drift out of sync.

**Why**: Inconsistent stats create confusion and erode trust in the system.

---

### 3. Narrative vs. Reference

**Narrative files** (COMMAND-NARRATIVES.md): Rich prose, atmospheric descriptions, character-driven
**Reference files** (COMMAND-ROSTER.md, PROGRESSION-SYSTEM.md): Tables, bullet points, factual data

**Don't mix**: Narrative files stay narrative, reference files stay reference.

---

### 4. Specialists are Integrated, Not Separate

Gordon Ramsay, CISO Validator, and Ernie Pyle appear in:
- COMMAND-ROSTER.md (alongside military commanders)
- README.md summary table (marked as *(Specialist)*)
- `profiles/` directory (same structure as military commanders)

They do NOT go in a separate "specialists" section. They're integrated members of the command structure.

**Why**: Specialists earn XP, ribbons, and medals just like military commanders. They're peers, not second-class citizens.

---

### 5. Historical Accuracy Matters

Military commanders have real WWII service records. **Honor them**:
- ✅ Accurate biographical details (birth/death dates, ranks, commands)
- ✅ Real achievements (Battle of Midway, D-Day, Pacific campaign)
- ✅ Documented personality traits from historical sources
- ❌ Fabricated achievements or exaggerated claims
- ❌ Treating real commanders as fictional characters

**Why**: "Never shortchange achievements" - core philosophy

---

## Common Tasks

### Adding XP to a Commander After Deployment

1. Calculate XP earned (base + bonuses - penalties)
2. Update `COMMAND-ROSTER.md`:
   - XP leaderboard
   - Competence progress table
3. Update `profiles/{commander}.md`:
   - Total XP in service record section
   - Add deployment entry to deployment history
   - Update competence progress
4. If ribbon/medal earned, add to both files

---

### Adding a New Commander

1. Research historical figure (if military) or persona (if specialist)
2. Create `profiles/{commander}.md` with full structure
3. Add to `COMMAND-ROSTER.md` roster section
4. Update `COMMAND-ROSTER.md` statistics tables
5. Add to `README.md` summary table
6. Add character portrait to `COMMAND-NARRATIVES.md`
7. If specialist, explain rationale in `SPECIALISTS.md`

---

### Recording a Deployment

1. Create `deployments/YYYY-MM-DD-project-name/` directory
2. Write `roster.md` (who was deployed, what roles)
3. Write `timeline.md` (chronological mission events)
4. Write `lessons.md` (what worked, what didn't, insights)
5. Update each deployed commander's profile with deployment entry
6. Award XP, ribbons, medals as appropriate
7. Update `COMMAND-ROSTER.md` statistics

---

### Creating a Character Narrative

Add to `COMMAND-NARRATIVES.md`:
- Set the scene (location, time, atmosphere)
- Show personality through action and dialogue
- Reference specific deployments or achievements
- Use rich prose and sensory details
- Stay true to historical personality traits

---

## Notes for Other Claude Sessions

### If You're Working on This Project

1. **Start here** (ORGANIZATION.md) to understand structure
2. **Check COMMAND-ROSTER.md** for current commander stats
3. **Read SPECIALISTS.md** if working with non-military specialists
4. **Reference PROGRESSION-SYSTEM.md** when calculating XP or awarding medals
5. **Don't reorganize** without understanding why files are structured this way

---

### If You're Updating Commander Stats

- Update **both** COMMAND-ROSTER.md and profiles/{commander}.md
- Keep XP, ribbons, medals synchronized
- Add deployment entries with behavioral observations
- Check if competence star should be awarded (5/10/20/50/100 deployments)

---

### If You're Adding Content

- **Narrative content** → COMMAND-NARRATIVES.md or deployment lessons
- **Reference data** → COMMAND-ROSTER.md or PROGRESSION-SYSTEM.md
- **Commander profiles** → profiles/ directory
- **Deployment records** → deployments/ directory
- **Project overview** → README.md (keep concise, link to detailed docs)

---

### If Something Seems Wrong

- **Inconsistent stats?** Check both COMMAND-ROSTER.md and profiles/{commander}.md
- **Missing specialist explanation?** Check SPECIALISTS.md
- **Unclear progression rules?** Check PROGRESSION-SYSTEM.md
- **Can't find something?** Use the "Quick Navigation" table at top of this file

---

## Philosophy Reminder

**"These were hard men not afraid to work really hard."**

This system honors real WWII achievements while building a functional AI agent coordination framework. When in doubt:

- Honor historical accuracy
- Earn expertise through repeated success
- Integrate specialists thoughtfully, not carelessly
- Keep narrative rich and reference data precise
- Document everything for future learning

---

**Last Updated**: 2026-02-08

**Questions?** Check the Quick Navigation table at the top of this file.
