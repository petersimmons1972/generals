#!/usr/bin/env python3
"""
Generate ~/.claude/generals-roster-cache.json from generals service-record YAMLs.
Run at session start to keep Field Marshal context lean.

Output format:
{
  "eisenhower": {"xp": 550, "model": "opus", "spec": "coordination"},
  ...
  "_generated": "2026-03-02T04:00:00Z",
  "_source": "generals/profiles/service-records/"
}
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    # Fallback: minimal YAML parser for simple key: value files
    yaml = None

# Hardcoded model assignments (not in YAMLs, lives in AGENTS.md/CLAUDE.md)
MODEL_ASSIGNMENTS = {
    "eisenhower": "opus",
    "montgomery": "opus",
    "spruance": "opus",
    "rickover": "opus",
    "bradley": "opus",
    "layton": "opus",
    "mitchell": "opus",
    "dowding": "opus",
    "nimitz": "sonnet",
    "king": "sonnet",
    "halsey": "sonnet",
    "rommel": "sonnet",
    # Extended roster
    "patton": "opus",
    "macarthur": "opus",
    "slim": "sonnet",
    "zhukov": "opus",
    "lemay": "sonnet",
    "ogilvy": "opus",
    "orwell": "sonnet",
    "pyle": "sonnet",
}

def parse_yaml_simple(path):
    """Minimal YAML parser for top-level key: value pairs (no PyYAML dependency)."""
    result = {}
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.rstrip()
                if not line or line.startswith(" ") or line.startswith("#"):
                    continue
                if ":" in line:
                    key, _, value = line.partition(":")
                    key = key.strip()
                    value = value.strip().strip('"')
                    if key and value:
                        result[key] = value
    except Exception as e:
        print(f"  Warning: could not parse {path}: {e}", file=sys.stderr)
    return result

def load_yaml(path):
    if yaml is not None:
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"  Warning: yaml.safe_load failed for {path}: {e}", file=sys.stderr)
            return parse_yaml_simple(path)
    else:
        return parse_yaml_simple(path)

def extract_short_spec(specializations):
    """Convert long specialization list to short string for cache."""
    if not specializations:
        return "general"
    if isinstance(specializations, list):
        first = specializations[0]
    else:
        first = str(specializations)
    # Shorten to <=30 chars
    spec_map = {
        "Multi-Team Coordination": "coordination",
        "Intelligence Synthesis": "intel-synthesis",
        "Campaign Leadership": "campaign-leadership",
        "Verification": "verification",
        "TDD": "tdd",
        "Configuration & Manifest Engineering": "config-manifests",
        "Competitive Intelligence Research": "intel-research",
        "Workflow Analysis": "workflow-analysis",
        "Coalition Building": "coordination",
        "Timeline Visualization": "visualization",
        "Data Retention Analysis": "data-analysis",
        "Rapid Tactical Execution": "rapid-execution",
        "Zero-defect standards": "zero-defect",
        "technical excellence": "technical-excellence",
        "Deployment Operations": "deployment",
        "Blocker Identification": "diagnostics",
        "Aggressive Action": "rapid-action",
        "Intelligence Analysis": "intel-analysis",
        "SIGINT": "sigint",
        "Air Power Innovation": "air-power",
        "Code Review": "code-review",
        "Integrated Defense": "systems-integration",
        "Systems Integration": "systems-integration",
    }
    for long, short in spec_map.items():
        if long.lower() in first.lower():
            return short
    # Default: lowercase first 30 chars, spaces to dashes
    return first[:30].lower().replace(" ", "-").replace("/", "-")

def main():
    script_dir = Path(__file__).parent
    generals_root = script_dir.parent
    service_records_dir = generals_root / "profiles" / "service-records"
    output_path = Path.home() / ".claude" / "generals-roster-cache.json"

    if not service_records_dir.exists():
        print(f"ERROR: service-records dir not found: {service_records_dir}", file=sys.stderr)
        sys.exit(1)

    roster = {}
    yaml_files = sorted(service_records_dir.glob("*.yaml"))

    if not yaml_files:
        print("WARNING: No YAML files found in service-records/", file=sys.stderr)

    for yaml_path in yaml_files:
        name = yaml_path.stem  # filename without .yaml
        data = load_yaml(yaml_path)

        # Extract total_xp
        xp_raw = data.get("total_xp", 0)
        try:
            xp = int(xp_raw)
        except (ValueError, TypeError):
            xp = 0

        # Extract specializations
        specs_raw = data.get("specializations", [])
        spec = extract_short_spec(specs_raw)

        # Model from hardcoded map, default sonnet
        model = MODEL_ASSIGNMENTS.get(name, "sonnet")

        roster[name] = {
            "xp": xp,
            "model": model,
            "spec": spec,
        }
        print(f"  {name}: xp={xp}, model={model}, spec={spec}")

    # Add metadata
    roster["_generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    roster["_source"] = "generals/profiles/service-records/"

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(roster, f, indent=2, sort_keys=True)

    print(f"\nWrote {len(roster) - 2} commanders to {output_path}")

if __name__ == "__main__":
    main()
