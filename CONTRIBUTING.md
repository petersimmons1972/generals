# Contributing to Generals

Thank you for considering contributing to Generals! This document explains how to share your campaign lessons and improvements with the community.

---

## What Makes a Good Contribution

### **✅ We Welcome:**

1. **Novel Campaign Lessons**
   - New coordination patterns that worked
   - Failure modes not yet documented
   - Commander personality insights from real deployments
   - Protocol improvements (like HALT/RESUME)

2. **Commander Profile Improvements**
   - Better personality descriptions
   - Historical context additions
   - Behavioral observations from deployments
   - XP/competence system refinements

3. **New Commanders**
   - Other historical figures (military, business, technical leaders)
   - Well-researched personality profiles
   - Distinct traits different from existing commanders

4. **Skill Enhancements**
   - Better prompts for spawn-commander
   - New coordination patterns for campaign-coordinator
   - Improved matching algorithms
   - Bug fixes and clarity improvements

5. **Documentation**
   - Better examples
   - Clearer explanations
   - New use cases
   - FAQ additions

### **❌ Please Avoid:**

1. **Campaign-Specific Details Without Generalizable Lessons**
   - "We deployed 14 websites" → Not useful alone
   - "Parallel execution prevents conflicts" → Useful lesson

2. **Sensitive Information**
   - Client names, proprietary data, confidential strategies
   - Trade secrets or competitive intelligence
   - Personal information about real people

3. **Unsubstantiated Claims**
   - "This always works" without evidence
   - Lessons contradicting existing knowledge without justification
   - Theoretical patterns without real deployment validation

4. **Low-Quality Additions**
   - Typo-only fixes (unless substantial)
   - Formatting changes without content improvement
   - Duplicate lessons already documented

---

## How to Contribute

### **Step 1: Document Your Lesson**

After completing a campaign, create a service record using the template:

```bash
cp templates/SERVICE-RECORD-TEMPLATE.md SERVICE-RECORD-YOUR-CAMPAIGN-NAME.md
# Fill in your campaign details, lessons learned, what worked/failed
```

**Be specific:**
- ✅ "HALT broadcasts must be followed by explicit RESUME for methodical commanders"
- ❌ "Communication is important"

**Provide evidence:**
- ✅ "Tested with Spruance - waited 10 hours for explicit order"
- ❌ "I think this might work"

### **Step 2: Update Relevant Files**

If your lesson affects:
- **Commander profiles**: Update `profiles/<commander>.md` with behavioral observations
- **Skills**: Update `skills/<skill-name>.md` with new patterns
- **README**: Add examples if it's a major lesson

### **Step 3: Commit to Your Fork**

```bash
git add SERVICE-RECORD-YOUR-CAMPAIGN-NAME.md profiles/*.md skills/*.md
git commit -m "docs: [Campaign Name] - [brief lesson summary]

[Longer description of what you learned]

Key lessons:
- [Lesson 1]
- [Lesson 2]

Evidence: [How you validated this]

Co-Authored-By: [Commander Names if applicable]
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin master
```

### **Step 4: Submit Pull Request**

1. Go to https://github.com/petersimmons1972/generals
2. Click "Pull Requests" → "New Pull Request"
3. Select your fork and branch
4. Write clear PR description:

```markdown
## Summary
[What you learned and why it matters]

## Campaign Context
- Team size: [N commanders]
- Duration: [X days]
- Pattern used: [Parallel/Sequential/Swarm]

## Key Lessons
1. [Lesson 1 with evidence]
2. [Lesson 2 with evidence]

## Files Changed
- `SERVICE-RECORD-*.md` - Campaign documentation
- `profiles/<commander>.md` - Behavioral observations
- `skills/<skill>.md` - Pattern improvements

## Testing
[How you validated these lessons]

## Questions for Reviewers
[Any uncertainties or areas needing feedback]
```

5. Submit PR and wait for review

---

## Review Process

### **What Reviewers Look For**

1. **Evidence-Based**: Are lessons backed by real deployments?
2. **Generalizable**: Can others apply this lesson?
3. **Clear**: Is it well-documented and understandable?
4. **No Conflicts**: Does it contradict existing knowledge?
5. **Quality**: Is the writing clear, formatting correct?

