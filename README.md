# Issue–commit linker · 2 hours

Build a small tool that links issues to commits that mention them. This is data
preparation for software-quality research; a mention does **not** prove a fix.
Read this page; `DATA.md` is optional provenance/reference material.

## Before the clock starts

Use Python 3.10+ and Git; no packages to install. Unzip this folder, open a terminal
in it, and run the following. Set your Git name/email locally if Git requests it.

```sh
python3 --version
git init -b main
git add .
git commit -m "Start assessment"
python3 link_issues.py --help
python3 -m unittest discover -s tests -v
```

The example test initially reports `NotImplementedError`: that is expected.
Tell the assessor about other setup problems before starting.

## Implement

Complete `build_links(issues, commits)` in `link_issues.py`. File loading and the
command-line interface are supplied. Inputs are JSON arrays:

```json
[{"issue_id":"ZOOKEEPER-12","summary":"Example issue"}]
```
```json
[{"hash":"abc123","message":"Revert ZOOKEEPER-12."}]
```

Expected output:

```json
[{"issue_id":"ZOOKEEPER-12","commits":["abc123"]}]
```

- Match exact, case-sensitive issue IDs anywhere in the message, including URLs,
  quoted text, and reverts. Match `ZOOKEEPER-12`, not `ZOOKEEPER-123`,
  `zookeeper-12`, or `ZOOKEEPER-012`.
- An ID must touch the start/end of the message or a character outside
  `A–Z`, `a–z`, `0–9`, `_`, and `-` on **each** side. Thus `(ZOOKEEPER-12)`
  matches; `XZOOKEEPER-12` and `ZOOKEEPER-12-extra` do not.
- A commit may reference several issues. Include its hash once per referenced
  issue. Ignore IDs absent from the input issue list.
- Include every supplied issue, using `[]` when it has no matches. Sort output
  issues by ID and each hash list alphabetically (ordinary string sorting).
- Inputs are valid UTF-8 JSON with the shown fields and string values. Issue IDs
  and commit hashes are unique within their input files; arrays/messages may be
  empty. Hashes are opaque strings. No malformed-input handling, network access,
  or performance optimisation is required. Keep the function and CLI interfaces.

## Test, commit, submit

```sh
python3 link_issues.py data/issues.json data/commits.json > result.json
python3 -m unittest discover -s tests -v
```

Write your own automated tests for normal/no matches, multiple/repeated
references, ID boundaries, ordering, and one file-to-output CLI case. Keep the
provided test. Do not alter the supplied data or hard-code its answers.

Work independently: no LLMs, coding agents, or generative autocomplete. Ordinary
editor completion, documentation, and web references are allowed; no copied
solutions or help from others. Briefly note any external sources you use below.
Commit meaningful progress during the session; do not squash the history.

Stop at 120 minutes, including reading, tests, and notes. Partial work earns partial credit.
Fill in the notes below, commit your work, then create the submission:

```sh
git add link_issues.py tests README.md
git commit -m "Finish assessment and notes"
git status --short
git bundle create ../submission.bundle --all
```

If you created other source files, add those too. Hand `submission.bundle` to the
assessor; it contains committed files/history, not uncommitted work. Grading:
correctness **40%**, your tests **30%**, readability **15%**, Git and notes **15%**.
Additional assessor tests check only the behaviour stated above.

**Your notes (at most five bullets):** assumptions, unfinished work, test command
changes (if any), and external sources used.

- Assumptions: An ID matches if its seperate from other letters, numbers, and _ or -. Each commit comes only once, and IDs not found in the issues file are ignored.
- Test Command: Unchanged.
- Sources: Used python docs to study regex.
