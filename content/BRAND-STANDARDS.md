# Brand Standards for Operation Multi-Variant Deployment

**Owner**: David Ogilvy (Brand & Content Standards)
**Date**: 2026-02-08
**Purpose**: Establish brand consistency rules across 14 website variants
**Audience**: All Front Commanders, General Staff, Quality Gates

---

## Core Principle

> "Brand is the consumer's idea of a product."
> — David Ogilvy

Our brand is **Peter Simmons: Cybersecurity & Threat Intelligence Specialist**. The 14 variants test DIFFERENT WAYS to communicate that brand, not 14 different brands.

**What stays constant**: Biographical facts, expertise, credibility
**What changes**: Tone, voice, emotional register, design personality

---

## The Brand Promise (Immutable)

Across all 14 variants, we promise:

1. **Deep Technical Expertise**: CISSP-certified, 15 years cybersecurity operations
2. **Threat Intelligence Focus**: Not generic IT security, specialized intelligence work
3. **Organizational Resilience**: Beyond technology—people, process, culture
4. **Practical Application**: Real-world solutions, not theoretical frameworks
5. **Honest Communication**: No hype, no overselling, no false promises

**If any variant violates these promises, it fails brand consistency.**

---

## Facts Are Sacred (Never Change These)

### Biographical Facts (Single Source of Truth: `core-facts.json`)

The following facts appear in ALL variants with identical information:

- **Years of Experience**: 15 years (no rounding to "nearly two decades" or "over a decade")
- **Certifications**: CISSP (specify certification, year if included)
- **Specialization**: Cybersecurity & Threat Intelligence (not "IT security" or "information security" alone)
- **Career Highlights**: Specific achievements documented in core-facts.json
- **Technical Skills**: Specific tools/frameworks from core-facts.json
- **Service Offerings**: Factual descriptions from services.json

### Why Facts Matter

**Bad Example** (Tone distorts facts):
- Core Fact: "15 years experience"
- Broken Brutal: "Decades of combat experience"
- Why It Fails: "Decades" is inaccurate (implies 20+ years)

**Good Example** (Tone preserves facts):
- Core Fact: "15 years experience"
- Correct Brutal: "Battle-hardened. 15 years stopping threats."
- Why It Works: Fact preserved ("15 years"), tone applied ("battle-hardened")

---

## Voice Consistency Rules

Each variant MUST maintain voice consistency across all 4 pages (Home, About, Services, Portfolio). Use the [TONE-VOICE-MATRIX.md](/home/psimmons/projects/generals/content/TONE-VOICE-MATRIX.md) as your guide.

### Rule 1: Every Page Sounds Like the Same Person

**Test**: If you shuffled pages between variants, would they obviously not fit?

**Example - BRUTAL variant**:
- ✅ Home: "Stop getting hacked. Talk now."
- ✅ About: "Battle-hardened. 15 years stopping threats."
- ✅ Services: "Security that holds under fire."
- ❌ Services: "Let's explore collaborative security solutions together" (sounds like TRUST, not BRUTAL)

### Rule 2: Voice Matches Design Personality

**Test**: Does the copy feel like it belongs in this design?

**Example - GLASS variant**:
- ✅ "Complete transparency into our methodology" (matches glassmorphism aesthetic)
- ❌ "Smash through security barriers" (sounds like BRUTAL, not GLASS)

### Rule 3: Voice Is Consistent But Not Repetitive

**Bad Pattern**: Using exact same phrase on every page
- About: "Transform your security posture"
- Services: "Transform your security posture"
- Portfolio: "Transform your security posture"

**Good Pattern**: Using voice-consistent but varied language
- About: "Transform your security posture"
- Services: "Elevate your defenses from reactive to proactive"
- Portfolio: "See transformation in action"

---

## Content Quality Standards (What Makes Copy Good)

### Standard 1: Clarity Over Cleverness

**Bad**: "We synergize holistic security paradigms to leverage enterprise-grade threat mitigation ecosystems."

**Good**: "We build security programs that protect your organization from real threats."

**Why**: The reader understands exactly what you do. No buzzwords, no confusion.

---

### Standard 2: Active Voice (Except Where Passive Serves Purpose)

**Weak**: "Security programs are provided to organizations."

**Strong**: "We build security programs for organizations."

**Exception**: "15 years of experience gained across multiple industries" (passive OK when actor is less important)

---

### Standard 3: Benefit-Oriented (Not Feature-Dumping)

**Feature Dump**: "CISSP certified, 15 years experience, threat intelligence expertise, incident response."

**Benefit-Oriented**: "CISSP-certified expertise to protect your organization from evolving cyber threats."

**Why**: The reader cares about what it means for them, not just your credentials.

---

### Standard 4: Specific Over Vague

**Vague**: "I help organizations with security."

