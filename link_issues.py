#!/usr/bin/env python3
"""Link supplied issue IDs to explicit mentions in commit messages."""

import argparse
import json
import sys
import re


def build_links(issues: list[dict], commits: list[dict]) -> list[dict]:
    """Return [{"issue_id": str, "commits": [str, ...]}, ...]; see README.md."""
    result = []
    for issue in issues:
        current_id = issue["issue_id"]
        start_check = r"(?<![A-Za-z0-9_-])"
        end_check = r"(?![A-Za-z0-9_-])"
        esc_id = re.escape(current_id)
        all_checks =  start_check + esc_id + end_check
        final_id = re.compile(all_checks)
        same_hashes = []
        for commit in commits:
            current_message = commit["message"]
            current_hash = commit["hash"]
            if final_id.search(current_message):
                same_hashes.append(current_hash)
        same_hashes.sort()
        result.append({"issue_id": current_id, "commits": same_hashes})
    result.sort(key=lambda x: x["issue_id"])
    return result


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
