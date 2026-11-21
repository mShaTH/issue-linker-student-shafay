#!/usr/bin/env python3
"""Link supplied issue IDs to explicit mentions in commit messages."""

import argparse
import json
import sys


def build_links(issues: list[dict], commits: list[dict]) -> list[dict]:
    """Return [{"issue_id": str, "commits": [str, ...]}, ...]; see README.md."""
    # TODO: implement the matching and output rules.
    raise NotImplementedError("Implement build_links")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("issues", help="Path to the issues JSON array")
    parser.add_argument("commits", help="Path to the commits JSON array")
    args = parser.parse_args()
    with open(args.issues, encoding="utf-8") as stream:
        issues = json.load(stream)
    with open(args.commits, encoding="utf-8") as stream:
        commits = json.load(stream)
    json.dump(build_links(issues, commits), sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
