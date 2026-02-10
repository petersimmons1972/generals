---
name: generals:award-experience
description: Update commander profile with deployment experience, XP, medals, and lessons learned
---

# Award Experience

## Purpose

After a commander completes a deployment, update their profile with:
- XP earned
- Deployment history entry
- Behavioral observations
- Lessons learned
- Ribbons/medals (if warranted)
- Competence progress toward stars

**This is how the self-learning cycle completes.** Each deployment makes commanders more experienced.

---

## Usage

```
/generals:award-experience <commander-name> <xp> <deployment-summary>
```

**Example:**
```
/generals:award-experience hopper 100 "Wrote EDR white paper for CISOs - excellent accessibility translation"
```

---

## How It Works

### **Step 1: Read Current Profile**

Load commander profile from `~/projects/generals/profiles/<name>.md` and extract:
- Current XP total
- Deployment count
- Competence progress
- Existing ribbons/medals

### **Step 2: Calculate Updates**

**XP Awards:**
- Base task: 50-100 XP
- Complex task: 100-150 XP
- Campaign leadership: 150-200 XP
- Exceptional performance: +50 bonus
- Lessons learned documented: +25 bonus

**Competence Progress:**
- Track deployments per category (e.g., "Technical Documentation")
- Progress toward stars: 10 deployments = ⭐ (Competent), 25 = ⭐⭐, 50 = ⭐⭐⭐, 100 = ⭐⭐⭐⭐, 250 = ⭐⭐⭐⭐⭐

**Ribbons/Medals:**
- Campaign Participation: Completed deployment
- Excellence: Exceptional quality or innovation
- Strategic Impact: Significant contribution to mission

### **Step 3: Update Profile**

Add new deployment entry in "AI Deployment History" section:

```markdown
### Deployment N: [Deployment Name] (YYYY-MM-DD)

**Mission**: [Task description]
**Role**: [What they did]
**Deliverable**: [What they produced]
**Outcome**: [SUCCESS/FAILURE with details]
**XP Earned**: [Amount] ([reason])

**Execution Details**:
[How they approached the task]

**Behavioral Observations**:
- [Trait 1]: [How it manifested in this deployment]
- [Trait 2]: [Consistency with historical personality]

**Lessons Learned**:
[What this deployment taught about the commander or the task type]

**Historical Parallel**:
[How this deployment relates to their WWII achievements]
```

### **Step 4: Update Statistics**

```markdown
**Current Rank**: [Rank]
**Specialization**: [Areas of expertise]
**Total XP**: [Old XP] → [New XP]
**Deployments**: [N] → [N+1]
**Success Rate**: [Percentage]
```

Update competence progress:
```markdown
| Category | Deployments | Progress to Star |
|----------|-------------|------------------|
| **Technical Documentation** | 2 → 3 | 3/10 (⭐ at 10) |
```

### **Step 5: Commit to GitHub**

```bash
git add profiles/<commander-name>.md
git commit -m "docs: [Commander] Deployment N - [brief description]

- XP: +[amount] (total: [new total])
- Deployment: [task summary]
- Lessons: [key lesson learned]

Co-Authored-By: [Commander Name] <commander@generals.ai>
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin master
```

---

## Output Format

```
═══════════════════════════════════════════════════════════════
GENERALS: AWARD EXPERIENCE
═══════════════════════════════════════════════════════════════

Commander: [Name]
Deployment: [Task description]

EXPERIENCE AWARDED
═══════════════════════════════════════════════════════════════
XP: +[amount]
  • Base: [base amount]
  • Bonus: [bonus reasons]

Total XP: [old] → [new]
Deployments: [N] → [N+1]

COMPETENCE PROGRESS
═══════════════════════════════════════════════════════════════
Category: [Category name]
Progress: [N/10] → [(N+1)/10]
[Progress bar: ████░░░░░░ 4/10 to ⭐]

Next milestone: [Deployments remaining] more deployments to earn ⭐

PROFILE UPDATED
═══════════════════════════════════════════════════════════════
✅ Deployment history added (Deployment [N])
✅ XP updated
✅ Competence progress incremented
✅ Behavioral observations documented
✅ Lessons learned captured

COMMITTED TO GITHUB
═══════════════════════════════════════════════════════════════
Commit: [hash]
Branch: master
Remote: Pushed to origin

Self-learning cycle complete. Commander profile now includes this
deployment experience for future reference.

═══════════════════════════════════════════════════════════════
```

---

## Dependencies

**Required:**
- Read (load profile)
- Edit (update profile)
- Bash (git commit/push)

**No other dependencies** - completely standalone.

---

## Self-Learning Integration

**This skill closes the loop:**

1. Match commander to task
2. Spawn commander with personality
3. Commander executes mission
4. **Award experience** ← YOU ARE HERE
5. Next time commander is spawned, updated profile includes this experience

**Each deployment makes commanders better:**
- More XP = more experienced
- More deployments = progress toward stars (⭐)
- Lessons learned = future spawns incorporate past experience
- Behavioral observations = validate personality consistency

---

## Privacy & Local Operation

**Completely local:**
- ✅ Updates files on your filesystem
- ✅ Commits to your local git repo
- ✅ Pushes to your remote (if you have one configured)
- ✅ No external API calls or data collection

Your commanders learn from YOUR campaigns, stored in YOUR repo.
