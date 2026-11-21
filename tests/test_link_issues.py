"""Synthetic example. Add your own cases; keep this test."""

import unittest

from link_issues import build_links


class LinkIssuesTests(unittest.TestCase):
    def test_one_reference(self):
        issues = [{"issue_id": "ZOOKEEPER-12", "summary": "Example issue"}]
        commits = [{"hash": "abc123", "message": "Revert ZOOKEEPER-12."}]
        self.assertEqual(
            build_links(issues, commits),
            [{"issue_id": "ZOOKEEPER-12", "commits": ["abc123"]}],
        )


if __name__ == "__main__":
    unittest.main()
