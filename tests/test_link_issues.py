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

    def test_two_references(self):
        issues = [{"issue_id": "ZOOKEEPER-12", "summary": "Example issue"}]
        commits = [{"hash": "aaa", "message": "ZOOKEEPER-12: fix issue"},{"hash": "bbb", "message": "follow up for ZOOKEEPER-12"}]
        self.assertEqual(
            build_links(issues, commits),
            [{"issue_id": "ZOOKEEPER-12", "commits": ["aaa", "bbb"]}],
        )
        
    def test_no_matches(self):
        issues = [{"issue_id": "ZOOKEEPER-12", "summary": "Example issue"}]
        commits = [{"hash": "aaa", "message": "not exists"}]
        self.assertEqual(
            build_links(issues, commits),
            [{"issue_id": "ZOOKEEPER-12", "commits": []},],
        )


if __name__ == "__main__":
    unittest.main()
