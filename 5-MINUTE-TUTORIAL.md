# 5-Minute Quick Start Guide

Get from zero to your first deployed commander in 5 minutes.

---

## Step 1: Enable Agent Teams (30 seconds)

Generals uses Claude Code's **Agent Teams** feature. Enable it:

```bash
# Add to your shell config (~/.bashrc or ~/.zshrc)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Then reload
source ~/.bashrc  # or source ~/.zshrc
```

**Why this matters:** Without this flag, multi-commander coordination won't work.

---

## Step 2: Clone & Install (1 minute)

```bash
# Clone the repository
git clone https://github.com/petersimmons1972/generals.git
cd generals

# Optional: Install skills for slash commands
ln -s $(pwd)/skills ~/.claude/skills/generals
```

**What you now have:**
- ✓ 20 commander profiles with accumulated knowledge
- ✓ Service records from past campaigns
- ✓ 4 coordination skills
- ✓ Complete progression system
- ✓ Templates for documentation

---

## Step 3: Deploy Your First Commander (2 minutes)

### Option A: Let Claude Auto-Match

Just describe your task naturally:

```
You: "I need to deploy a critical security patch to production NOW."

Claude: [Analyzes task requirements]
        [Matches → General Patton: aggressive execution, no delays]
        [Spawns Patton with full personality context]

Patton: "No time for committee meetings. Here's what we're doing:
         1. Patch is going to staging NOW
         2. 60-second smoke test
         3. Rolling deploy across all nodes
         4. If it breaks, we roll back. We don't wait."

[Patton completes deployment in 8 minutes]
[Service record automatically updated with XP and lessons]
```

### Option B: Choose Your Commander Explicitly

Use the slash command to pick:

```
You: "/generals:spawn-commander patton 'Deploy security patch immediately'"

Claude: [Reads Patton's profile + past deployment lessons]
        [Generates personality-preserved spawn prompt]
        [Launches Patton subagent]

Patton: [Aggressive execution mode activated]
```

### Option C: Run a Multi-Commander Campaign

For complex work requiring coordination:

```
You: "/generals:campaign-coordinator 'Generate security report with charts and validation'"

Claude: [Deploys multi-commander team]

        Operation Assigned:
        ├── Admiral Nimitz (Research) — Gather intelligence
        ├── Admiral Spruance (Analysis) — Cost modeling, risk
        ├── Fleet Admiral King (Visuals) — Data visualization
        ├── Field Marshal Montgomery (Coordination) — Orchestra conductor
        └── Gordon Ramsay (Quality Gate) — Presentation standards

[All commanders work in parallel, Montgomery coordinates]
[Service records updated for all at completion]
```

---

## Step 4: See Results (1 minute)

After deployment completes, check what happened:

```bash
# View the commander's service record
cat profiles/patton.md

# See recent deployments section:
# - XP earned (+200 XP)
# - Lessons learned ("Rolling deploys safer than big-bang")
# - Behavioral observations ("Patton moved decisively under time pressure")
# - Competence progress (Emergency Response: 3/5 → ⭐)
```

---

## What Just Happened?

1. **Task analyzed** — Claude identified the task type and personality fit
2. **Commander spawned** — Patton loaded with historical traits + past lessons
3. **Mission executed** — Patton applied his aggressive, decisive approach
4. **Learning captured** — Service record updated with XP, lessons, observations
5. **Committed to GitHub** — Next spawn automatically includes this experience

**The 2nd deployment of Patton will be smarter than the 1st because he learned from it.**

---

## Visual Example: How The Roster Works

### The 20 Commanders

| Category | Commanders | Use When... |
|----------|-----------|-------------|
| **Aggressive Executors** | Patton, Halsey, MacArthur | Speed matters more than caution |
| **Methodical Validators** | Spruance, Bradley, Nimitz | Precision matters more than speed |
| **Multi-Force Coordinators** | Montgomery, Eisenhower, Marshall | Multiple teams need orchestration |
| **Technical Specialists** | Hopper, Rickover, Groves | Deep domain expertise required |
| **Creative Thinkers** | Mitchell, Slim, Rommel | Problem needs fresh approach |
| **Quality Gates** | Ramsay, CISO Validator | Presentation/content validation |
| **War Correspondents** | Pyle, Murrow, Orwell | LinkedIn/social documentation |

**Full roster with photos:** See [COMMAND-ROSTER.md](COMMAND-ROSTER.md)

---

