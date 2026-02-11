# Functional Card-Based Commander Selection Interface

**Date**: 2026-02-11
**Status**: Design Complete - Ready for Implementation
**Purpose**: Make SVG trading cards functional selection tools for spawning commanders

---

## Problem Statement

The generals project has beautiful SVG commander cards and comprehensive profiles, but no way for users to **visually select and spawn commanders** using these cards. Current workflow requires knowing commander names and using manual slash commands. The cards are purely documentation/visual assets, not functional UI elements.

**User request**: "Design functional card-based commander selection interface - make the trading cards actually usable for selecting/spawning commanders instead of just visual documentation"

---

## Design Solution

### Architecture Overview

**Two-Phase System:**

**Phase 1: Selection Interface** (User picks commander)
- Browser-based card gallery displaying all 41 SVG cards
- User clicks/selects desired commander
- Selection written to shared file (`~/.claude/commander-selection.json`)
- Interface closes automatically

**Phase 2: Spawn Integration** (Claude Code acts on selection)
- Claude Code skill watches for selection file
- Reads selected commander + task context
- Uses existing `spawn-commander` skill to deploy
- Cleans up selection file

**Rationale**: Browser renders SVG cards beautifully. File-based IPC is simple and requires no server infrastructure. Claude Code skills can poll/watch files trivially. This approach integrates with existing spawn architecture without modifications.

---

## System Components

### 1. Selection Gallery Script

**File**: `bin/generals-select`
**Language**: Bash
**Purpose**: Launch browser, wait for selection, return commander name

**Implementation**:
```bash
#!/bin/bash
# Functional commander selection interface
# Usage: generals-select "task description"

TASK="${1:-Select a commander}"
SELECTION_FILE="$HOME/.claude/commander-selection.json"
SELECTOR_HTML="$(dirname $0)/../assets/selector/index.html"

# Clean any old selection
rm -f "$SELECTION_FILE"

# Launch browser with task context
TASK_ENCODED=$(echo "$TASK" | jq -sRr @uri)
if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "file://$SELECTOR_HTML?task=$TASK_ENCODED" >/dev/null 2>&1 &
elif command -v open >/dev/null 2>&1; then
    open "file://$SELECTOR_HTML?task=$TASK_ENCODED" >/dev/null 2>&1 &
fi

# Wait for selection (max 2 minutes)
echo "Waiting for commander selection..."
for i in {1..120}; do
    if [ -f "$SELECTION_FILE" ]; then
        SELECTED=$(jq -r '.commander' "$SELECTION_FILE")
        echo "$SELECTED"
        rm -f "$SELECTION_FILE"
        exit 0
    fi
    sleep 1
done

echo "Selection timeout" >&2
exit 1
```

**Key Features**:
- Task description passed via URL parameter
- Polls for selection file (2-minute timeout)
- Cross-platform browser launch (xdg-open/open)
- Returns selected commander name to stdout
- Clean exit codes for error handling

### 2. Web Selection Interface

**File**: `assets/selector/index.html`
**Language**: HTML/CSS/JavaScript
**Purpose**: Visual card gallery with selection handling

**Key Features**:
- Load all SVG cards from `../commander-cards/*.svg`
- Extract task from URL params, display prominently
- Filter buttons by category (Aggressive, Methodical, Coordinator, Technical, Creative)
- Click handler writes selection to file system
- Auto-close on selection

**Critical Implementation Detail**: Browser File System Access

Modern browsers cannot write to arbitrary filesystem paths due to security. Three solutions:

**Option A: File System Access API** (Chromium only, requires user permission)
```javascript
const fileHandle = await window.showSaveFilePicker({
  suggestedName: 'commander-selection.json',
  startIn: 'downloads'
});
const writable = await fileHandle.createWritable();
await writable.write(JSON.stringify(selection));
await writable.close();
```

