# Output Format Examples

Detailed output format examples for all Generals skills.

---

## spawn-commander Output

### Example 1: Perfect Match (Aggressive Task + Aggressive Commander)

```
TASK ANALYSIS
═══════════════════════════════════════════════════════════════
Task: Deploy brutal variant with aggressive copy and bold CTA

Requirements Detected:
• Pace: Fast
• Style: Bold/Aggressive
• Domain: Marketing/Creative
• Complexity: Medium
• Risk: Medium

COMMANDER SELECTED
═══════════════════════════════════════════════════════════════

Commander: General George S. Patton Jr.
Personality Fit: ⭐⭐⭐⭐⭐ (5/5)
Historical Role: Third Army Commander, rapid advance across Europe

WHY PATTON:
• Aggressive execution matches aggressive content requirement
• Bold decision-making aligns with bold CTA requirement
• Speed of execution fits tight timeline

HISTORICAL PARALLEL:
Third Army advanced 600 miles in 6 months across Europe (1944-1945)
→ This task requires similar breakthrough speed and bold execution

WHAT TO EXPECT:
✅ Immediate action (will start without extensive planning)
✅ Bold choices (prefers impact over subtlety)
⚠️ May skip review steps in favor of speed
💬 Communication: Direct, forceful, impatient with delays

SPAWN PROMPT READY
═══════════════════════════════════════════════════════════════
Use Task tool with generated prompt to deploy Patton.
```

### Example 2: Mismatch Warning

```
⚠️ PERSONALITY MISMATCH WARNING
═══════════════════════════════════════════════════════════════

Commander: General George S. Patton Jr.
Task: Validate trust variant for accuracy

MISMATCH ANALYSIS:
❌ Task requires: Methodical, careful, precise validation
❌ Patton excels at: Fast, aggressive, breakthrough execution
⚠️ Risk: Patton may rush validation, miss subtle issues

RECOMMENDATION: Consider Admiral Spruance instead
• Methodical, thorough validator
• "The Quiet Warrior" - perfect for trust variant
• Won Midway through calculated precision

Proceed anyway? Task tool invocation generated, but consider better-matched commander.
```

---

## match-commander-to-task Output

```
TASK ANALYSIS
═══════════════════════════════════════════════════════════════
Task: Write technical white paper on enterprise EDR deployment

Requirements Detected:
• Pace: Methodical (accuracy critical)
• Style: Measured, professional
• Domain: Technical/Security
• Complexity: High
• Risk: Low (reputation risk if inaccurate)

RECOMMENDED COMMANDERS
═══════════════════════════════════════════════════════════════

🥇 BEST MATCH: Rear Admiral Grace Hopper
Personality Fit: ⭐⭐⭐⭐⭐ (5/5)
Domain Expertise: Computer science pioneer, technical writing
Past Success: 3 technical documentation deployments, 100% accuracy

Why Hopper:
• Technical precision matches accuracy requirement
• Invented COBOL - understands enterprise technical communication
• Known for translating complex topics for non-technical audiences

What She'll Excel At:
• Technical accuracy (will verify every claim)
• Clear explanations for CISO audience (non-technical executives)
• Structured documentation (pioneered software documentation practices)

Watch For:
• May over-explain concepts (valuable for audience, but watch length)

Expected Approach: Thorough research → structured outline → precise writing
Timeline: Medium (methodical but efficient)

---

🥈 ALTERNATIVE 1: Admiral Hyman Rickover
Personality Fit: ⭐⭐⭐⭐ (4/5)
Domain Expertise: Nuclear engineering, technical standards, quality obsession

Why Rickover:
• Extreme quality standards (nuclear submarine safety record)
• Technical depth (understands complex systems)
• Known for documentation rigor

What He'll Excel At:
• Zero tolerance for errors
• Deep technical validation
• Standards compliance

Watch For:
• May be overly critical (perfection can slow delivery)
• Less accessible writing style than Hopper

---

🥉 ALTERNATIVE 2: Admiral Raymond Spruance
Personality Fit: ⭐⭐⭐ (3/5)
Domain Expertise: Strategic analysis, methodical validation

Why Spruance:
• Methodical approach matches accuracy requirement
• Calm, measured communication fits professional tone
• Strategic thinking aligns with enterprise positioning

What He'll Excel At:
• Accuracy validation
• Measured, authoritative tone
• Strategic framing

Watch For:
• Less technical depth than Hopper/Rickover
• May need technical review from specialist

═══════════════════════════════════════════════════════════════
RECOMMENDATION: Use Hopper for technical accuracy + audience accessibility

Next: /generals:spawn-commander hopper "Write enterprise EDR white paper"
```

---

## award-experience Output

```
═══════════════════════════════════════════════════════════════
GENERALS: AWARD EXPERIENCE
═══════════════════════════════════════════════════════════════

Commander: Rear Admiral Grace Hopper
Deployment: Enterprise EDR Technical White Paper

EXPERIENCE AWARDED
═══════════════════════════════════════════════════════════════
XP: +125
  • Base: 100 (complex technical task)
  • Bonus: +25 (lessons learned documented)

Total XP: 450 → 575
Deployments: 3 → 4

COMPETENCE PROGRESS
═══════════════════════════════════════════════════════════════
Category: Technical Documentation
Progress: 3/10 → 4/10
████░░░░░░ 4/10 to ⭐

Next milestone: 6 more deployments to earn ⭐ (Competent)

PROFILE UPDATED
═══════════════════════════════════════════════════════════════
✅ Deployment history added (Deployment 4)
✅ XP updated
✅ Competence progress incremented
✅ Behavioral observations documented
✅ Lessons learned captured

COMMITTED TO GITHUB
═══════════════════════════════════════════════════════════════
Commit: a3f9c21
Branch: master
Remote: Pushed to origin

Self-learning cycle complete. Commander profile now includes this
deployment experience for future reference.

═══════════════════════════════════════════════════════════════
```

---

## campaign-coordinator Output

### Pattern Selection Guidance

```
CAMPAIGN PATTERN RECOMMENDATION
═══════════════════════════════════════════════════════════════

Your Campaign: Deploy 14 website variants with unique positioning

Analysis:
• Tasks: 14 independent fronts (no dependencies)
• Complexity: Medium (3 pages per variant)
• Timeline: Tight (want fast delivery)
• Coordination: Minimal cross-dependencies

RECOMMENDED PATTERN: Parallel Execution
═══════════════════════════════════════════════════════════════

Structure:
Team Lead (1) - You or Montgomery
├─ Chief of Staff (1) - Bedell Smith (daily ops)
├─ Front Commanders (14) - One per variant
└─ Quality Validators (3) - Post-deployment testing

Timeline: ~18-24 hours (vs 35+ hours sequential)
Scaling Efficiency: ~50% of sequential time

Critical Protocols:
⚠️ HALT/RESUME: If blocking issue, send explicit RESUME after resolution
✅ Quality Gates: Run after all fronts complete (build, functional, brand)

Next Steps:
1. Use /generals:match-commander-to-task for each variant
2. Spawn commanders using /generals:spawn-commander
3. Coordinate using SendMessage for blockers
4. Run quality gates after completion
5. Award experience to all commanders

See docs/LESSONS-LEARNED.md#halt-resume for critical protocol details.
```

---

## General Output Principles

All skills follow this structure:
1. **Analysis** - What was requested, what was detected
2. **Recommendation** - Best approach with rationale
3. **What to Expect** - Set realistic expectations
4. **Next Steps** - Clear action items
5. **References** - Links to detailed docs for deep dives

Compact output in skills, detailed examples in this doc.