## Your First Day Workflow

### Morning: Deploy Single Commanders

```
Task: "Fix the broken authentication service"
→ Claude suggests: Field Marshal Slim (disaster recovery specialist)
→ Deploy Slim
→ Service restored, lesson learned: "Check OAuth token expiry first"
```

### Afternoon: Run a Campaign

```
Task: "Generate competitive analysis report with charts"
→ Claude deploys Operation [Name]
→ 5 commanders: Research, Analysis, Visuals, Coordination, Quality
→ 45-page report with 14 charts
→ All service records updated
```

### Evening: Review Learning

```bash
# See what commanders learned today
git diff profiles/

# Commit the day's learning
git commit -m "Service records: authentication fix + report generation"
git push
```

---

## Next Steps

**You now understand the basics.** For deeper understanding:

- **Philosophy** → [PHILOSOPHY.md](PHILOSOPHY.md) — Why this works
- **Advanced Features** → [ADVANCED-FEATURES.md](ADVANCED-FEATURES.md) — Memory, social media, testing
- **Full Roster** → [COMMAND-ROSTER.md](COMMAND-ROSTER.md) — Meet all 20 commanders
- **Skills Reference** → [SKILLS.md](SKILLS.md) — Deep dive on the 4 core skills

---

## Common First-Day Questions

### "How do I know which commander to use?"

Let Claude auto-match. The system analyzes:
- Task urgency (CRITICAL → Patton)
- Task type (Research → Nimitz, Charts → King)
- Complexity (Simple → single commander, Complex → campaign)

### "What if I pick the wrong commander?"

**No penalty for experimentation.** If Patton was too aggressive, deploy Spruance next time. The system learns from both approaches.

### "Do I need all 20 commanders?"

No. Start with 3-5. Most work uses:
- Patton (aggressive execution)
- Spruance (careful validation)
- Montgomery (coordination)
- Hopper (technical innovation)
- Ramsay (quality gate)

Discover the others organically.

### "How much does this cost?"

**Zero infrastructure costs.** Everything runs locally:
- No external servers
- No API keys required
- No subscriptions
- No telemetry/tracking

You only pay for Claude Code usage (your existing subscription).

### "Can I customize the commanders?"

**Yes.** Edit `profiles/*.md` to adjust personality traits, add lessons, modify spawn prompts. It's your fork — diverge as needed.

---

## Troubleshooting

### "Agent Teams aren't working"

```bash
# Verify flag is set
echo $CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS
# Should output: 1

# If empty, add to shell config and reload
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
source ~/.bashrc
```

### "Skills aren't available"

```bash
# Verify symlink
ls -la ~/.claude/skills/generals
# Should point to: /path/to/generals/skills

# If missing, create it
ln -s $(pwd)/skills ~/.claude/skills/generals
```

### "Service records aren't updating"

After each deployment, run:

```
You: "/generals:award-experience patton 200 'Deployed security patch successfully. Lesson: rolling deploys safer than big-bang.'"

Claude: [Updates profiles/patton.md]
        [Commits to git]
        [Pushes to remote]
```

This is normally automatic during campaigns, but can be manual for single deployments.

---

## Visual: The Self-Learning Cycle

```
┌─────────────────────────────────────────────────────────────────────┐
│  DEPLOYMENT 1: Patton deployed for emergency fix                   │
│  Lesson captured: "Check pod logs before assuming network issue"   │
└────────────────────────┬────────────────────────────────────────────┘
                         ↓
                  profiles/patton.md updated
                  Lesson stored in profile
                         ↓
┌─────────────────────────────────────────────────────────────────────┐
│  DEPLOYMENT 2: Patton spawned again                                │
│  Spawn prompt now includes: "Remember: check pod logs first"       │
│  → Patton follows lesson automatically                             │
└────────────────────────┬────────────────────────────────────────────┘
                         ↓
                  New lesson learned
                  Profile grows smarter
                         ↓
                  Deployment 3 is even better...
```

**Each deployment makes commanders more experienced. Automatically.**

---

## Success Checklist

After 5 minutes, you should have:

- [x] Agent Teams flag enabled
- [x] Generals repository cloned
- [x] At least one commander deployed
- [x] Seen service record update with XP/lessons
- [x] Understanding of the self-learning cycle

**You're ready.** Start deploying commanders for real work and watch them get smarter over time.

---

*"Plans are worthless, but planning is everything."*
— General Dwight D. Eisenhower