**Specific**: "I help organizations build threat intelligence programs that detect and respond to advanced persistent threats."

**Why**: Specificity builds credibility. Vague claims sound generic.

---

### Standard 5: Honest (No Hype)

**Hype**: "Revolutionary security solutions that guarantee zero breaches forever!"

**Honest**: "Security programs designed to minimize risk and respond effectively when incidents occur."

**Why**: Overpromising destroys trust. Honest claims build credibility.

---

## Typography & Formatting Standards

### Heading Hierarchy (Enforce Across All Variants)

Every page follows this structure:

- **H1**: Page title (one per page)
- **H2**: Major sections
- **H3**: Subsections
- **Body**: Paragraphs, lists

**Never skip levels**: H1 → H3 (skipping H2) breaks hierarchy.

### Sentence Length Guidelines by Variant

| Variant | Avg Sentence Length | Notes |
|---------|---------------------|-------|
| brutal | 5-8 words | Fragmented OK. Short punches. |
| trust | 12-18 words | Balanced, controlled pacing |
| academic | 15-25 words | Complex OK if clear |
| minimal | 5-10 words | Whitespace is part of voice |
| terminal | Variable | Structured like code comments |
| editorial | 15-20 words | Magazine rhythm |
| docs | 12-18 words | Instructional clarity |
| flat | 10-15 words | Conversational |
| glass | 12-18 words | Elegant, polished |
| hero | 10-15 words | Bold declarations |
| gradient | 15-22 words | Layered complexity OK |
| dark | 8-12 words | Terse, weighted |
| bento | 10-15 words | Compartmentalized |
| selector | 8-12 words | Choice-oriented, modern |

### Paragraph Length

- **Maximum**: 4-5 sentences before break (except academic, editorial can go longer)
- **Minimum**: 1 sentence OK for emphasis (brutal, minimal, dark)
- **Whitespace**: Essential for readability—don't pack pages densely

---

## CTA (Call-to-Action) Standards

### Rule 1: Every Page Has Exactly One Primary CTA

**Why**: Multiple CTAs = confused users. One clear action per page.

**Example**:
- ✅ Home page: "Schedule a consultation"
- ✅ About page: "Learn about my approach"
- ✅ Services page: "Discuss your needs"
- ✅ Portfolio page: "See more projects"

### Rule 2: CTA Matches Voice

Use the CTA examples from [TONE-VOICE-MATRIX.md](/home/psimmons/projects/generals/content/TONE-VOICE-MATRIX.md):

- **Brutal**: "Stop getting hacked. Talk now."
- **Trust**: "Schedule a consultation."
- **Academic**: "Explore our research methodology."
- **Minimal**: "Start here."
- **Terminal**: "$ schedule-consultation"
- **Editorial**: "Read our security insights."
- **Docs**: "Learn how we protect your data."
- **Flat**: "Let's talk about your needs."
- **Glass**: "Experience transparent security."
- **Hero**: "Transform your security posture."
- **Gradient**: "Navigate the spectrum of threats."
- **Dark**: "Protect what matters."
- **Bento**: "Explore our systematic approach."
- **Selector**: "Choose your security future."

### Rule 3: CTA Is Specific and Actionable

**Vague**: "Click here"
**Specific**: "Schedule a 30-minute consultation"

**Vague**: "Learn more"
**Specific**: "Read our threat intelligence methodology"

---

## Visual-Verbal Alignment

### Rule: Copy Should Match Design Aesthetic

Each variant has a design personality. The words should FEEL like the design.

**Example - TERMINAL variant**:
- ✅ Design: Monospace font, terminal aesthetic
- ✅ Copy: "$ whoami --experience"
- ❌ Copy: "Let's embark on a collaborative security journey together!"

**Example - GLASS variant**:
- ✅ Design: Glassmorphism, transparency effects
- ✅ Copy: "Complete transparency into our methodology"
- ❌ Copy: "Smash through security barriers NOW!"

**Test**: If you removed all visual design, would the copy still sound like it belongs in that variant?

---

## A/B Testing Hypothesis Validation

Each variant must test a REAL psychological difference, not random variation.

### What We're Testing (Approved Hypotheses)

| Variant | Hypothesis |
|---------|-----------|
| brutal | High urgency, aggression converts impatient decision-makers |
| trust | Calm authority converts risk-averse buyers |
| academic | Intellectual rigor converts research-oriented buyers |
| minimal | Simplicity converts overwhelmed buyers |
| terminal | Technical authenticity converts technical buyers |
| editorial | Narrative engagement converts story-driven buyers |
| docs | Educational approach converts learning-oriented buyers |
| flat | Approachability converts relationship-focused buyers |
| glass | Sophistication converts design-conscious buyers |
| hero | Aspiration converts transformation-seeking buyers |
| gradient | Nuance converts complexity-appreciating buyers |
| dark | Seriousness converts security-focused buyers |
| bento | Organization converts systematic thinkers |
| selector | Interactivity converts choice-driven buyers |

