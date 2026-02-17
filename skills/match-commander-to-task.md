---
name: generals:match-commander-to-task
description: Analyze task requirements and recommend commanders based on personality fit
---

# Match Commander to Task

Analyze task requirements and recommend best-fit commander(s) based on personality traits, strengths, and past deployment experience.

**Prevents mismatches** (Patton for methodical validation, Spruance for aggressive breakthrough).

---

## Usage

```
/generals:match-commander-to-task <task-description>
```

**Example**:
```
/generals:match-commander-to-task "Write technical white paper on enterprise EDR deployment"
```

---

## How It Works

### Step 1: Analyze Task Requirements

Extract task characteristics:
- **Pace**: Fast/aggressive vs. methodical/careful
- **Style**: Bold/dramatic vs. calm/measured
- **Complexity**: Simple execution vs. complex coordination
- **Domain**: Technical, strategic, creative, operational
- **Risk tolerance**: High-risk breakthrough vs. low-risk validation
- **Communication**: Direct/forceful vs. measured/diplomatic

### Step 2: Scan Commander Profiles

Read all profiles in `~/projects/generals/profiles/` and score each:
- Personality alignment (1-5 stars)
- Domain expertise (relevant experience)
- Past deployment success in similar tasks
- Current availability/competence level

### Step 3: Recommend Top 3

Return:
1. **Best match** - Highest fit, detailed rationale
2. **Alternative 1** - Second-best, why they'd also work
3. **Alternative 2** - Third option, different approach

For each:
- Personality fit explanation
- What they'll excel at
- What to watch for
- Expected timeline/approach

---

## Output

```
TASK ANALYSIS
═══════════════════════════════════════════════════════════════
Task: [Description]

Requirements:
• Pace: [Fast/Methodical]
• Style: [Bold/Measured]
• Domain: [Technical/Strategic/Creative]
• Risk: [High/Low]

RECOMMENDED COMMANDERS
═══════════════════════════════════════════════════════════════

🥇 BEST MATCH: [Commander]
Personality Fit: ⭐⭐⭐⭐⭐ (5/5)
Domain Expertise: [Experience]
Past Success: [Similar deployments]

Why:
• [Reason 1]
• [Reason 2]

Excel At:
• [Strength 1]
• [Strength 2]

Watch For:
• [Potential issue]

Timeline: [Fast/Medium/Slow]

---

🥈 ALTERNATIVE 1: [Commander]
Personality Fit: ⭐⭐⭐⭐ (4/5)
[Similar format...]

---

🥉 ALTERNATIVE 2: [Commander]
Personality Fit: ⭐⭐⭐ (3/5)
[Similar format...]

═══════════════════════════════════════════════════════════════
RECOMMENDATION: Use [Best Match] unless [specific reason for alternative]

Next: /generals:spawn-commander [best-match] "[task]"
```

[Full output examples: docs/OUTPUT-FORMATS.md#match-commander](../docs/OUTPUT-FORMATS.md#match-commander)

---

## Commander Types Quick Reference

| Type | Commanders | Best For |
|------|-----------|----------|
| **Aggressive** | Patton, Halsey, MacArthur | Fast execution, breakthrough |
| **Methodical** | Spruance, Bradley, Nimitz | Quality validation, accuracy |
| **Coordinators** | Montgomery, Eisenhower, Marshall | Team lead, coalition |
| **Technical** | Hopper, Rickover, Groves | Technical depth, engineering |
| **Creative** | Mitchell, Slim, Rommel | Innovation, adaptation |

[Detailed traits: docs/LESSONS-LEARNED.md#commander-behavior](../docs/LESSONS-LEARNED.md#commander-behavior)

---

## Dependencies

**Required**:
- `Read` - Scan profiles
- `Glob` - Find all profiles

**No other dependencies** - completely standalone.
