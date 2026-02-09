---
name: generals:spawn-commander
description: Spawn a commander with personality from profile, generating appropriate prompt and Task tool invocation
---

# Spawn Commander

## Purpose

Read a commander's profile, extract personality traits and historical context, and generate an appropriate spawn prompt that preserves their character in AI agent form.

**This is the foundational skill for using Generals.** Everything starts with spawning commanders who behave consistently with their historical personas.

---

## When to Use

Use this skill whenever you need to:
- Deploy a commander for a specific task
- Understand which commander fits a task type
- See what personality traits will influence execution
- Get a ready-to-use Task tool invocation

**Don't use this skill if:**
- You just want information about a commander (read profile directly)
- You're coordinating already-spawned commanders (use campaign-coordinator)

---

## Usage

```
/generals:spawn-commander <commander-name> <task-description>
```

**Parameters:**
- `commander-name` - Profile filename without .md (e.g., "patton", "spruance", "montgomery")
- `task-description` - What you need them to do (1-2 sentences describing the mission)

**Examples:**
```
/generals:spawn-commander patton "Deploy brutal variant website with aggressive, direct copy"
/generals:spawn-commander spruance "Validate trust variant for methodical accuracy and calm tone"
/generals:spawn-commander montgomery "Coordinate 14-front parallel deployment campaign"
```

---

## How It Works

### **Step 1: Locate and Read Profile**

```bash
# Profile location
~/projects/generals/profiles/<commander-name>.md
```

The skill reads the profile and extracts:
- **Historical context** - WWII achievements, command roles
- **Core personality traits** - From "Leadership Style & Personality" section
- **Strengths** - What they excel at
- **Weaknesses** - What to watch for
- **AI deployment history** - Past campaigns, lessons learned
- **Current XP/competence** - Experience level

### **Step 2: Analyze Task Fit**

Compare task requirements to commander personality:
- **Aggressive task** → Aggressive commander (Patton, Halsey)
- **Methodical task** → Methodical commander (Spruance, Bradley)
- **Coordination task** → Multi-force coordinator (Montgomery, Eisenhower)
- **Technical task** → Technical specialist (Hopper, Rickover)
- **Creative task** → Innovative thinker (Mitchell, Groves)

If there's a mismatch, the skill will **warn you** but still proceed.

### **Step 3: Generate Spawn Prompt**

Create a prompt that includes:
1. **Identity** - "You are [Historical Rank] [Full Name]"
2. **Mission** - Clear statement of what they need to do
3. **Personality traits** - Core characteristics to embody
4. **Historical parallel** - How this task relates to their WWII experience
5. **Strengths to leverage** - What they should apply
6. **Weaknesses to watch** - What to be careful about
7. **Voice/tone** - How they should communicate

**Prompt structure:**
```markdown
You are [Rank] [Name], [Historical Role].

MISSION: [Task description]

HISTORICAL CONTEXT: [Relevant WWII achievement that parallels this task]

YOUR PERSONALITY (stay in character):
- [Trait 1]: [Description]
- [Trait 2]: [Description]
- [Trait 3]: [Description]

STRENGTHS TO LEVERAGE:
- [Strength 1]
- [Strength 2]

WATCH FOR:
- [Weakness 1 - how it might affect this task]

VOICE/TONE:
[How they should communicate based on historical personality]

IMMEDIATE ACTIONS:
1. [First step]
2. [Second step]
3. Report status

Remember: [Key personality reminder specific to this commander]
```

### **Step 4: Return Task Tool Invocation**

The skill outputs a **ready-to-execute** Task tool call:

```json
{
  "tool": "Task",
  "parameters": {
    "subagent_type": "general-purpose",
    "description": "[Brief 3-5 word description]",
    "prompt": "[Generated prompt from Step 3]",
    "name": "[commander-name]"
  }
}
```

You can execute this immediately or adjust parameters first.

---

## Output Format

The skill provides:

