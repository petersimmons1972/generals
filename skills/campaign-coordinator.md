---
name: generals:campaign-coordinator
description: Coordinate multi-commander operations with team patterns, protocols, and quality gates
---

# Campaign Coordinator

## Purpose

Coordinate operations involving multiple commanders working together. Provides team structures, communication protocols, quality gates, and lessons learned from past campaigns.

**Use this when:**
- Deploying multiple commanders in parallel
- Coordinating complex multi-phase operations
- Setting up quality validation workflows
- Need proven coordination patterns

---

## When to Use

### **Single Commander Tasks**
❌ Don't use this skill - just spawn the commander directly

### **Multi-Commander Campaigns**
✅ Use this skill to:
- Set up team structure
- Establish communication protocols
- Define quality gates
- Coordinate parallel work
- Manage dependencies between commanders

---

## Campaign Patterns

### **Pattern 1: Parallel Execution (Independent Fronts)**

**When to use:**
- Multiple independent tasks (no dependencies)
- Each commander works on separate deliverable
- Example: Deploy 14 website variants, each with own commander

**Structure:**
```
Team Lead (1)
├─ Chief of Staff (1) - Daily coordination, blocker escalation
├─ Front Commanders (N) - Independent parallel execution
└─ Quality Validators (3-6) - Post-deployment validation
```

**Coordination:**
- Team Lead assigns tasks, makes strategic decisions
- Chief of Staff runs daily standups, tracks progress, resolves blockers
- Front Commanders execute independently (no cross-dependencies)
- Quality Validators test after all fronts complete

**Tools:**
- `TeamCreate` - Create team structure
- `Task` - Spawn each commander
- `SendMessage` - Coordinate communication
- `TaskCreate/TaskUpdate` - Track work

**Timeline:** Fast (parallel execution maximizes speed)

**Lessons from Operation Multi-Variant Deployment:**
- ✅ Works well: 14 commanders deployed 42 pages in ~18 hours
- ⚠️ HALT/RESUME Protocol: If you broadcast HALT, you MUST broadcast explicit RESUME
- ⚠️ Methodical commanders (Spruance, Bradley) wait for explicit orders - don't assume they'll infer resumption
- ⚠️ Quality validators: 3 sufficient (build, functional, brand) - don't over-recruit

---

### **Pattern 2: Sequential Pipeline (Dependencies)**

**When to use:**
- Tasks have dependencies (output of Task A → input for Task B)
- Assembly-line workflow
- Example: Research → Plan → Build → Test → Deploy

**Structure:**
```
Team Lead (1)
├─ Phase 1: Research Commander (1)
├─ Phase 2: Planning Commander (1)
├─ Phase 3: Implementation Commanders (N)
├─ Phase 4: Testing Commander (1)
└─ Phase 5: Deployment Commander (1)
```

**Coordination:**
- Each phase completes before next begins
- Handoffs require verification (Phase N output validates before Phase N+1 starts)
- Team Lead approves progression between phases

**Tools:** Same as Pattern 1, plus dependency tracking

**Timeline:** Slower (sequential bottleneck)

**When to use:** Complex projects where later phases depend on earlier work

---

### **Pattern 3: Swarm (Collaborative)**

**When to use:**
- Single complex deliverable requiring multiple perspectives
- Commanders collaborate on same artifact
- Example: Strategic plan requiring military, technical, and political input

**Structure:**
```
Team Lead (1)
└─ Specialist Commanders (3-5) - Collaborate on single deliverable
    ├─ Military Strategy (Patton, Marshall)
    ├─ Technical Architecture (Hopper, Rickover)
    └─ Political Coordination (Eisenhower, Montgomery)
```

**Coordination:**
- Commanders work on same document/deliverable
- Regular sync meetings to align
- Team Lead resolves conflicts between perspectives

**Tools:** Same as Pattern 1, plus shared workspace (Google Docs, Git branch)

