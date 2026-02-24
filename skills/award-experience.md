---
name: generals:award-experience
description: Update commander profile with deployment experience, XP, medals, and lessons learned
---

# Award Experience

Update commander profile after deployment with XP, deployment history, behavioral observations, lessons learned, ribbons/medals, and competence progress.

**This closes the self-learning cycle.** Each deployment makes commanders more experienced.

⚠️ **CRITICAL**: Updates MUST be committed to GitHub (https://github.com/petersimmons1972/generals).

Local profiles are working copies only. GitHub is the authoritative source of truth. If you don't update GitHub, future sessions will have stale XP/deployment data and may re-deploy already-experienced commanders as if they're fresh. **ALWAYS COMMIT TO GITHUB after awarding experience.**

---

## Usage

```
/generals:award-experience <commander-name> <xp> <deployment-summary>
```

**Example**:
```
/generals:award-experience hopper 100 "Wrote EDR white paper - excellent accessibility translation"
```

---

## How It Works

### Step 1: Read Current Profile

Load `~/projects/generals/profiles/<name>.md` and extract:
- Current XP total
- Deployment count
- Competence progress
- Existing ribbons/medals

### Step 2: Calculate Updates

**XP Awards**:
- Base task: 50-100 XP
- Complex task: 100-150 XP
- Campaign leadership: 150-200 XP
- Exceptional performance: +50 bonus
- Lessons documented: +25 bonus

**Competence Progress**:
- Track deployments per category
- Stars: 10 deployments = ⭐, 25 = ⭐⭐, 50 = ⭐⭐⭐, 100 = ⭐⭐⭐⭐, 250 = ⭐⭐⭐⭐⭐

**Ribbons/Medals**:
- Campaign Participation: Completed deployment
- Excellence: Exceptional quality/innovation
- Strategic Impact: Significant mission contribution

### Step 3: Update Profile

Add deployment entry in "AI Deployment History":

```markdown
### Deployment N: [Name] (YYYY-MM-DD)

**Mission**: [Task description]
**Role**: [What they did]
**Deliverable**: [What they produced]
**Outcome**: [SUCCESS/FAILURE with details]
**XP Earned**: [Amount] ([reason])

**Execution Details**:
[How they approached the task]

**Behavioral Observations**:
- [Trait 1]: [How it manifested]
- [Trait 2]: [Consistency with historical personality]

**Lessons Learned**:
[What this taught about commander/task type]

**Historical Parallel**:
[How this relates to WWII achievements]
```

### Step 4: Update Statistics

```markdown
**Total XP**: [Old XP] → [New XP]
**Deployments**: [N] → [N+1]
**Success Rate**: [Percentage]
```

Update competence table:
```markdown
| Category | Deployments | Progress to Star |
|----------|-------------|------------------|
| **Technical Documentation** | 2 → 3 | 3/10 (⭐ at 10) |
```

### Step 5: Commit to GitHub

```bash
git add profiles/<commander-name>.md
git commit -m "docs: [Commander] Deployment N - [brief description]

- XP: +[amount] (total: [new total])
- Deployment: [task summary]
- Lessons: [key lesson]

Co-Authored-By: [Commander] <commander@generals.ai>
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin master
```

---

## Output

```
═══════════════════════════════════════════════════════════════
GENERALS: AWARD EXPERIENCE
═══════════════════════════════════════════════════════════════

Commander: [Name]
Deployment: [Task]

EXPERIENCE AWARDED
═══════════════════════════════════════════════════════════════
XP: +[amount]
  • Base: [base]
  • Bonus: [reasons]

Total XP: [old] → [new]
Deployments: [N] → [N+1]

COMPETENCE PROGRESS
═══════════════════════════════════════════════════════════════
Category: [Category]
Progress: [N/10] → [(N+1)/10]
████░░░░░░ 4/10 to ⭐

Next milestone: [X] more deployments to earn ⭐

PROFILE UPDATED
═══════════════════════════════════════════════════════════════
✅ Deployment history added
✅ XP updated
✅ Competence progress incremented
✅ Behavioral observations documented
✅ Lessons learned captured

COMMITTED TO GITHUB
═══════════════════════════════════════════════════════════════
Commit: [hash]
Branch: master
Remote: Pushed to origin

Self-learning cycle complete.
═══════════════════════════════════════════════════════════════
```

[Full output example: docs/OUTPUT-FORMATS.md#award-experience](../docs/OUTPUT-FORMATS.md#award-experience)

---

## Self-Learning Integration

**This skill closes the loop**:

1. Match commander to task
2. Spawn commander with personality
3. Commander executes mission
4. **Award experience** ← **YOU ARE HERE**
5. Next spawn includes this experience

**Each deployment makes commanders better**:
- More XP = more experienced
- More deployments = progress toward stars
- Lessons learned = future spawns incorporate experience
- Behavioral observations = validate personality consistency

---

## Dependencies

**Required**:
- `Read` - Load profile
- `Edit` - Update profile
- `Bash` - Git commit/push

**No other dependencies** - completely standalone.

---

## Privacy

**Completely local**:
- ✅ Updates files on your filesystem
- ✅ Commits to your local git repo
- ✅ Pushes to your remote (if configured)
- ✅ No external API calls

Your commanders learn from YOUR campaigns, stored in YOUR repo.