**Option B: Download + Manual Move** (Universal, no permissions)
```javascript
const blob = new Blob([JSON.stringify(selection)], {type: 'application/json'});
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'commander-selection.json';
a.click();
// User manually moves file to ~/.claude/
```

**Option C: Local Server** (Most reliable, best UX)
```javascript
fetch('http://localhost:7272/select', {
  method: 'POST',
  body: JSON.stringify(selection)
});
// Server writes file, returns success
```

**Recommendation**: Option C (local server). Server runs only when selection active, writes file, exits immediately. Provides seamless UX without manual file operations.

**Server Implementation** (`assets/selector/server.js`):
- Minimal Node.js/Python HTTP server
- Single endpoint: POST /select
- Writes JSON to `~/.claude/commander-selection.json`
- CORS enabled for file:// protocol
- Auto-shutdown after selection or timeout

### 3. Spawn Integration Skill

**File**: `skills/select-and-spawn`
**Language**: Markdown (Claude Code skill format)
**Purpose**: Orchestrate full selection-to-spawn workflow

**Workflow**:

1. **Launch Selection UI**
   - Run `bin/generals-select "task description"`
   - Script opens browser with card gallery
   - User sees all 41 commanders with visual cards
   - Task description shown prominently

2. **Wait for Selection**
   - Script polls for `~/.claude/commander-selection.json`
   - Timeout: 2 minutes
   - Returns selected commander name or error

3. **Spawn Commander**
   - Use existing `spawn-commander` skill
   - Pass selected commander + task description
   - Commander deploys with full personality

4. **Cleanup**
   - Remove selection file
   - Close selection interface

**Usage**:
```
/generals:select-and-spawn "Emergency K8s node recovery - worker135 down"
```

User sees visual gallery, clicks Patton's card, Patton spawns immediately with personality intact.

---

## Data Flow

```
User Request ("I need help with X")
    ↓
Claude invokes /generals:select-and-spawn skill
    ↓
Skill launches bin/generals-select script with task context
    ↓
Script opens browser with assets/selector/index.html?task=...
    ↓
Browser displays 41 SVG cards in filterable grid
    ↓
User browses cards, reads traits/specializations
    ↓
User clicks desired commander card
    ↓
JavaScript POSTs selection to localhost:7272/select
    ↓
Local server writes ~/.claude/commander-selection.json
    ↓
Server responds with success, closes
    ↓
bin/generals-select script detects file
    ↓
Script reads commander name, returns to Claude
    ↓
Claude invokes existing spawn-commander skill
    ↓
Commander deployed with full personality and service record
```

---

## File Structure

```
generals/
├── bin/
│   └── generals-select          # Shell script launcher
├── assets/
│   ├── commander-cards/          # 41 SVG cards (already exist)
│   │   ├── patton-card.svg
│   │   ├── montgomery-card.svg
│   │   └── ... (39 more)
│   └── selector/                 # NEW: Selection interface
│       ├── index.html            # Card gallery UI
│       ├── server.js             # Local selection server
│       └── styles.css            # UI styling (dark theme)
└── skills/
    └── select-and-spawn          # NEW: Integration skill
```

---

## Integration with Existing System

This design integrates seamlessly with zero changes to existing architecture:

**Existing System**:
- `spawn-commander` skill spawns commanders by name
- Commander profiles in `profiles/*.md`
- Service records tracked across deployments
- XP/ribbons/medals system intact

**Addition**:
- Visual selection UI provides commander name
- Same spawn logic, same personality injection
- Same service record updates

**Result**: The visual cards become functional **input mechanisms** without changing core spawning architecture. The trading card metaphor becomes reality.

---

## Alternative: Terminal-Native ASCII Selection

If browser approach proves problematic in some environments, fallback to terminal-native:

**Implementation**:
```bash
# Display ASCII cards in terminal grid
cat assets/ascii-cards/patton.txt
cat assets/ascii-cards/montgomery.txt
cat assets/ascii-cards/nimitz.txt
# ... display all 41 cards

# Interactive selection
echo "Type commander name to select:"
read SELECTED

# Spawn directly
/generals:spawn-commander "$SELECTED" "$TASK"
```

