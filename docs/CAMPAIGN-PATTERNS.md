# Campaign Patterns - Detailed Guide

Comprehensive guide to multi-commander coordination patterns.

---

## Pattern 1: Parallel Execution (Independent Fronts) {#parallel}

### When to Use

✅ **Perfect for**:
- Multiple independent tasks (no dependencies between them)
- Each commander works on separate deliverable
- Want maximum speed through parallel execution

❌ **Not for**:
- Tasks with dependencies (use Sequential pattern)
- Single deliverable requiring collaboration (use Swarm pattern)

### Structure

```
Team Lead (1)
├─ Chief of Staff (1) - Daily coordination, blocker escalation
├─ Front Commanders (N) - Independent parallel execution
└─ Quality Validators (3-6) - Post-deployment validation
```

**Roles**:
- **Team Lead**: Strategic decisions, approvals, final authority
- **Chief of Staff**: Daily operations, blocker resolution, progress tracking
- **Front Commanders**: Execute assigned tasks independently
- **Quality Validators**: Test deliverables after completion (build, functional, brand)

### Coordination

**Daily Operations** (if campaign >3 days):
1. Commanders report progress to Chief of Staff
2. Chief of Staff synthesizes and reports to Team Lead
3. Team Lead makes strategic decisions, unblocks issues

**Communication**:
- Commanders work autonomously (minimal cross-communication)
- Blockers escalate to Chief of Staff immediately
- Team Lead coordinates only when strategic decision needed

**Tools**:
- `TeamCreate` - Create team structure
- `Task` - Spawn each commander
- `SendMessage` - Coordinate communication
- `TaskCreate/TaskUpdate` - Track work

### Timeline

**Speed**: FAST (parallel execution)

**Scaling**:
- N tasks in ~1 task time (with overhead)
- Operation Multi-Variant: 14 tasks in ~18 hours vs 35+ hours sequential
- Efficiency: ~50% of sequential time

**Duration factors**:
- Commander personality (aggressive 0.5x, methodical 1.5x baseline)
- Task complexity
- Quality gate time (add 10-20%)

### Example: Operation Multi-Variant Deployment

**Campaign**: Deploy 14 website variants
**Team**: Montgomery (lead), Bedell Smith (CoS), 14 front commanders, 3 validators
**Outcome**: 14/14 deployed in ~18 hours, 100% quality pass
**Lessons**: HALT/RESUME protocol critical, sample-based testing sufficient

See [docs/LESSONS-LEARNED.md](./LESSONS-LEARNED.md) for detailed case study.

---

## Pattern 2: Sequential Pipeline (Dependencies) {#sequential}

### When to Use

✅ **Perfect for**:
- Tasks with dependencies (output of Task A → input for Task B)
- Assembly-line workflow
- Quality gates between phases

❌ **Not for**:
- Independent tasks (use Parallel pattern - much faster)

### Structure

```
Team Lead (1)
├─ Phase 1: Research Commander (1)
├─ Phase 2: Planning Commander (1)
├─ Phase 3: Implementation Commanders (N)
├─ Phase 4: Testing Commander (1)
└─ Phase 5: Deployment Commander (1)
```

**Phase Flow**:
1. Research phase completes → outputs findings
2. Planning phase uses findings → outputs plan
3. Implementation phase uses plan → outputs deliverables
4. Testing phase validates deliverables → outputs test results
5. Deployment phase deploys validated deliverables

### Coordination

**Handoff Protocol**:
```
Phase N completes
  ↓
Deliverable verified by Team Lead
  ↓
Phase N+1 receives deliverable and begins
  ↓
No parallel work between sequential phases
```

**Critical**: Each phase MUST complete before next begins (prevent rework)

### Timeline

**Speed**: SLOW (sequential bottleneck)

**Duration**: N phases × average phase duration

**When to accept slowness**:
- Later phases genuinely depend on earlier work
- Rework cost would exceed sequential overhead
- Complex projects requiring staged approach

