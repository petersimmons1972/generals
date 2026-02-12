---
name: generals:spawn-commander
description: Spawn commander with personality from profile, generating Task tool invocation
---

# Spawn Commander

Read commander profile, extract personality/historical context, generate spawn prompt preserving character.

**Foundation skill** - Everything starts here.

---

## Usage

```
/generals:spawn-commander <commander-name> <task-description>
```

**Parameters**:
- `commander-name` - Profile filename without .md (e.g., "patton", "hopper", "montgomery")
- `task-description` - Clear mission statement (1-2 sentences)

**Examples**:
```
/generals:spawn-commander patton "Deploy aggressive variant website with bold CTA"
/generals:spawn-commander spruance "Validate trust variant for accuracy and calm tone"
/generals:spawn-commander montgomery "Coordinate 14-front parallel deployment"
```

---

## How It Works

### Step 1: Read Profile

Location: `~/projects/generals/profiles/<commander-name>.md`

**Extracts**:
- Historical context (WWII achievements, command roles)
- Core personality traits (Leadership Style & Personality section)
- Strengths and weaknesses
- AI deployment history (past campaigns, lessons learned)
- Current XP/competence

### Step 2: Analyze Task Fit

**Match task requirements to commander personality**:
- Aggressive task → Aggressive commander (Patton, Halsey)
- Methodical task → Methodical commander (Spruance, Bradley)
- Coordination task → Multi-force coordinator (Montgomery, Eisenhower)
- Technical task → Technical specialist (Hopper, Rickover)
- Creative task → Innovative thinker (Mitchell, Groves)

**If mismatch detected**: Warns but proceeds with better recommendation.

### Step 3: Generate Spawn Prompt

**Includes**:
1. Identity: "You are [Rank] [Name]"
2. Mission: Clear task statement
3. Personality traits: Core characteristics to embody
4. Historical parallel: How task relates to WWII experience
5. Strengths to leverage
6. Weaknesses to watch
7. Voice/tone: Communication style

### Step 4: Return Task Tool Invocation

**Output**: Ready-to-execute Task tool call with generated prompt.

---

## Output

### Perfect Match

```
✅ EXCELLENT MATCH

Commander: General George S. Patton Jr.
Personality: Aggressive, bold, action-oriented
Task: Deploy aggressive variant

Historical Parallel:
Third Army advanced 600 miles in 6 months
→ Requires similar breakthrough speed

What to Expect:
✅ Immediate action (minimal planning)
✅ Bold choices (impact over subtlety)
⚠️ May skip validation for speed
💬 Direct, forceful communication

Task tool invocation ready.
```

### Mismatch Warning

```
⚠️ PERSONALITY MISMATCH

Commander: Patton
Task: Validate trust variant (requires methodical precision)

MISMATCH:
❌ Task needs: Methodical, careful validation
❌ Patton excels: Fast, aggressive execution
⚠️ Risk: May rush validation, miss issues

RECOMMENDATION: Use Admiral Spruance instead

Proceed anyway? Invocation generated, but consider better match.
```

[Full output examples: docs/OUTPUT-FORMATS.md](../docs/OUTPUT-FORMATS.md)

---

## Commander Quick Reference

| Type | Commanders | Best For |
|------|-----------|----------|
| **Aggressive** | Patton, Halsey, MacArthur | Fast execution, breakthrough, aggressive content |
| **Methodical** | Spruance, Bradley, Nimitz | Quality validation, accuracy-critical, trust content |
| **Coordinators** | Montgomery, Eisenhower, Marshall | Team lead, coalition management, strategic planning |
| **Technical** | Hopper, Rickover, Groves | Technical validation, engineering, quality assurance |
| **Creative** | Mitchell, Slim, Rommel | Innovation, unconventional approaches, adaptive strategy |

[Detailed traits: docs/LESSONS-LEARNED.md#commander-behavior](../docs/LESSONS-LEARNED.md#commander-behavior)

---

## Workflow Integration

**Typical campaign flow**:
1. **Match**: Use `/generals:match-commander-to-task` (finds best fit)
2. **Spawn**: Use this skill (generate personality prompt) ← **YOU ARE HERE**
3. **Coordinate**: Use `/generals:campaign-coordinator` (manage execution)
4. **Award**: Use `/generals:award-experience` (capture lessons, update profile)

---

## Advanced Usage

### Custom Parameters

Generated Task tool defaults (can override):
```json
{
  "subagent_type": "general-purpose",
  "model": "sonnet",  // Override: "haiku" (simple), "opus" (complex)
  "description": "[Auto-generated]",
  "prompt": "[From profile]",
  "name": "[commander-name]"
}
```

### Team Coordination

**Multi-commander teams**:
1. Spawn team lead first (Montgomery)
2. Use `TeamCreate` for structure
3. Spawn commanders under team lead
4. Lead coordinates using campaign-coordinator patterns

---

## Self-Learning Integration

**After deployment**:
1. Note behavioral observations (matched expectations?)
2. Document lessons learned
3. Use `/generals:award-experience` to update profile
4. Service records capture success/failure

**Next spawn**:
- Updated profile includes new experience
- Prompt incorporates recent lessons
- Commander "learns" from past deployments

**This closes the self-learning loop.**

---

## Error Handling

**Profile not found**:
```
❌ ERROR: Profile not found
Location: ~/projects/generals/profiles/patton.md
Available: [lists all profiles]
```

**Invalid commander name**:
```
❌ ERROR: Use profile filename without .md
Provided: "george-patton"
Available: patton, spruance, montgomery
```

**Vague task**:
```
⚠️ WARNING: Task description vague
Provided: "do something"
Example: "Deploy aggressive variant with bold CTA"
```

---

## Dependencies

**Required**:
- `Read` - Load commander profile
- `Task` - Spawn agent with generated prompt

**Files**:
- Commander profile at `~/projects/generals/profiles/<name>.md`

**Optional**:
- `/generals:match-commander-to-task` - Find best fit first
- `superpowers:*` - Spawned commanders can use if available

---

## Privacy

**Completely local**:
- ✅ Reads profiles from your filesystem
- ✅ Generates prompts locally
- ✅ No external API calls
- ✅ No data sent anywhere

Your commanders, your campaigns, your machine.

---

## Summary

**Transforms static profiles into living commanders.**

Input: Profile (markdown) + Task description
Output: Personality-preserved prompt + Task tool invocation
Result: Commander behaves consistently with historical character

**Use as foundation for all Generals coordination work.**

Next: Use `/generals:campaign-coordinator` for multi-commander operations.
