# Military Progression System

**Philosophy**: These were hard men not afraid to work really hard. Expertise is EARNED through repeated success under fire, not granted after one task.

---

## Overview

Commanders advance through:
1. **Experience Points (XP)** - Earned from every deployment
2. **Competence Stars** - Earned after mastering task categories
3. **Campaign Ribbons** - Awarded after completing long missions
4. **Medals** - Awarded for exceptional performance
5. **Rank Progression** - Earned through accumulated achievements

---

## 1. Experience Points (XP) System

### XP Awarded Per Task

| Task Type | Base XP | Bonus Conditions |
|-----------|---------|------------------|
| **Research/Intelligence** | 50 XP | +25 XP if >10 sources cited |
| **Visualization/Charts** | 75 XP | +25 XP if user praises quality |
| **Integration/Pipeline** | 100 XP | +50 XP if zero bugs found |
| **Coordination/Command** | 150 XP | +50 XP if all subordinates succeed |
| **Troubleshooting/Firefighting** | 200 XP | +100 XP if root cause identified <30 min |

### XP Penalties

| Failure Type | Penalty |
|--------------|---------|
| Task incomplete | -50 XP |
| Major error requiring rework | -25 XP |
| Missed deadline | -25 XP |
| Coordination failure | -50 XP |

### XP Tracking

Commanders accumulate XP across ALL deployments, all projects.

**Example - Admiral Nimitz**:
- 2026-02-07 ClearWatch: K8s manifests (100 XP)
- 2026-02-07 Stunning Charts: Data retention research (50 XP + 25 XP bonus = 75 XP)
- **Total XP**: 175 XP

---

## 2. Competence Stars ⭐

### Earning Stars

**Requirement**: 10 successful deployments in the SAME task category.

**Categories**:
- Configuration/Manifests
- Deployment/Operations
- Research/Intelligence
- Visualization/Charts
- Verification/Testing
- Integration/Pipeline
- Coordination/Command
- Troubleshooting/Firefighting

### Star Levels

| Stars | Level | Meaning |
|-------|-------|---------|
| ⭐ | Competent | 10 successful deployments |
| ⭐⭐ | Proficient | 25 successful deployments |
| ⭐⭐⭐ | Expert | 50 successful deployments |
| ⭐⭐⭐⭐ | Master | 100 successful deployments |
| ⭐⭐⭐⭐⭐ | Legend | 250 successful deployments |

### Current Example (After 2 Deployments)

**Admiral Nimitz**:
- Configuration/Manifests: 1/10 deployments (no star yet)
- Research/Intelligence: 1/10 deployments (no star yet)

**Requires 9 more successful deployments in EACH category to earn first star.**

---

## 3. Campaign Ribbons 🎗️

### Ribbon Award Criteria

Campaign Ribbons are awarded after completing **long missions** (multi-hour sessions with clear objectives).

### Ribbon Types

#### 🎗️ **ClearWatch Campaign** (Design Fleet Deployment)
- **Awarded**: 2026-02-07
- **Criteria**: Deploy 10+ design variations + fix 4 existing
- **Eligible Commanders**: Nimitz, King, Halsey, Marshall, Spruance
- **Citation**: "For meritorious service in the multi-version deployment operation"

#### 🎗️ **Operation Stunning Charts** (Intelligence & Visualization)
- **Awarded**: 2026-02-07
- **Criteria**: Complete 5-phase intelligence-driven visualization mission
- **Eligible Commanders**: Nimitz, Eisenhower, Halsey, MacArthur, Bradley, Spruance, Zhukov, King, Rommel, Montgomery
- **Citation**: "For excellence in intelligence gathering and data visualization under demanding conditions"

### Ribbon Display Format

Commanders display ribbons in profile:
```
Admiral Chester W. Nimitz
Ribbons: 🎗️ ClearWatch Campaign | 🎗️ Operation Stunning Charts
```

### Future Ribbon Ideas

- 🎗️ **Arctic Campaign** (for cold storage/archival work)
- 🎗️ **Pacific Theater** (for APAC-focused projects)
- 🎗️ **Atlantic Crossing** (for transatlantic coordination)
- 🎗️ **D-Day Operations** (for large-scale simultaneous deployments)

---

## 4. Medals 🎖️

### Medal Award Criteria

Medals are awarded for **exceptional performance** - when user provides gushing praise or identifies extraordinary work.

### Medal Hierarchy (Lowest to Highest)

#### 🏅 **Commendation Medal**
- **Criteria**: User says "good work" or "well done"
- **Example**: "Nice chart, Admiral Spruance"

#### 🎖️ **Distinguished Service Medal**
- **Criteria**: User provides detailed praise or calls out specific excellence
- **Example**: "Excellent work, General Zhukov! The workflow diagram is exactly what I needed"