---

## Pattern 3: Swarm (Collaborative) {#swarm}

### When to Use

✅ **Perfect for**:
- Single complex deliverable requiring multiple perspectives
- Commanders collaborate on same artifact
- Need diverse expertise on one problem

❌ **Not for**:
- Independent deliverables (use Parallel pattern)
- Sequential tasks (use Sequential pattern)

### Structure

```
Team Lead (1)
└─ Specialist Commanders (3-5) - Collaborate on single deliverable
    ├─ Military Strategy (Patton, Marshall)
    ├─ Technical Architecture (Hopper, Rickover)
    └─ Political Coordination (Eisenhower, Montgomery)
```

**Collaboration Model**:
- All commanders work on same document/deliverable
- Regular sync meetings to align perspectives
- Team Lead resolves conflicts between approaches

### Coordination

**Sync Protocol**:
```
Daily standups:
  - Each specialist reports progress
  - Conflicts raised and resolved
  - Next 24 hours planned

Team Lead role:
  - Balance competing perspectives
  - Make final decisions on approach
  - Ensure coherent deliverable
```

**Tools**: Same as Parallel pattern + shared workspace (Google Docs, Git branch)

### Timeline

**Speed**: MEDIUM (collaboration overhead)

**Duration**: Single task time × 1.5 (collaboration tax)

**Tradeoff**: Slower than single commander, but higher quality from diverse expertise

---

## Team Structure Guidance

### Minimal Team (Small Campaign)

```
You (acting as Team Lead)
└─ 1-3 Commanders (execute tasks)
```

**When**: <5 tasks, <3 day duration, low complexity

**Coordination**: You manage everything directly

---

### Standard Team (Medium Campaign)

```
Team Lead (You or Montgomery)
├─ Chief of Staff (Bedell Smith) - Daily ops
├─ Front Commanders (3-10) - Execute tasks
└─ Quality Validators (2-3) - Test after completion
```

**When**: 5-20 tasks, 3-10 day duration, medium complexity

**Coordination**: Chief of Staff handles daily ops, you make strategic decisions

---

### Large Team (Major Campaign)

```
Team Lead (Montgomery, Eisenhower)
├─ Chief of Staff (Bedell Smith) - Operations coordination
├─ Intelligence (Layton) - Analytics, metrics, reporting
├─ Logistics (Marshall) - Resource allocation, dependencies
├─ Front Commanders (10-20) - Parallel execution
├─ Quality Validators (3-6) - Multi-track testing
└─ Communications (Ogilvy) - Stakeholder updates, documentation
```

**When**: 20+ tasks, 10+ day duration, high complexity

**Coordination**: Full staff structure, you focus on strategic decisions only

---

## Quality Gates

### Gate 1: Build Validation

**Purpose**: Verify code compiles, dependencies resolve, no syntax errors

**Who**: Technical validator (Moreell, Rickover)

**Process**:
1. All deployments complete
2. Validator attempts build on each deliverable
3. Reports: Pass/Fail per deliverable + error details

**Pass Criteria**: 100% build success

**Sample Size**: Test all (builds are fast)

---

### Gate 2: Functional Testing

**Purpose**: Verify features work as specified

**Who**: Methodical tester (Layton, Spruance)

**Process**:
1. Sample testing (representative subset)
2. Test categories: Navigation, content accuracy, responsive design, accessibility, performance
3. Reports: Pass/Fail per category

**Pass Criteria**: 100% test pass rate

**Sample Size**:
- Small campaigns (<5): Test all
- Medium (5-20): Test 30-50%
- Large (>20): Test 20-30%

**Lesson from Operation Multi-Variant**: 36% sample (5/14 variants), 100% pass rate - sample-based testing sufficient

---

### Gate 3: Brand/Content Consistency

**Purpose**: Verify content accuracy, voice consistency, brand standards

**Who**: Brand expert (Ogilvy) or domain validator