**Timeline:** Medium (collaboration overhead)

**When to use:** Deliverable requires diverse expertise

---

## Communication Protocols

### **HALT/RESUME Discipline (CRITICAL)**

**Learned from:** Operation Multi-Variant Deployment (Spruance 10-hour delay)

**The Problem:**
When you broadcast HALT to multiple commanders:
- Aggressive commanders (Patton, Halsey) infer resumption from context
- Methodical commanders (Spruance, Bradley) wait for explicit RESUME order

**The Protocol:**
```
IF broadcasting HALT to all commanders:
  1. State blocker reason clearly
  2. Investigate blocker resolution
  3. WHEN blocker resolved:
     → Send EXPLICIT RESUME broadcast to ALL commanders
     → Include: "Blocker resolved. Resume operations. Authorization: [details]"
     → Never assume commanders will infer resumption
```

**Why This Matters:**
Methodical commanders follow orders exactly. "HALT" means "stop and wait for RESUME," not "stop until you think it's safe to continue."

**Template Message:**
```
ALL COMMANDERS: RESUME OPERATIONS

Blocker identified at [time]: [description]
Blocker resolved at [time]: [resolution]

RESUME ALL WORK. You are authorized to proceed.

No further approvals required. Execute your assigned missions.

[Team Lead signature]
```

---

### **Daily Standup (For Multi-Week Campaigns)**

**When:** Campaigns lasting >3 days

**Format:**
1. Each commander reports (via SendMessage to Chief of Staff):
   - Progress since last standup
   - Blockers (if any)
   - Plan for next 24 hours
2. Chief of Staff synthesizes → reports to Team Lead
3. Team Lead makes decisions, unblocks issues

**Frequency:** Daily for long campaigns, unnecessary for <3 day sprints

---

### **Blocker Escalation**

**Protocol:**
```
Commander encounters blocker
  ↓
Report to Chief of Staff immediately (don't wait for standup)
  ↓
Chief of Staff assesses:
  - Can I resolve? → Resolve and inform Team Lead
  - Strategic decision? → Escalate to Team Lead immediately
  ↓
Team Lead decides:
  - HALT all commanders? (if blocker affects everyone)
  - HALT only affected commanders?
  - Proceed with workaround?
```

**Key:** Blockers escalate immediately, not at next standup.

---

## Quality Gates

### **Gate 1: Build Validation**

**Purpose:** Verify code compiles, dependencies resolve, no syntax errors

**Commander Type:** Technical validator (Moreell, Rickover)

**Process:**
1. All deployments complete
2. Validator attempts build on each deliverable
3. Reports: Pass/Fail per deliverable + error details

**Pass Criteria:** 100% build success (no compilation errors)

**Learned from:** Operation Multi-Variant Deployment
- Moreell validated 14/14 variants built successfully
- TypeScript strict mode: 93% pass (acceptable)

---

### **Gate 2: Functional Testing**

**Purpose:** Verify features work as specified

**Commander Type:** Methodical tester (Layton, Spruance)

**Process:**
1. Sample testing (test representative subset, not exhaustive)
2. Test categories: Navigation, content accuracy, responsive design, accessibility, performance
3. Reports: Pass/Fail per category

**Pass Criteria:** 100% test pass rate (no functional defects)

**Sample Size:**
- Small campaigns (<5 deliverables): Test all
- Medium campaigns (5-20): Test 30-50%
- Large campaigns (>20): Test 20-30% (statistically significant sample)

**Learned from:** Operation Multi-Variant Deployment
- Layton tested 5/14 variants (36% sample)
- 50/50 tests passed (100% rate)
- Sample-based testing sufficient for quality confidence

---

### **Gate 3: Brand/Content Consistency**

**Purpose:** Verify content accuracy, voice consistency, brand standards

**Commander Type:** Brand expert (Ogilvy) or domain validator (CISO for security content)