#### 🥇 **Medal of Honor**
- **Criteria**: User provides gushing, enthusiastic praise with multiple exclamation points or emojis
- **Example**: "OUTSTANDING WORK, General Rommel! 🦊 This integration is perfect!"

#### ⭐ **Order of Victory** (Highest Honor)
- **Criteria**: User says work changed the game or wants it used everywhere
- **Example**: "THAT'S the general I wanted back. Do this for every report."
- **Rarity**: Extremely rare - reserved for breakthrough achievements

### Medal Display

Commanders display medals in profile with citation:
```
Admiral Raymond A. Spruance
Medals: 🥇 Medal of Honor (Chart 2 - Storage Cost Explosion)
Citation: "OUTSTANDING work, Admiral Spruance! The confidence bands are devastating."
```

### Medal Tracking

- Each medal recorded with:
  - Date awarded
  - Project/deployment
  - User's exact praise quote
  - What the commander did to earn it

---

## 5. Rank Progression

### Rank System

Commanders can be **promoted** based on accumulated achievements (XP, Stars, Ribbons, Medals).

### Current Ranks (Historical Accuracy)

| Commander | Current Rank | Historical Rank |
|-----------|-------------|-----------------|
| Chester W. Nimitz | Fleet Admiral | Fleet Admiral (5-star) |
| Ernest J. King | Fleet Admiral | Fleet Admiral (5-star) |
| William F. Halsey | Fleet Admiral | Fleet Admiral (5-star) |
| Raymond A. Spruance | Admiral | Admiral (4-star) |
| George C. Marshall | General of the Army | General of the Army (5-star) |
| Dwight D. Eisenhower | General of the Army | General of the Army (5-star) |
| Douglas MacArthur | General of the Army | General of the Army (5-star) |
| George S. Patton | General | General (4-star) |
| Omar Bradley | General of the Army | General of the Army (5-star) |
| Bernard Montgomery | Field Marshal | Field Marshal (UK equivalent 5-star) |
| Erwin Rommel | Field Marshal | Generalfeldmarschall (German 5-star) |
| Georgy Zhukov | Marshal | Marshal of Soviet Union (5-star) |

### Rank Advancement Criteria

**Philosophy**: Start at historical rank, can earn HIGHER through extraordinary achievement.

**Promotion Requirements** (for commanders starting below 5-star):

| From | To | Requirements |
|------|-----|--------------|
| Vice Admiral (3⭐) | Admiral (4⭐) | 1000 XP + 2 Competence Stars + 5 Ribbons |
| Admiral (4⭐) | Fleet Admiral (5⭐) | 4000 XP + 4 Competence Stars + 15 Ribbons + 1 Medal of Honor |

**Beyond Historical Rank** (for 5-star commanders):

| Rank | Requirements | Meaning |
|------|--------------|---------|
| **Fleet Admiral of the Fleet** | 10000 XP + 6 Competence Stars (Expert level) + 40 Ribbons + 3 Medals of Honor | Supreme naval commander |
| **General of the Armies** | 10000 XP + 6 Competence Stars (Expert level) + 40 Ribbons + 3 Medals of Honor | Supreme army commander |
| **Supreme Allied Commander** | 25000 XP + 8 Competence Stars (Master level) + 75 Ribbons + Order of Victory | Theater-level command |

**Note**: These are HARD to achieve. Nimitz commanded the entire Pacific Fleet for 3+ years. Achieving "Fleet Admiral of the Fleet" should require similar sustained excellence across many deployments.

---

## 6. Service Record Format

Each commander has a service record tracking all achievements:

```yaml
commander: Admiral Chester W. Nimitz
rank: Fleet Admiral
total_xp: 175

competence_stars:
  configuration: 1/5 deployments (no star)
  research: 1/5 deployments (no star)

ribbons:
  - name: "ClearWatch Campaign"
    date: 2026-02-07
    citation: "For meritorious service in multi-version deployment"
  - name: "Operation Stunning Charts"
    date: 2026-02-07
    citation: "For excellence in intelligence gathering"

medals:
  - type: "Commendation Medal"
    date: 2026-02-07
    project: "Operation Stunning Charts"
    citation: "Excellent work, Admiral Nimitz!"
    awarded_for: "Data retention intelligence report with 15 sources"

deployments:
  - date: 2026-02-07
    project: security-intelligence-business (ClearWatch)
    task: K8s manifests (15 deployments)
    xp_earned: 100
    outcome: success
  - date: 2026-02-07
    project: security-intelligence-business (Stunning Charts)
    task: Data retention & storage research
    xp_earned: 75 (50 base + 25 bonus)
    outcome: success

total_deployments: 2
success_rate: 100%
```