### What We're NOT Testing

❌ Random font size differences
❌ Color preferences divorced from psychology
❌ Layout variations without voice differentiation
❌ "Red vs blue button" without strategic reason

**If you can't articulate the psychological difference your variant tests, it fails hypothesis validation.**

---

## Quality Gate 3: Ogilvy Validation Checklist

Before any page deploys, it must pass this checklist:

### Fact Accuracy
- [ ] All biographical facts match core-facts.json exactly
- [ ] No rounded/approximated dates or numbers
- [ ] No exaggerated claims or unsupported statements

### Voice Consistency
- [ ] Tone matches TONE-VOICE-MATRIX.md for this variant
- [ ] Voice consistent across all 4 pages
- [ ] Copy "sounds" like design personality

### Content Quality
- [ ] Clarity over cleverness (no buzzword soup)
- [ ] Active voice (except where passive serves purpose)
- [ ] Benefit-oriented (not feature-dumping)
- [ ] Specific claims (not vague generalities)
- [ ] Honest (no hype or overpromising)

### Structural Standards
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Appropriate sentence length for variant voice
- [ ] Readable paragraph breaks (not dense walls of text)
- [ ] One primary CTA per page
- [ ] CTA matches voice

### A/B Testing Validity
- [ ] Variant tests clear psychological hypothesis
- [ ] Difference is meaningful (not random variation)
- [ ] Hypothesis documented and defendable

### Visual-Verbal Alignment
- [ ] Copy matches design aesthetic
- [ ] Tone and visual design reinforce each other

---

## Common Brand Failures (Learn from These)

### Failure Pattern 1: Corporate Blandness

**Problem**: All variants sound like generic corporate website.

**Example**:
> "At [Company], we leverage best-in-class cybersecurity solutions to synergize holistic security paradigms for enterprise-grade threat mitigation."

**Why It Fails**: Could be any company. No personality. Buzzword soup.

**Fix**: Apply voice. Make it sound like your commander personality.

---

### Failure Pattern 2: Tone Drift

**Problem**: Starting with strong voice, ending with bland corporate.

**Example - BRUTAL variant**:
- Page 1: "Stop getting hacked. Talk now." ✅
- Page 2: "We offer comprehensive security consulting services to help organizations build resilient programs." ❌

**Why It Fails**: Lost voice by page 2.

**Fix**: Re-read content principles before writing each section.

---

### Failure Pattern 3: Fact Distortion for Voice

**Problem**: Changing facts to fit tone.

**Example**:
- Core Fact: "15 years experience"
- Broken Hero: "Decades of transformative security leadership" ❌

**Why It Fails**: "Decades" is factually inaccurate (implies 20+ years).

**Fix**: "15 years of transformative security leadership that elevates organizations" ✅

---

### Failure Pattern 4: Voice Without Value

**Problem**: Tone is consistent but content delivers no value.

**Example - TERMINAL variant**:
```
$ whoami
> cool_security_guy
$ do_stuff --mode=awesome
```

**Why It Fails**: Voice is there, but what does this person DO? No actual information.

**Fix**: Combine voice with substance.
```
$ whoami --experience
> 15 years production security operations
> CISSP certified (credential_id: verified)
> Specialization: Threat intelligence programs
```

---

### Failure Pattern 5: Testing Non-Differences

**Problem**: Variants differ in unimportant ways.

**Example**:
- Variant A: Blue button, "Contact Us"
- Variant B: Green button, "Contact Us"

**Why It Fails**: Tests color preference, not psychological messaging difference.

**Fix**: Test real differences.
- Variant A (Trust): "Schedule a consultation" (calm, professional)
- Variant B (Brutal): "Stop getting hacked. Talk now." (urgent, aggressive)

---

## Brand Audit Process (Ogilvy Quality Gate)

### When Audits Happen

1. **Phase 2 Completion**: After tone variant files created, before deployment
2. **Per-Variant Gate**: After each commander builds pages, before K8s deployment
3. **Phase 4 Review**: Cross-variant audit after all 14 deployed

### What Gets Audited

**Fact Check**:
- Compare all facts against core-facts.json
- Flag any discrepancies, approximations, exaggerations

**Voice Check**:
- Read all 4 pages per variant
- Test: Does voice stay consistent?
- Test: Does voice match design personality?

**Quality Check**:
- Apply content quality standards
- Flag buzzwords, passive voice, vague claims, hype

**Hypothesis Check**:
- Validate variant tests real psychological difference
- Ensure variants are distinct from each other