**Process:**
1. Spot-check sample for:
   - Factual accuracy (no false claims)
   - Voice consistency (matches intended personality)
   - Brand standards (logos, colors, tone)
2. Reports: Pass/Fail per deliverable + issues found

**Pass Criteria:** 100% brand consistency (zero factual errors, voice matches spec)

**Learned from:** Operation Multi-Variant Deployment
- Ogilvy validated 6/14 variants (43% sample)
- 100% biographical accuracy, perfect voice consistency

---

## Team Structures

### **Minimal Team (Small Campaign)**

```
You (acting as Team Lead)
└─ 1-3 Commanders (execute tasks)
```

**When:** <5 tasks, <3 day duration, low complexity

**Coordination:** You manage everything directly

---

### **Standard Team (Medium Campaign)**

```
Team Lead (You or Montgomery)
├─ Chief of Staff (Bedell Smith) - Daily ops
├─ Front Commanders (3-10) - Execute tasks
└─ Quality Validators (2-3) - Test after completion
```

**When:** 5-20 tasks, 3-10 day duration, medium complexity

**Coordination:** Chief of Staff handles daily ops, you make strategic decisions

---

### **Large Team (Major Campaign)**

```
Team Lead (Montgomery, Eisenhower)
├─ Chief of Staff (Bedell Smith) - Operations coordination
├─ Intelligence (Layton) - Analytics, metrics, reporting
├─ Logistics (Marshall) - Resource allocation, dependencies
├─ Front Commanders (10-20) - Parallel execution
├─ Quality Validators (3-6) - Multi-track testing
└─ Communications (Ogilvy) - Stakeholder updates, documentation
```

**When:** 20+ tasks, 10+ day duration, high complexity

**Coordination:** Full staff structure, you focus on strategic decisions only

---

## Commander Assignment Strategy

### **Match Personality to Role**

**Team Lead:**
- **Large campaigns**: Montgomery (multi-force coordination)
- **Coalition campaigns**: Eisenhower (diplomatic coordination)
- **Technical campaigns**: Marshall (logistics & organization)

**Chief of Staff:**
- Bedell Smith (unglamorous excellence, detail-obsessed)

**Front Commanders (Aggressive Tasks):**
- Patton, Halsey, MacArthur (speed, breakthrough)

**Front Commanders (Methodical Tasks):**
- Spruance, Bradley, Nimitz (precision, validation)

**Front Commanders (Technical Tasks):**
- Hopper, Rickover, Groves (technical depth)

**Quality Validators:**
- Build: Moreell, Rickover (engineering rigor)
- Functional: Layton, Spruance (methodical testing)
- Brand: Ogilvy (content standards)

---

## Timeline Estimation

### **Factors:**

**Commander Personality:**
- Aggressive (Patton): 0.5x - 0.7x baseline (fast)
- Balanced (Bradley): 1.0x baseline (standard)
- Methodical (Spruance): 1.3x - 1.5x baseline (slower but thorough)

**Task Complexity:**
- Simple (single file edit): Hours
- Medium (feature implementation): Days
- Complex (architecture design): Weeks

**Dependencies:**
- Parallel (no dependencies): N tasks in ~1 task time
- Sequential (dependencies): N tasks × 1 task time each

**Quality Gates:**
- Add 10-20% time for validation rounds

---

## Error Handling

### **Commander Not Responding**

**Diagnosis:**
1. Check inbox: Did they receive the task?
2. Check task assignment: Is task clear?
3. Check blockers: Are they waiting on something?

**Resolution:**
- If waiting for orders: Send explicit instructions
- If blocked: Remove blocker or reassign task
- If unclear task: Clarify and restate mission

**Learned from:** Operation Multi-Variant Deployment
- Spruance waited 10 hours for explicit RESUME
- Not a failure - he correctly followed orders
- Lesson: Explicit communication prevents delays

---

### **Quality Gate Failures**

