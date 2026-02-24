---
name: generals:campaign-coordinator
description: Coordinate multi-commander operations with team patterns, protocols, and quality gates
---

# Campaign Coordinator

Coordinate operations involving multiple commanders. Provides team structures, communication protocols, quality gates, and proven patterns.

**Use when**: Deploying 2+ commanders in parallel or complex multi-phase operations.

**Don't use**: Single commander tasks - just spawn directly.

---

## Quick Reference

### Campaign Patterns

| Pattern | Use Case | Structure | Speed | Details |
|---------|----------|-----------|-------|---------|
| **Parallel** | Independent tasks, no dependencies | Lead + N commanders + validators | Fast (50% of sequential) | [docs/CAMPAIGN-PATTERNS.md#parallel](../docs/CAMPAIGN-PATTERNS.md#parallel) |
| **Sequential** | Task dependencies, phased approach | Phase pipeline (Research → Plan → Build → Test → Deploy) | Slow (N × task time) | [docs/CAMPAIGN-PATTERNS.md#sequential](../docs/CAMPAIGN-PATTERNS.md#sequential) |
| **Swarm** | Collaborative on single deliverable | Lead + 3-5 specialists on same artifact | Medium (collab overhead) | [docs/CAMPAIGN-PATTERNS.md#swarm](../docs/CAMPAIGN-PATTERNS.md#swarm) |

### Team Structures

| Size | When | Structure |
|------|------|-----------|
| **Minimal** | <5 tasks, <3 days, low complexity | You + 1-3 commanders |
| **Standard** | 5-20 tasks, 3-10 days, medium complexity | Lead + Chief of Staff + 3-10 commanders + 2-3 validators |
| **Large** | 20+ tasks, 10+ days, high complexity | Full staff (Lead, CoS, Intel, Logistics, 10-20 commanders, 3-6 validators, Comms) |

---

## CRITICAL: HALT/RESUME Protocol

⚠️ **Learned from Operation Multi-Variant Deployment (Spruance 10hr delay)**

### The Problem

Personality-driven behavior differences:
- **Aggressive commanders** (Patton, Halsey) infer resumption from context
- **Methodical commanders** (Spruance, Bradley) wait for explicit RESUME order

### The Protocol

```
IF broadcasting HALT to commanders:
  1. State blocker reason clearly
  2. Investigate and resolve blocker
  3. WHEN blocker resolved:
     → Send EXPLICIT RESUME broadcast to ALL commanders
     → Include: "Blocker resolved. Resume operations. Authorization: [details]"
     → NEVER assume commanders will infer resumption
```

**Template**:
```
ALL COMMANDERS: RESUME OPERATIONS

Blocker resolved: [description]
RESUME ALL WORK. You are authorized to proceed.
No further approvals required.

[Team Lead]
```

**Why Critical**: Methodical commanders follow orders literally. "HALT" means "wait for RESUME," not "wait until you think it's safe."

[Full protocol: docs/LESSONS-LEARNED.md#halt-resume](../docs/LESSONS-LEARNED.md#halt-resume)

---

## Quality Gates

| Gate | Purpose | Who | Sample Size | Pass Criteria |
|------|---------|-----|-------------|---------------|
| **Build** | Code compiles, no syntax errors | Moreell, Rickover | 100% (builds fast) | 100% build success |
| **Functional** | Features work as specified | Layton, Spruance | 20-50% sample | 100% test pass rate |
| **Brand** | Content accuracy, voice, standards | Ogilvy | 30-50% spot-check | 100% consistency |

**Lesson from Operation Multi-Variant**: 36% functional sample (5/14 variants), 100% pass - sample-based testing sufficient.

[Details: docs/CAMPAIGN-PATTERNS.md#quality-gates](../docs/CAMPAIGN-PATTERNS.md)

---

## Commander Assignment

**PRIORITY RULE: Give experience to underutilized commanders first**

1. Check GitHub (https://github.com/petersimmons1972/generals) for current XP
2. **Prefer 0 XP commanders** when their specialization matches the task
3. Only use heavily deployed commanders if no underutilized alternative exists
4. Example: Dowding (0 XP, Systems Integration) > Rickover (925 XP) for architecture design

**Match personality to role** (within priority rule):

| Role | Commanders | Underutilized Alternative |
|------|-----------|---------------------------|
| **Team Lead** | Montgomery (200 XP), Eisenhower (50 XP), Marshall (100 XP) | Slim (0 XP, Innovation) |
| **Chief of Staff** | Bedell Smith (0 XP, detail-obsessed) | ✅ Use Bedell Smith |
| **Aggressive Tasks** | Patton (0 XP), Halsey (150 XP), MacArthur (50 XP) | ✅ Use Patton (0 XP) |
| **Methodical Tasks** | Bradley (75 XP), Spruance (225 XP) | Slim (0 XP, adaptable) |
| **Technical Tasks** | Groves (0 XP), Hopper (100 XP), Rickover (925 XP) | ✅ Use Groves (0 XP) |
| **Intelligence/Pattern** | Layton (0 XP), Orwell (0 XP), Murrow (0 XP) | ✅ Use any (all 0 XP) |
| **Quality Validators** | Build: Moreell (0 XP); Functional: Layton (0 XP); Brand: Ogilvy (0 XP) | ✅ Prefer 0 XP options |

[Full strategy: docs/CAMPAIGN-PATTERNS.md#commander-assignment](../docs/CAMPAIGN-PATTERNS.md#commander-assignment)

---

## Communication Protocols

### Daily Standup (if campaign >3 days)

1. Commanders report to Chief of Staff: Progress, blockers, next 24hrs
2. Chief of Staff synthesizes → Team Lead
3. Team Lead makes decisions, unblocks

### Blocker Escalation

```
Commander encounters blocker
  → Report to Chief of Staff immediately (don't wait)
  → CoS resolves or escalates to Team Lead
  → Team Lead decides: HALT all? HALT affected only? Workaround?
```

**Key**: Immediate escalation, not at next standup.

---

## Campaign Workflow

1. **Plan**: Define goals, choose pattern/structure, break into tasks
2. **Match**: Use `/generals:match-commander-to-task` for each role
3. **Spawn**: `TeamCreate` + `/generals:spawn-commander` for each member
4. **Execute**: Apply pattern, HALT/RESUME protocol, daily standups if >3 days
5. **Quality Gates**: Validate (build, functional, brand), fix issues, re-validate
6. **Award**: Use `/generals:award-experience` for each commander, commit lessons
7. **Retrospective**: Document lessons, update patterns

[Full workflow: docs/CAMPAIGN-PATTERNS.md](../docs/CAMPAIGN-PATTERNS.md)

---

## Error Handling

| Issue | Diagnosis | Resolution |
|-------|-----------|------------|
| **Commander not responding** | Check: Received task? Clear assignment? Waiting for orders? | Send explicit instructions (likely waiting for RESUME) |
| **Quality gate failure** | Validator documents issues | Assign fix to ORIGINAL commander → re-validate → repeat until pass |
| **Scope creep** | Deliverable > spec, timeline extends, unapproved features | Accept if valuable, trim if excessive, redirect to spec |

[Details: docs/CAMPAIGN-PATTERNS.md#error-handling](../docs/CAMPAIGN-PATTERNS.md#error-handling)

---

## Timeline Estimation

**Personality multipliers** (observed):
- Aggressive (Patton): 0.5x - 0.7x baseline
- Balanced (Bradley): 1.0x baseline
- Methodical (Spruance): 1.3x - 1.5x baseline

**Pattern multipliers**:
- Parallel: ~50% of sequential time
- Sequential: N tasks × 1 task time each
- Swarm: 1.5x single commander (collaboration overhead)

**Add**: 10-20% for quality gates

[Full metrics: docs/CAMPAIGN-PATTERNS.md#success-metrics](../docs/CAMPAIGN-PATTERNS.md#success-metrics)

---

## Case Study

**Operation Multi-Variant Deployment** (Feb 2026):
- 14 website variants deployed in parallel
- Team: Montgomery, Bedell Smith, 14 commanders, 3 validators
- 14/14 deployed in ~18 hours (vs 35+ sequential)
- 100% quality gate pass rate
- Key lesson: HALT/RESUME protocol critical

[Full case study: docs/LESSONS-LEARNED.md](../docs/LESSONS-LEARNED.md)

---

## Dependencies

**Required**:
- `TeamCreate` - Create team structure
- `Task` - Spawn commanders
- `SendMessage` - Coordinate communication
- `TaskCreate/TaskUpdate` - Track work

**Optional**:
- `superpowers:brainstorming` - Plan campaign
- `superpowers:writing-plans` - Document plan
- `superpowers:subagent-driven-development` - Parallel framework

---

## Contributing

Discovered better patterns? Learned from campaigns?

1. Document in service records
2. Update [docs/LESSONS-LEARNED.md](../docs/LESSONS-LEARNED.md)
3. Submit PR with lessons

---

## Summary

**Proven patterns for multi-commander coordination**:
- 3 campaign patterns (Parallel, Sequential, Swarm)
- HALT/RESUME protocol (critical for methodical commanders)
- 3 quality gates (Build, Functional, Brand)
- 3 team structures (Minimal, Standard, Large)
- Lessons from Operation Multi-Variant Deployment

**Use when coordinating 2+ commanders.**

Next: Document YOUR campaign lessons to improve these patterns.
