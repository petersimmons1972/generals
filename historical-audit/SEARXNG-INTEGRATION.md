# SearXNG Integration for Research

**Purpose**: Use local SearXNG instance for web searches to reduce API costs.

**Instance**: `https://searxng.petersimmons.com`

---

## When to Use SearXNG (Cost-Benefit Analysis)

**STRONGLY CONSIDER SearXNG when search costs could be significant**:

**High search volume scenarios** (use SearXNG):
- Exploratory research phases (10+ searches)
- Discovering new sources/archives/databases
- Multi-source verification across many sites
- Competitive analysis requiring broad web coverage
- Market research with many general queries
- Topic discovery ("find everything on X")

**Low search volume scenarios** (WebFetch/WebSearch acceptable):
- Direct URL access (you already have the URL)
- Known archives (Hansard, National Archives, specific repositories)
- 1-3 targeted searches
- Specific document retrieval

**Cost-benefit rule**: If you expect >5 exploratory searches, use SearXNG. If <5 targeted searches, WebFetch/WebSearch is fine.

---

## API Usage

### Basic Search

```
WebFetch with URL: https://searxng.petersimmons.com/search?q={query}&format=json
```

**Parameters**:
- `q` - Search query (URL-encoded)
- `format=json` - Return JSON results
- `language=en` - English results (optional)
- `categories=general` - Search category (optional)

### Example Queries

**General search**:
```
https://searxng.petersimmons.com/search?q=Battle+of+Britain+primary+sources&format=json
```

**Academic search**:
```
https://searxng.petersimmons.com/search?q=Erich+von+Manstein+war+crimes&format=json&categories=science
```

**News/historical articles**:
```
https://searxng.petersimmons.com/search?q=Hugh+Dowding+1940&format=json&categories=news
```

---

## Response Format

**JSON structure**:
```json
{
  "query": "search terms",
  "results": [
    {
      "title": "Page title",
      "url": "https://example.com/page",
      "content": "Snippet of content...",
      "engine": "google"
    }
  ]
}
```

**Processing results**:
1. Parse JSON response
2. Extract relevant URLs from `results` array
3. Use WebFetch to access full content of promising URLs
4. Document sources accessed

---

## Integration in Research Workflow

### Discovery Phase

**Task**: Find sources on "Air Chief Marshal Dowding spiritualism"

**Step 1 - Search via SearXNG**:
```
WebFetch("https://searxng.petersimmons.com/search?q=Dowding+spiritualism+Many+Mansions&format=json")
```

**Step 2 - Review results**:
- Parse JSON, identify relevant URLs
- Prioritize: academic sources, archives, official records
- Note: museum sites, biographical databases

**Step 3 - Access full sources**:
```
WebFetch("https://example.com/dowding-spiritualism-article")  # Direct access
```

**Step 4 - Document**:
```markdown
### Source Discovery Method
- SearXNG query: "Dowding spiritualism Many Mansions"
- Results reviewed: 10 URLs
- Accessed: 3 URLs (academic papers, biographical sources)
- Method: Local search instance (cost-optimized)
```

### Verification Phase

**Task**: Cross-verify claim across multiple sources

**Use SearXNG for**:
- Finding additional sources on specific claim
- Discovering contradictory evidence
- Locating primary source repositories

---

## Cost Comparison

### WebSearch (Anthropic)
```
WebSearch("Battle of Britain statistics")
→ API operation cost (higher)
→ Results processed through Anthropic infrastructure
```

### SearXNG (Local)
```
WebFetch("searxng.petersimmons.com/search?q=Battle+of+Britain+statistics&format=json")
→ WebFetch cost only (lower)
→ Search computation on local hardware (free)
→ Same token cost for processing results
```

**Savings**: WebFetch cheaper than WebSearch, search compute happens locally.

---

## Agent Prompt Template

**For future research missions, include**:

```markdown
**SEARCH METHODOLOGY**:

For web searches, use SearXNG (local instance) instead of WebSearch tool:

1. **Exploratory searches**:
   - Use: `WebFetch("https://searxng.petersimmons.com/search?q={query}&format=json")`
   - Parse JSON results
   - Access promising URLs with additional WebFetch calls

2. **Direct URL access**:
   - Use: `WebFetch("{url}")` directly
   - Skip SearXNG for known URLs

3. **Document search method**:
   - Note: "Source discovered via SearXNG query: {query}"
   - Include URLs accessed from search results

**Cost optimization**: SearXNG runs on local infrastructure, reducing API costs.
```

---

## Availability and Health

**Check SearXNG status**:
```bash
curl -I https://searxng.petersimmons.com/search?q=test
# Should return: HTTP/2 200
```

**If SearXNG unavailable**:
- Fallback to WebSearch tool
- Document in research notes: "SearXNG unavailable, used WebSearch fallback"
- Report to Field Marshal

**Scaling** (if needed):
```bash
kubectl scale deployment searxng -n default --replicas=2
```

---

## Example: Full Research Workflow

**Research task**: Find open-access papers on Battle of Britain tactics

**Step 1 - Discover sources**:
```
WebFetch("https://searxng.petersimmons.com/search?q=Battle+of+Britain+tactics+open+access+PDF&format=json&categories=science")
```

**Step 2 - Parse results** (example):
```json
{
  "results": [
    {
      "title": "Bootstrapping the Battle of Britain",
      "url": "https://muse.jhu.edu/article/12345",
      "content": "Open-access paper on tactical analysis..."
    }
  ]
}
```

**Step 3 - Access paper**:
```
WebFetch("https://muse.jhu.edu/article/12345")
```

**Step 4 - Verify open access**:
- If paywalled: note limitation, search for preprint
- If accessible: download and read fully

**Step 5 - Document**:
```markdown
### Source: Bootstrapping the Battle of Britain
**Discovery**: SearXNG query "Battle of Britain tactics open access PDF"
**Access**: Full text (open-access)
**Read**: Complete (37 pages)
```

---

## Best Practices

1. **Use specific queries**: "Dowding Despatch 1946 full text" vs "Dowding"
2. **Combine search terms**: "von Manstein" + "Einsatzgruppen" + "11th Army"
3. **Filter by category**: Use `categories=science` for academic sources
4. **Parse results carefully**: Not all results will be relevant or accessible
5. **Document search method**: Always note how you found a source

---

## Fallback Protocol

**If SearXNG is down or slow**:

1. Check status: `curl -I https://searxng.petersimmons.com`
2. If unavailable: Use WebSearch tool as fallback
3. Document: "SearXNG unavailable at {timestamp}, used WebSearch"
4. Report to Field Marshal for investigation

**Do not block research on SearXNG availability** - fallback to WebSearch immediately if needed.

---

**Last updated**: 2026-02-15
**Integration status**: Active for all future research missions
