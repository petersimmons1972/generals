# Sync Protocol

**When to sync**: After any deployment that changes XP/stats.

**How to sync**:
1. `cd ~/projects/generals && git pull origin master`
2. Compare roster XP in `~/AGENTS.md` against `profiles/service-records/*.yaml`
3. Update AGENTS.md roster table if stale
4. Note new sync date in Section 2 header

**Why staleness is acceptable**: Spawn decisions are specialization-based, not XP-dependent. A commander's specialization doesn't change between syncs. XP only matters for model assignment (high-XP = proven = Opus-worthy), and small XP deltas don't change that calculus.
