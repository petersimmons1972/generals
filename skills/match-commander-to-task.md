---
name: generals:match-commander-to-task
description: Analyze task requirements and recommend commanders based on personality fit
---

# Match Commander to Task

## Purpose

Analyze a task's requirements and recommend the best-fit commander(s) based on personality traits, strengths, and past deployment experience.

**This prevents mismatches** (like using Patton for methodical validation or Spruance for aggressive breakthrough).

---

## Usage

```
/generals:match-commander-to-task <task-description>
```

**Example:**
```
/generals:match-commander-to-task "Write technical white paper on enterprise EDR deployment"
```

---

## How It Works

### **Step 1: Analyze Task Requirements**

Extract task characteristics:
- **Pace**: Fast/aggressive vs. methodical/careful
- **Style**: Bold/dramatic vs. calm/measured
- **Complexity**: Simple execution vs. complex coordination
- **Domain**: Technical, strategic, creative, operational
- **Risk tolerance**: High-risk breakthrough vs. low-risk validation
- **Communication**: Direct/forceful vs. measured/diplomatic

### **Step 2: Scan Commander Profiles**

Read all profiles in `~/projects/generals/profiles/` and score each on task fit:
- Personality alignment (1-5 stars)
- Domain expertise (relevant experience)
- Past deployment success in similar tasks
- Current availability/competence level

### **Step 3: Recommend Top 3**

Return:
1. **Best match** - Highest fit score, detailed rationale
2. **Alternative 1** - Second-best, why they'd also work
3. **Alternative 2** - Third option, different approach

For each recommendation:
- Personality fit explanation
- What they'll excel at
- What to watch for
- Expected timeline/approach

---

## Output Format

```
TASK ANALYSIS
═══════════════════════════════════════════════════════════════
Task: [Description]

Requirements Detected:
• Pace: [Fast/Methodical]
• Style: [Bold/Measured]
• Domain: [Technical/Strategic/Creative]
• Complexity: [Simple/Complex]
• Risk: [High/Low]

RECOMMENDED COMMANDERS
═══════════════════════════════════════════════════════════════

🥇 BEST MATCH: [Commander Name]
Personality Fit: ⭐⭐⭐⭐⭐ (5/5)
Domain Expertise: [Relevant experience]
Past Success: [Similar deployments]

Why This Commander:
• [Reason 1]
• [Reason 2]
• [Reason 3]

What They'll Excel At:
• [Strength 1 applied to task]
• [Strength 2 applied to task]

Watch For:
• [Potential issue]

Expected Approach: [How they'll tackle it]
Timeline: [Fast/Medium/Slow]

---

🥈 ALTERNATIVE 1: [Commander Name]
Personality Fit: ⭐⭐⭐⭐ (4/5)
[Similar format...]

---

🥉 ALTERNATIVE 2: [Commander Name]
Personality Fit: ⭐⭐⭐ (3/5)
[Similar format...]

═══════════════════════════════════════════════════════════════
RECOMMENDATION: Use [Best Match] unless [specific reason to consider alternative]

Next: /generals:spawn-commander [best-match-name] "[task]"
```

---

## Dependencies

**Required:**
- Read (scan profiles)
- Glob (find all profiles)

**No other dependencies** - completely standalone.
