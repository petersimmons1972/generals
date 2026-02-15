# Historical Audit - Thorough Standard Methodology

**Updated**: 2026-02-15
**Status**: Active standard for all Phase 2+ research

---

## Definition: "Thorough" Standard

Read all publicly accessible full sources completely. Acknowledge paywalled limitations explicitly.

**Time estimate**: 1-2 days per subject
**Quality target**: 88-95/100 accuracy with documented source access limitations

---

## Search Methodology - Cost Optimization

**Use SearXNG when search costs could be significant** (local instance)

**Cost-benefit guideline**:
- **High search volume** (>5 exploratory searches): Use SearXNG
- **Low search volume** (<5 targeted searches): WebFetch/WebSearch acceptable
- **Direct URLs**: Always use WebFetch directly

**SearXNG usage**:
- **URL**: `https://searxng.petersimmons.com/search?q={query}&format=json`
- **Cost**: WebFetch cheaper than WebSearch, search compute on local hardware
- **Fallback**: If SearXNG unavailable, use WebSearch tool

**See**: `../SEARXNG-INTEGRATION.md` for complete usage guide and scenarios

---

## What "Thorough" Means

### 1. Primary Sources - FULL READING REQUIRED

**Government/Official Records** (publicly accessible):
- Parliamentary debates (Hansard) - read complete transcripts, not excerpts
- Declassified military records - read full documents, not summaries
- Official despatches - read complete text
- Government inquiries/reports - read full reports, not executive summaries

**Tools**:
- UK Parliament website (hansard.parliament.uk) - full debates
- National Archives (UK: nationalarchives.gov.uk, US: archives.gov)
- German Federal Archive (bundesarchiv.de) - digitized records
- Digital collections from national libraries

**Evidence standard**: Quote directly from source, cite page numbers, provide URLs

### 2. Academic Sources - FULL READING WHERE ACCESSIBLE

**Open Access** (FULL READING):
- Open-access journal articles (complete PDFs)
- Dissertations on open repositories (complete text)
- Google Books with full preview (complete available sections)
- Author-provided preprints and working papers

**Paywalled** (ACKNOWLEDGE LIMITATION):
- Major academic books (Bungay, Saunders, etc.) - use previews where available
- Journal articles behind paywalls - cite abstracts, note limitation
- University press publications - use reviews and summaries

**Evidence standard**:
- For full-access: Quote, cite page numbers, provide methodology assessment
- For limited-access: "Based on [preview/abstract/secondary citation], acknowledging full text not accessed"

### 3. Contemporary Sources - FULL READING REQUIRED

**Newspapers/Periodicals** (digitized archives):
- New York Times archive (freely accessible)
- Times Digital Archive (some access via Google)
- Life, Picture Post (archive.org)

**Tools**:
- archive.org - historical newspapers, magazines
- Google News Archive
- National library digital collections

**Evidence standard**: Full article text, publication date, page number

### 4. Secondary Synthesis - ACKNOWLEDGE LIMITATIONS

**Museum/Educational Sites**:
- Read complete exhibition text, not just summaries
- Cite curators and institutional authority
- Note when using institutional synthesis of sources

**Documentary Evidence**:
- Watch full documentaries if relevant (not just clips)
- Assess documentary sources and methodology
- Note when using documentary claims vs. verifying original sources

---

## What NOT to Do

**NEVER**:
- Claim "read Bungay 2000" when you read Google Books preview only
- Present museum summary as if you read underlying sources
- Use "according to [source]" for third-hand claims without verification chain
- Claim comprehensive coverage when paywalls blocked access
- Synthesize from Wikipedia without checking its citations

**ALWAYS**:
- Distinguish direct reading from secondary citation
- Document access limitations explicitly
- Provide evidence chain (where did this claim originate?)
- Note when you cannot verify a claim due to access limits

---

## Source Access Tracking

For each source, document:

```markdown
### [Source Title]

**Access level**:
- FULL (read complete text)
- PARTIAL (read preview/excerpts, note % coverage)
- SUMMARY (used secondary synthesis, note limitation)

**Evidence extracted**:
- [Direct quotes with page numbers]
- [Methodological assessment if full access]

**Reliability tier**: [1-7 per hierarchy]

**Limitations**: [What you couldn't verify]
```

---

## Example: Thorough vs Summary-Based

### SUMMARY-BASED (OLD - DON'T DO THIS):
"Bungay (2000) says fighter-to-fighter strength was near parity."

### THOROUGH (NEW STANDARD):
"Bungay's *The Most Dangerous Enemy* (2000) reconstructs Luftwaffe order of battle from German primary sources (Bundesarchiv) and British records (National Archives). His Chapter 4 analysis shows:

- RAF single-engine fighters: 620-700 (July 10, 1940)
- Luftwaffe Bf 109s: 700-800 (same date)

**Source access**: Google Books preview provides 85% of Chapter 4. Full statistical appendices not accessible (paywalled). Cross-verified core figures against Hansard Parliamentary Debate (May 14, 1947) which cites German records directly - figures align within 5% margin.

**Assessment**: Parity claim VERIFIED via primary sources (Hansard), independent of Bungay access limitation. Methodology appears sound based on accessible sections."

---

## Quality Checklist

Before claiming research complete:

- [ ] All publicly accessible primary sources read in full
- [ ] Direct quotes extracted with page numbers/URLs
- [ ] Paywalled sources explicitly acknowledged
- [ ] Evidence chains documented (where did this claim come from?)
- [ ] Cross-verification attempted for paywalled claims
- [ ] Source access levels documented for each source
- [ ] No unverifiable claims presented as fact
- [ ] Limitations section included in research notes

---

## Time Allocation

**Day 1**: Primary sources
- Read Hansard debates (if relevant)
- Read official military records/despatches
- Read declassified documents
- Extract and cross-reference key data

**Day 2**: Academic synthesis
- Read all open-access papers completely
- Review Google Books previews
- Verify paywalled claims through cross-reference
- Document limitations and accessibility gaps

---

## Team Instructions

**For researchers (Murrow, Orwell, Pyle)**:

When you encounter a source:
1. Determine access level (full/partial/summary)
2. If FULL: Read completely, extract quotes, assess methodology
3. If PARTIAL: Read available sections, note coverage %, cite what you verified
4. If SUMMARY: Use secondary synthesis, note limitation, attempt cross-verification
5. Document access level in sources.md

**Red flags** (stop and report):
- Claiming comprehensive coverage when paywalls blocked major sources
- Presenting secondary claims without evidence chain
- Using "according to X" for unverified third-hand claims
- Speed inconsistent with claimed full reading (500-page book in 1 hour = NOT full reading)

---

## Success Metrics

**Thorough standard achieved when**:
- All accessible primary sources read in full
- Paywalled limitations explicitly documented
- Evidence chains clear and verifiable
- Accuracy 88-95/100 (acknowledging access gaps)
- No false claims of comprehensiveness

**Thorough standard FAILED when**:
- Claimed full reading but used summaries
- Paywalled limitations hidden or minimized
- Evidence chains broken or unverifiable
- Overclaimed certainty on inaccessible sources

---

*This standard balances depth with feasibility. It is HONEST about limitations while dramatically improving quality over summary-based research.*