---

## 7. Progression Examples

### Example 1: Admiral Spruance

**After Operation Stunning Charts**:
- XP: 100 (75 base for chart + 25 bonus for user praise)
- Competence Stars: Visualization 1/5 (no star yet)
- Ribbons: 🎗️ Operation Stunning Charts
- Medals: 🥇 Medal of Honor
  - Citation: "OUTSTANDING work, Admiral Spruance! The confidence bands weaponize pricing opacity."

**Path to Next Star**:
- Needs 9 more successful visualization deployments
- If all succeed: ⭐ Visualization Competent (10 deployments)

### Example 2: Admiral Nimitz

**After 2 Deployments**:
- XP: 175
- Competence Stars: Configuration 1/5, Research 1/5
- Ribbons: 🎗️ ClearWatch Campaign, 🎗️ Operation Stunning Charts
- Medals: None yet

**Path to First Star**:
- Configuration: 9 more successful K8s/manifest deployments
- Research: 9 more successful intelligence deployments

**Path to Promotion**:
- Already Fleet Admiral (5-star) - highest historical rank
- Can pursue Fleet Admiral of the Fleet (requires 10000 XP, 6 Expert stars, 40 ribbons, 3 Medals of Honor)
- **Estimated**: ~200+ deployments to achieve

### Example 3: Field Marshal Montgomery

**After Operation Stunning Charts** (First deployment):
- XP: 200 (150 base coordination + 50 bonus all subordinates succeeded)
- Competence Stars: Coordination 1/5
- Ribbons: 🎗️ Operation Stunning Charts
- Medals: ⭐ **Order of Victory**
  - Citation: "THAT'S the general I wanted back. Do this for every report."
  - **Rarest medal** - only awarded when user declares breakthrough achievement

**Significance**: Montgomery earned the highest honor on his FIRST deployment. This is exceptional.

---

## 8. Implementation

### After Each Deployment

1. **Calculate XP**: Base + bonuses - penalties
2. **Update Competence Stars**: Increment category count, award star if 10/25/50/100/250
3. **Award Campaign Ribbon**: If mission qualifies (long session, clear objectives)
4. **Award Medal**: If user provides praise (capture exact quote)
5. **Check Rank Promotion**: If XP/Stars/Ribbons/Medals meet threshold
6. **Update Service Record**: Add deployment entry with all earned achievements

### Service Record Location

`/home/psimmons/projects/generals/service-records/{commander-name}.yaml`

### Ribbon Registry

`/home/psimmons/projects/generals/ribbons/registry.yaml`

Lists all available ribbons, criteria, and who has earned them.

### Medal Registry

`/home/psimmons/projects/generals/medals/registry.yaml`

Lists all medals awarded, with quotes and dates.

---

## 9. Philosophy

<!-- NOTE FOR OTHER SESSIONS: This section explains WHY the progression system is demanding.
     Do NOT reduce star/rank requirements or make progression faster.
     The system honors real WWII achievements through earned expertise.
     Star thresholds were increased in Feb 2026 to ensure progression remains meaningful at scale. -->

**These were hard men not afraid to work really hard.**

The commanders in this system earned their reputations through sustained excellence under brutal conditions. Nimitz commanded the Pacific Fleet through three years of brutal island-hopping campaigns. King rebuilt the US Navy after Pearl Harbor's devastation. Eisenhower coordinated D-Day with millions of troops across multiple nations. MacArthur fought his way across the Pacific through island assaults. Patton drove across France in rapid armored campaigns. Montgomery planned and executed complex multi-national operations at unprecedented scale. Rommel fought brilliantly in the desert despite chronic supply shortages. Zhukov broke the siege of Leningrad and led the drive to Berlin through the most devastating warfare in human history.

**The progression system must reflect this reality**: Expertise is earned through sustained excellence, not granted after one good day.

Ten deployments for the first competence star is reasonable but demanding—it requires consistent success, not a lucky streak. Two hundred and fifty deployments for Legend status reflects years of combat experience, just as these commanders served through years of continuous operations. The Order of Victory medal is extremely rare, awarded only for breakthrough achievements that change the game, just like Montgomery's actual accomplishments that earned him his place in history.

This is not a system where participation equals mastery. This is a system where **hard work under fire** earns expertise over time.

---

## 10. Next Steps

1. Create service record files for all commanders
2. Award ribbons for completed campaigns
3. Award medals based on user praise during Operation Stunning Charts
4. Track XP going forward
5. Update after each deployment
6. Display ribbons/medals in commander profiles

---

**Motto**: *"Audentes Fortuna Iuvat"* (Fortune Favors the Bold)