**Protocol:**
```
Quality gate fails
  ↓
Validator documents issues
  ↓
Assign fix to ORIGINAL commander (they know the code)
  ↓
Commander fixes issues
  ↓
Validator re-tests
  ↓
Repeat until pass
```

**Don't:**
- Assign fixes to different commander (context loss)
- Skip re-validation after fixes (assume it's fixed)
- Proceed to next phase with open issues

---

### **Scope Creep**

**Prevention:**
- Clear task definitions upfront
- "Done" criteria specified per task
- Aggressive commanders (Patton) may add features - review before accepting

**Detection:**
- Deliverable larger than specified
- Timeline extends beyond estimate
- Commander adding "improvements" not requested

**Resolution:**
- Accept if improvements valuable
- Trim if scope creep excessive
- Redirect commander focus to original spec

---

## Success Metrics

### **Campaign-Level Metrics**

- **Delivery Rate**: Tasks completed / Tasks assigned
- **Quality Rate**: Quality gates passed / Quality gates attempted
- **Timeline Accuracy**: Actual duration / Estimated duration
- **Coordination Efficiency**: Blockers resolved / Blockers raised

### **Commander-Level Metrics**

- **Speed**: Tasks completed per day
- **Quality**: First-time quality pass rate
- **Collaboration**: Messages sent/received ratio
- **Autonomy**: Questions asked per task (lower = more autonomous)

**Use metrics to:**
- Award XP (high performers get bonuses)
- Improve estimates (learn actual vs estimated duration)
- Refine assignments (match commanders to roles better)

---

## Integration with Workflow

**Full Campaign Flow:**

1. **Plan Campaign**
   - Define goals, break into tasks
   - Choose team structure (minimal/standard/large)
   - Assign commanders to tasks

2. **Match Commanders**
   - Use `generals:match-commander-to-task` for each role
   - Verify personality fit

3. **Spawn Team**
   - Use `TeamCreate` for structure
   - Use `generals:spawn-commander` for each member
   - Establish communication channels

4. **Execute Campaign**
   - Use THIS SKILL for coordination patterns
   - Apply HALT/RESUME protocol as needed
   - Daily standups if >3 days

5. **Quality Gates**
   - Run validation after completion
   - Fix issues, re-validate
   - 100% pass required

6. **Award Experience**
   - Use `generals:award-experience` for each commander
   - Document lessons learned
   - Commit to GitHub

7. **Campaign Retrospective**
   - What worked? What failed?
   - Update this skill with new lessons
   - Improve future campaigns

---

## Dependencies

**Required:**
- TeamCreate (core) - Create team structure
- Task (core) - Spawn commanders
- SendMessage (core) - Coordinate communication
- TaskCreate/TaskUpdate (core) - Track work

**Optional:**
- `superpowers:brainstorming` - Plan campaign approach
- `superpowers:writing-plans` - Document implementation plan
- `superpowers:subagent-driven-development` - Parallel execution framework

**No hard dependencies** - works with core Claude Code tools.

---

## Privacy & Local Operation

**Completely local:**
- ✅ All coordination happens on your machine
- ✅ Team data stored in `~/.claude/teams/`
- ✅ No external API calls
- ✅ Your campaigns stay private

---

## Contributing

Discovered better coordination patterns? Learned from failed campaigns?

1. Document in service records
2. Update this skill with new patterns
3. Submit PR with lessons learned

Community improvements welcome via pull requests.

---

## Summary

**This skill provides proven patterns for multi-commander coordination:**

- **3 campaign patterns**: Parallel, Sequential, Swarm
- **HALT/RESUME protocol**: Critical for methodical commanders
- **3 quality gates**: Build, Functional, Brand
- **3 team structures**: Minimal, Standard, Large
- **Commander assignment strategy**: Personality → Role matching
- **Lessons from real campaigns**: Operation Multi-Variant Deployment

**Use this skill when coordinating 2+ commanders working together.**

Next: Document lessons learned from YOUR campaigns to improve this skill.