**Process**:
1. Spot-check sample for:
   - Factual accuracy (no false claims)
   - Voice consistency (matches intended personality)
   - Brand standards (logos, colors, tone)
2. Reports: Pass/Fail per deliverable + issues found

**Pass Criteria**: 100% brand consistency

**Sample Size**: 30-50% spot-check

---

## Commander Assignment Strategy

### Match Personality to Role

**Team Lead**:
- **Large campaigns**: Montgomery (multi-force coordination)
- **Coalition campaigns**: Eisenhower (diplomatic coordination)
- **Technical campaigns**: Marshall (logistics & organization)

**Chief of Staff**:
- Bedell Smith (unglamorous excellence, detail-obsessed)

**Front Commanders (Aggressive Tasks)**:
- Patton, Halsey, MacArthur (speed, breakthrough)

**Front Commanders (Methodical Tasks)**:
- Spruance, Bradley, Nimitz (precision, validation)

**Front Commanders (Technical Tasks)**:
- Hopper, Rickover, Groves (technical depth)

**Quality Validators**:
- Build: Moreell, Rickover (engineering rigor)
- Functional: Layton, Spruance (methodical testing)
- Brand: Ogilvy (content standards)

---

## Error Handling

### Commander Not Responding

**Diagnosis**:
1. Check inbox: Did they receive the task?
2. Check task assignment: Is task clear?
3. Check blockers: Are they waiting on something?

**Resolution**:
- If waiting for orders: Send explicit instructions (HALT/RESUME protocol)
- If blocked: Remove blocker or reassign task
- If unclear task: Clarify and restate mission

**Most Common**: Waiting for explicit RESUME after HALT (see LESSONS-LEARNED.md)

### Quality Gate Failures

**Protocol**:
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

**Don't**:
- Assign fixes to different commander (context loss)
- Skip re-validation after fixes
- Proceed to next phase with open issues

### Scope Creep

**Prevention**:
- Clear task definitions upfront
- "Done" criteria specified per task
- Review aggressive commanders (may add features)

**Detection**:
- Deliverable larger than specified
- Timeline extends beyond estimate
- Commander adding "improvements" not requested

**Resolution**:
- Accept if valuable
- Trim if excessive
- Redirect to original spec

---

## Success Metrics

### Campaign-Level

- **Delivery Rate**: Tasks completed / Tasks assigned
- **Quality Rate**: Quality gates passed / Quality gates attempted
- **Timeline Accuracy**: Actual duration / Estimated duration
- **Coordination Efficiency**: Blockers resolved / Blockers raised

### Commander-Level

- **Speed**: Tasks completed per day
- **Quality**: First-time quality pass rate
- **Collaboration**: Messages sent/received ratio
- **Autonomy**: Questions asked per task (lower = more autonomous)

**Use metrics to**:
- Award XP (high performers get bonuses)
- Improve estimates (learn actual vs estimated duration)
- Refine assignments (match commanders to roles better)

---

## Full Campaign Workflow

1. **Plan Campaign**
   - Define goals, break into tasks
   - Choose pattern (Parallel/Sequential/Swarm)
   - Choose team structure (Minimal/Standard/Large)

2. **Match Commanders**
   - Use `/generals:match-commander-to-task` for each role
   - Verify personality fit

3. **Spawn Team**
   - Use `TeamCreate` for structure
   - Use `/generals:spawn-commander` for each member
   - Establish communication channels

4. **Execute Campaign**
   - Apply coordination pattern
   - Use HALT/RESUME protocol as needed
   - Daily standups if >3 days

5. **Quality Gates**
   - Run validation after completion
   - Fix issues, re-validate
   - 100% pass required

6. **Award Experience**
   - Use `/generals:award-experience` for each commander
   - Document lessons learned
   - Commit to GitHub

7. **Campaign Retrospective**
   - What worked? What failed?
   - Update patterns with new lessons
   - Improve future campaigns