### **Timeline**

- Initial review: Within 7 days
- Feedback/iteration: As needed
- Merge decision: When approved by maintainer

### **Possible Outcomes**

- ✅ **Approved & Merged**: Lesson added to origin repo
- 🔄 **Changes Requested**: Reviewers suggest improvements
- ❌ **Declined**: Doesn't meet contribution criteria (with explanation)

---

## Contribution Categories

### **1. Campaign Lessons** (Most Common)

**What:** Share coordination patterns, failures, successes from your campaigns

**How:**
1. Document in service record
2. Update relevant skills/profiles
3. Submit PR with evidence

**Example PR:**
```
Title: "Campaign lesson: Outlier detection protocol"

Learned from Campaign X:
- Commander >2σ from mean completion time needs proactive diagnosis
- Don't wait for user authorization - investigate immediately
- Updated campaign-coordinator skill with outlier detection protocol
```

### **2. Commander Improvements**

**What:** Enhance existing commander profiles with new observations

**How:**
1. Deploy commander on task
2. Document behavioral observations
3. Update profile with XP, lessons, ribbons
4. Submit PR with deployment details

**Example PR:**
```
Title: "Admiral Hopper: Infrastructure analogy effectiveness"

Deployment: EDR white paper for CISOs
Observation: Infrastructure analogies (postal system) achieved 100% comprehension
Updated: Profile with "infrastructure analogy" strength
Evidence: White paper test readers, CISO feedback
```

### **3. New Commanders**

**What:** Add new historical figures as commanders

**How:**
1. Research thoroughly (biography, achievements, personality)
2. Create profile using existing format
3. Include: Historical achievements, personality traits, strengths/weaknesses, historical parallels
4. Start with 0 XP, 0 deployments (they'll earn experience through use)
5. Submit PR with research sources

**Requirements:**
- Historical figure (documented personality)
- Distinct traits (different from existing commanders)
- Rich personality data (enough for spawn prompts)
- Public domain information (no copyright issues)

**Example PR:**
```
Title: "New commander: Admiral Hyman Rickover"

Historical Role: Father of Nuclear Navy
Personality: Quality obsession, uncompromising standards
Strengths: Technical rigor, long-term thinking, mentorship
Distinct from: Patton (Rickover prioritizes safety over speed)
Sources: [Naval History publications]
```

### **4. Skill Enhancements**

**What:** Improve existing coordination skills

**How:**
1. Identify weakness in current skill
2. Propose improvement with rationale
3. Test improvement if possible
4. Submit PR with before/after comparison

**Example PR:**
```
Title: "spawn-commander: Add mismatch warning"

Problem: Users spawn wrong commander for task without realizing
Solution: Add personality-to-task mismatch detection
Before: Silent mismatch
After: Warning + recommendation for better-fit commander
Testing: Tested with Patton on methodical tasks - warning triggered correctly
```

---

## Code of Conduct

### **Be Respectful**
- Disagree with ideas, not people
- Provide constructive feedback
- Assume good intent

### **Be Evidence-Based**
- Back claims with deployment results
- Admit when uncertain
- Update views when evidence changes

### **Be Collaborative**
- Build on others' work
- Credit sources and inspiration
- Help newcomers learn the system

---

## Questions?

- **General questions**: GitHub Discussions
- **Bugs**: GitHub Issues
- **Contribution questions**: Comment on your PR or open Discussion

---

## Recognition

Contributors who submit merged PRs will be:
- Listed in README contributors section
- Credited in relevant service records
- Building the collective knowledge of the Generals community

**Thank you for making Generals better for everyone!**

---

## Quick Checklist

Before submitting PR, verify:

- [ ] Service record documented (using template)
- [ ] Lessons are evidence-based (real deployments)
- [ ] Lessons are generalizable (others can apply them)
- [ ] Relevant files updated (profiles, skills, README if major)
- [ ] Commit message follows format
- [ ] PR description clear and complete
- [ ] No sensitive information included
- [ ] Writing is clear and well-formatted
- [ ] Changes tested/validated if applicable

---

**Let's build better coordination systems together.**