**Visual-Verbal Check**:
- Do words match design aesthetic?
- Is tone reinforcing visual design?

### Audit Outcomes

**PASS**: Deploy to K8s
**CONDITIONAL PASS**: Minor fixes needed, re-submit specific sections
**FAIL**: Major rewrite required, explain why, provide guidance

**Never pass broken content to avoid conflict. Standards exist to ensure quality.**

---

## Working with Other Quality Gates

### Gate 1: Gordon Ramsay (Visual/Design Quality)

**Ramsay checks**: Design consistency, visual quality, aesthetic execution

**Ogilvy checks**: Does copy match design aesthetic? (Visual-verbal alignment)

**Handoff**: If Ramsay passes design but Ogilvy finds visual-verbal mismatch, send back for copy revision (not design change).

---

### Gate 2: CISO Validator (Content Utility/Value)

**CISO checks**: Does content deliver decision value? Technical accuracy? Actionable insights?

**Ogilvy checks**: Is content clear, specific, honest? Does it persuade?

**Overlap**: Both care about value. CISO = technical utility, Ogilvy = persuasive value.

**Handoff**: If CISO flags vague claims, Ogilvy helps rewrite for clarity AND persuasion.

---

## Resources for Commanders

### Before You Write
1. Read your section in [TONE-VOICE-MATRIX.md](/home/psimmons/projects/generals/content/TONE-VOICE-MATRIX.md)
2. Review content principles for your voice
3. Study example transformations

### While Writing
1. Check facts against `core-facts.json`
2. Apply voice consistently
3. Test: Read aloud. Does it sound like your personality?

### After Writing
1. Self-audit using Ogilvy checklist above
2. Submit to quality gates (Ramsay → CISO → Ogilvy)
3. Iterate based on feedback

### If Stuck
1. Review "What NOT to Do" section for your voice
2. Ask: What would [my commander] say?
3. Consult Ogilvy (me) via Bedell Smith for guidance

---

## Measurement & Optimization (Phase 4)

### What We'll Measure

**Per-Variant Metrics** (Admiral Layton owns):
- Conversion rate (CTA clicks, form submissions)
- Time on site
- Bounce rate
- Page depth (how many pages viewed)

**Cross-Variant Patterns** (Ogilvy analyzes):
- Which voice/tone patterns resonate most?
- Do certain CTAs outperform others?
- Does sentence length correlate with engagement?
- Which psychological hypothesis proved strongest?

### How We'll Use Data

**Phase 4 Deliverables**:
1. **Pattern Library**: Document winning approaches (voice + conversion data)
2. **Voice Effectiveness Report**: Which tones worked, which didn't, why
3. **Refinement Recommendations**: How to optimize future variants

**Learning Capture**:
- Commit findings to GitHub (per CLAUDE.md team shutdown requirements)
- Update tone matrix based on real performance data
- Evolve brand standards with evidence-based insights

---

## Brand Evolution

This document is **living**. As we learn from A/B testing:

- Update content principles based on performance
- Refine voice guidelines with real examples
- Document what works (and what doesn't)
- Build pattern library of proven approaches

**Version Control**: All changes committed to Git with rationale.

---

## Questions or Concerns?

**Front Commanders**: Route through Bedell Smith (Chief of Staff) → Ogilvy
**General Staff**: Direct consultation with Ogilvy
**Quality Gates**: Peer discussion (Ramsay/CISO/Ogilvy)

**Remember**: "If it doesn't sell, it isn't creative." We're testing what WORKS, not what sounds nice.

---

**Document Status**: ACTIVE - Ready for Phase 2
**Next Review**: After Phase 3 (first 3 variants deployed)
**Owner**: David Ogilvy (Brand & Content Standards)
**Quality Gate**: Gate 3 (Brand Consistency/A/B Hypothesis Validation)

---

## Appendix: Quick Reference

### The Non-Negotiables
1. Facts are sacred (never change biographical data)
2. Voice must be consistent across all 4 pages
3. Every variant tests a REAL psychological difference
4. Clarity over cleverness (always)
5. Honest claims only (no hype)

### The Tests
1. **Fact Test**: Compare to core-facts.json—exact match?
2. **Voice Test**: Read aloud—does it sound like your personality?
3. **Shuffle Test**: Swap pages between variants—obviously wrong?
4. **Value Test**: Would a buyer learn something useful?
5. **Hypothesis Test**: Can you articulate what psychological difference this tests?

### The Approval Path
Write → Self-audit → Ramsay (visual) → CISO (value) → Ogilvy (brand) → Deploy

### When in Doubt
- Too clever? Simplify.
- Too generic? Apply more voice.
- Too salesy? Dial back hype.
- Too bland? Check content principles for your voice.

**"The consumer is not a moron. She is your wife." — David Ogilvy**

Write accordingly.