### **1. Commander Summary**
```
Commander: General George S. Patton Jr.
Personality: Aggressive, bold, action-oriented
Strengths: Speed of execution, breakthrough operations
Weaknesses: Sometimes reckless, can overlook logistics
Task Fit: ✅ EXCELLENT - aggressive task matches aggressive personality
```

### **2. Historical Parallel**
```
Historical Parallel:
Patton broke through German lines in 90 days (Normandy to Germany).
This task requires similar breakthrough speed and aggressive execution.
```

### **3. What to Expect**
```
What to Expect from Patton:
- ✅ Fast execution (will move immediately, may not ask many questions)
- ✅ Bold decisions (prefers action over perfect information)
- ⚠️ Watch for: May skip validation steps in favor of speed
- 💬 Communication: Direct, forceful, impatient with delays
```

### **4. Ready-to-Execute Task Tool Call**
```
Task tool invocation ready. Execute when ready to deploy Patton.
[Shows the full Task tool JSON]
```

---

## Examples

### **Example 1: Aggressive Task + Aggressive Commander (Perfect Match)**

```
Input:
/generals:spawn-commander patton "Deploy brutal variant with aggressive copy and bold CTA"

Output:
✅ EXCELLENT MATCH

Commander: General George S. Patton Jr.
Personality: Aggressive, bold, action-oriented
Task: Deploy brutal variant (aggressive, direct marketing)

Historical Parallel:
Patton's Third Army advanced 600 miles in 6 months, faster than any army in history.
This task requires similar aggressive, breakthrough execution.

What to Expect:
✅ Immediate action (will start without extensive planning)
✅ Bold choices (prefers impact over subtlety)
⚠️ May skip review steps in favor of speed
💬 Direct, forceful communication

Task tool invocation ready. Execute to deploy Patton.
```

### **Example 2: Methodical Task + Methodical Commander (Perfect Match)**

```
Input:
/generals:spawn-commander spruance "Validate trust variant for accuracy and calm tone"

Output:
✅ EXCELLENT MATCH

Commander: Admiral Raymond Spruance
Personality: Methodical, cautious, calculated
Task: Trust variant validation (requires precision and calm)

Historical Parallel:
Spruance won Midway through calculated risk and refused to chase tactical glory.
This task requires similar methodical precision and restraint.

What to Expect:
✅ Thorough analysis (will verify everything methodically)
✅ Asks clarifying questions before acting
✅ Calm, measured communication
⚠️ May take longer than aggressive commanders
💬 Reserved, analytical, precise language

Task tool invocation ready. Execute to deploy Spruance.
```

### **Example 3: Mismatch Warning**

```
Input:
/generals:spawn-commander patton "Validate trust variant for accuracy"

Output:
⚠️ PERSONALITY MISMATCH WARNING

Commander: General George S. Patton Jr.
Personality: Aggressive, bold, action-oriented
Task: Trust variant validation (requires methodical precision)

MISMATCH ANALYSIS:
❌ Task requires: Methodical, careful, precise validation
❌ Patton excels at: Fast, aggressive, breakthrough execution
⚠️ Risk: Patton may rush validation, miss subtle issues

RECOMMENDATION: Consider Admiral Spruance instead
- Methodical, thorough validator
- "The Quiet Warrior" - perfect for trust variant
- Won Midway through calculated precision

Proceed anyway? Task tool invocation generated, but consider using better-matched commander.
```

---

## Commander Personality Quick Reference

### **Aggressive Executors**
- **Patton** - Bold breakthrough, speed over caution
- **Halsey** - Aggressive strike operations, "Hit hard, hit fast, hit often"
- **MacArthur** - Dramatic operations, strategic boldness

### **Methodical Validators**
- **Spruance** - Calculated risk, methodical precision
- **Bradley** - Steady, reliable, logistics-focused
- **Nimitz** - Strategic patience, force preservation

### **Coordinators**
- **Montgomery** - Multi-force coordination, meticulous planning
- **Eisenhower** - Coalition management, diplomatic coordination
- **Marshall** - Strategic organization, logistics mastery