**Trade-offs**:
- **Pro**: Works in pure terminal environments, no browser required
- **Pro**: Faster for keyboard-first users who know their commander
- **Con**: ASCII cards lose visual appeal of SVG design
- **Con**: Harder to browse unfamiliar commanders

**Recommendation**: Offer both options. Power users can use ASCII/keyboard selection. New users can browse visual gallery.

---

## Implementation Plan

### Phase 1: MVP (Browser + Local Server)

**Goal**: Functional visual selection with seamless file writing

**Tasks**:
1. Create `assets/selector/index.html` with card grid
   - Load all 41 SVG cards dynamically
   - Display task context from URL params
   - Implement category filters (5 categories)
   - Click handler POSTs to localhost

2. Create `assets/selector/server.js` (Node.js)
   - Minimal HTTP server on port 7272
   - POST /select endpoint writes JSON file
   - CORS enabled for file:// protocol
   - Auto-shutdown after selection

3. Create `bin/generals-select` polling script
   - Launch browser with task context
   - Start local server in background
   - Poll for selection file (2min timeout)
   - Return commander name to stdout

4. Test with existing 5 cards
   - Verify selection flow end-to-end
   - Confirm file writing works reliably
   - Test timeout handling

**Success Criteria**:
- User clicks card → file written → script returns name
- Total time: < 3 seconds from click to spawn
- Zero manual file operations required

### Phase 2: Full Integration

**Goal**: Integrate with all 41 commanders, create skill

**Tasks**:
1. Wait for all 41 SVG cards to be created
   - Current status: 5 complete, 36 in progress via team campaign
   - Cards must follow template exactly (250×350px, consistent styling)

2. Create `/generals:select-and-spawn` skill
   - Invoke `bin/generals-select` with task description
   - Parse returned commander name
   - Invoke existing `spawn-commander` skill
   - Handle errors (timeout, no selection, invalid commander)

3. Update README with visual selection workflow
   - Add screenshots/demo GIF
   - Document keyboard shortcuts (ESC to cancel, etc.)
   - Explain filter categories

**Success Criteria**:
- User can browse all 41 commanders visually
- Selection spawns correct commander with personality
- Error handling graceful (timeout → ask for manual selection)

### Phase 3: Polish & Enhancement

**Goal**: Improve UX and add intelligence

**Tasks**:
1. Add commander recommendations
   - Analyze task keywords
   - Highlight 3 best-fit commanders in UI
   - Show fit scores and rationale

2. Search/filter functionality
   - Text search by name, specialty, traits
   - Multi-select category filters
   - Sort by XP, deployments, success rate

3. Recent selections history
   - Track last 10 selections
   - "Deploy again" quick button
   - Show trending commanders

4. Animation and transitions
   - Card hover effects (already in prototype)
   - Smooth filter transitions
   - Selection confirmation animation

**Success Criteria**:
- New users get helpful recommendations
- Experienced users can search/filter quickly
- Interface feels polished and professional

### Phase 4: Documentation & Community

**Goal**: Make feature discoverable and shareable

**Tasks**:
1. Write `docs/visual-selection-guide.md`
   - When to use visual selection vs. direct command
   - How recommendations work
   - Customization options

2. Create demo materials
   - Screen recording showing full workflow
   - GIF for README
   - Example selections for different task types

3. Gather feedback
   - Test with different task types
   - Identify usability issues
   - Iterate based on real usage

**Success Criteria**:
- Users discover feature without prompting
- Documentation covers common questions
- Community contributions (new filters, custom themes)

---

## Technical Considerations

### Security

