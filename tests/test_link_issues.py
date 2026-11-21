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
            [{"issue_id": "ZOOKEEPER-12", "commits": []}],
        )
        
    def test_boundaries(self):
        issues = [{"issue_id": "ZOOKEEPER-12", "summary": "Example issue"}]
        commits = [
            {"hash": "aaa", "message": "ZOOKEEPER-12"},
            {"hash": "bbb", "message": "(ZOOKEEPER-12)"},
            {"hash": "ccc", "message": "ZOOKEEPER-12: fix issue"},
            {"hash": "ddd", "message": 'Revert "ZOOKEEPER-12: fix issue"'},
            {"hash": "eee", "message": "https://abc.def.com/test/test2/ZOOKEEPER-12"},
            {"hash": "fff", "message": "first line\nZOOKEEPER-12."},
            {"hash": "ggg", "message": "ZOOKEEPER-123"},
            {"hash": "hhh", "message": "ZOOKEEPER-012"},
            {"hash": "iii", "message": "zookeeper-12"},
            {"hash": "jjj", "message": "XZOOKEEPER-12"},
            {"hash": "kkk", "message": "ZOOKEEPER-12-extra"},
            {"hash": "lll", "message": "_ZOOKEEPER-12"},
            {"hash": "mmm", "message": "ZOOKEEPER-12a"},
            {"hash": "nnn", "message": "fix/ZOOKEEPER-12-fix-issue"},
        ]
        self.assertEqual(
            build_links(issues, commits),
            [{"issue_id": "ZOOKEEPER-12", "commits": ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]}],
        )


if __name__ == "__main__":
    unittest.main()