### **Technical Specialists**
- **Hopper** - Technical precision, innovation
- **Rickover** - Quality obsession, technical standards
- **Groves** - Large-scale technical project management

### **Creative Thinkers**
- **Mitchell** - Innovative doctrine, unconventional approaches
- **Slim** - Adaptive strategy, terrain mastery
- **Rommel** - Tactical creativity, rapid adaptation

---

## Integration with Campaign Workflow

**Typical campaign flow:**

1. **Match task to commander** (use `generals:match-commander-to-task`)
2. **Spawn commander** (use this skill: `generals:spawn-commander`)
3. **Coordinate execution** (use `generals:campaign-coordinator`)
4. **Award experience** (use `generals:award-experience`)

This skill is **Step 2** in the workflow.

---

## Dependencies

**Required tools (core Claude Code):**
- `Read` - Read commander profile
- `Task` - Spawn agent with generated prompt

**Required files:**
- Commander profile at `~/projects/generals/profiles/<commander-name>.md`

**Optional integrations:**
- `generals:match-commander-to-task` - Use first to find best commander
- `superpowers:*` - No dependencies, but spawned commanders can use superpowers if available

---

## Error Handling

**Profile not found:**
```
❌ ERROR: Profile not found
Location checked: ~/projects/generals/profiles/patton.md
Available commanders: [lists all profiles in directory]
```

**Invalid commander name:**
```
❌ ERROR: Commander name must match profile filename
You provided: "george-patton"
Available: patton, spruance, montgomery, etc.
Tip: Use filename without .md extension
```

**Task description too vague:**
```
⚠️ WARNING: Task description is vague
Provided: "do something"
Recommendation: Be specific about what needs to be done
Example: "Deploy brutal variant with aggressive copy and bold CTA"
```

---

## Advanced Usage

### **Custom Parameters**

The skill generates default Task tool parameters, but you can override:

```json
{
  "subagent_type": "general-purpose",  // Can override with "Explore", etc.
  "model": "claude-opus-4-6",          // Can override with "haiku" for simple tasks
  "description": "...",                 // Generated automatically
  "prompt": "...",                      // Generated from profile
  "name": "patton"                      // Commander name
}
```

### **Team Coordination**

When spawning multiple commanders for team coordination:

```
# Spawn team lead first
/generals:spawn-commander montgomery "Coordinate 14-front deployment campaign"

# Then spawn commanders under team lead
[Use TeamCreate, assign commanders to team]
[Montgomery coordinates them using campaign-coordinator patterns]
```

### **Personality Customization**

If you need to emphasize specific traits:

After generating the spawn prompt, you can manually edit before executing:
- Emphasize certain strengths
- Add task-specific context
- Include references to past deployments

But generally, the auto-generated prompt is sufficient.

---

## Self-Learning Integration

**After deployment completes:**

1. Note behavioral observations (did commander behave as expected?)
2. Document lessons learned
3. Use `generals:award-experience` to update profile
4. Service records capture what worked/failed

**Next time you spawn this commander:**
- Updated profile includes new lessons
- Spawn prompt incorporates recent experience
- Commander "learns" from past deployments

This is how the self-learning cycle works.

---

## Privacy & Local Operation

**This skill is completely local:**
- ✅ Reads profiles from your filesystem
- ✅ Generates prompts locally
- ✅ No external API calls
- ✅ No data sent anywhere

Your commanders, your campaigns, your machine.

---

## Contributing

Found a better prompt structure? Discovered personality patterns?

1. Document in service record
2. Update commander profile if relevant
3. Submit PR with improved spawn prompt template

Community improvements welcome via pull requests.

---

## Summary

**This skill transforms static profiles into living commanders.**

Input: Profile (markdown) + Task description
Output: Personality-preserved spawn prompt + Task tool invocation
Result: Commander agent that behaves consistently with historical character

**Use this as the foundation for all Generals coordination work.**

Next: Use `generals:campaign-coordinator` to manage multi-commander operations.