**File Writing**: Selection file written to `~/.claude/` (user's home directory). No external network access. Server runs locally, binds to localhost only. No authentication needed (same-machine trust).

**XSS Prevention**: Task description displayed in UI must be HTML-escaped. No innerHTML with user content. Use textContent for task display.

**Path Traversal**: Server must validate file path is exactly `~/.claude/commander-selection.json`. Reject any path manipulation attempts.

### Performance

**Card Loading**: 41 SVG files (~10KB each) = ~410KB total. Modern browser loads in <500ms. Can optimize with sprite sheet if needed, but likely unnecessary.

**Selection Response**: POST → file write → polling detection should complete in <100ms on local filesystem. Total click-to-spawn: 2-3 seconds (dominated by agent spawn time, not selection).

**Memory**: Browser displays 41 cards simultaneously. Each card ~10KB SVG + ~5KB photo. Total memory footprint ~615KB. Negligible on modern systems.

### Browser Compatibility

**Target**: Modern Chromium-based browsers (Chrome, Edge, Brave)
**Fallback**: Firefox, Safari (with degraded features)
**Minimum**: Any browser with ES6 fetch API support

**Known Issues**:
- Safari file:// protocol restrictions may require local server always
- Firefox CORS strictness may need explicit headers
- Mobile browsers: touch events work but small cards may need zoom

### Maintenance

**SVG Card Updates**: When commander profiles change (XP, ribbons, traits), regenerate SVG cards. Selection interface automatically loads latest versions.

**New Commanders**: Add SVG card to `assets/commander-cards/`, update profiles. Selection interface auto-discovers via glob pattern. Zero code changes needed.

**Server Dependencies**: Node.js server requires `http` module only (stdlib). Zero npm dependencies. Python alternative uses stdlib `http.server`. Minimal maintenance burden.

---

## Success Metrics

**Usability**:
- 90%+ of new users complete first selection without help
- Average selection time: <30 seconds from launch to confirmation
- Zero manual file operations required

**Adoption**:
- 50%+ of spawns use visual selection vs. direct commands (within 1 month)
- Positive feedback on "trading card" UX metaphor
- Community requests for custom card designs

**Technical**:
- <1% selection failures (timeout/error rate)
- <3 second total latency (click to spawn)
- Works across Linux, macOS, Windows

---

## Future Enhancements

**Beyond MVP**:

1. **Card Customization**
   - User-defined color schemes
   - Custom portrait photos
   - Personalized traits based on fork history

2. **Team Selection**
   - Multi-select mode for campaigns
   - Visual team composition preview
   - Drag-drop role assignment

3. **Analytics Dashboard**
   - Commander deployment heatmap
   - Success rate by task type
   - XP leaderboard visualization

4. **Mobile App**
   - Native iOS/Android selection interface
   - Push notifications on deployment completion
   - Service record viewing

5. **Voice Integration**
   - "Deploy Patton for this emergency" voice command
   - Audio feedback on selection
   - Accessibility improvements

---

## Conclusion

This design transforms SVG trading cards from visual documentation into functional UI elements for commander selection. The browser-based gallery provides intuitive browsing and selection, while file-based IPC integrates seamlessly with Claude Code's skill system.

**Key Innovation**: Making the metaphor real. The cards aren't just pictures of commanders - they're actual selection tools that deploy those commanders when clicked.

**Next Steps**:
1. Validate design with user feedback
2. Implement Phase 1 MVP (browser + server + script)
3. Integrate with existing spawn-commander skill
4. Test with 41-card full roster

**Implementation Complexity**: Low-Medium
- Phase 1: ~4-6 hours development
- Phase 2: ~2-3 hours integration
- Phase 3: ~4-8 hours polish
- **Total**: 10-17 hours for full implementation

**Risk Level**: Low
- No changes to existing spawn architecture
- File-based IPC is battle-tested pattern
- Fallback to ASCII selection if browser issues
- Incremental rollout possible (start with 5 cards, expand to 41)

---

**Design Status**: ✅ Complete - Ready for Implementation
**Recommendation**: Proceed to Phase 1 MVP implementation
