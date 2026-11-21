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
        curr_id = issue["issue_id"]
        c = r"(?<![A-Za-z0-9_-])"
        c2 = r"(?![A-Za-z0-9_-])"
        esc = re.escape(curr_id)
        p =  c + esc + c2
        p = re.compile(p)
        same_hashes = []
        for commit in commits:
            mes = commit["message"]
            hash = commit["hash"]
            if p.search(mes):
                same_hashes.append(hash)
        result.append({"issue_id":curr_id, "commits":same_hashes})
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
