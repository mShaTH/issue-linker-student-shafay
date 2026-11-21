# Data reference (optional reading)

**Source:** Maëlick Claes and Mika V. Mäntylä (2020), *20-MAD: 20 Years of
Issues and Commits of Mozilla and Apache Development*, MSR '20, pp. 503–507.
[Paper DOI](https://doi.org/10.1145/3379597.3387487) ·
[Author manuscript record](https://oulurepo.oulu.fi/handle/10024/28299).

These fixtures contain **20 real ZooKeeper issues and 60 real commits** from the
[authors' sample](https://github.com/M3SOulu/MozillaApacheDataset-sample/tree/665fdbe89efa3507dd14bfd8ca293049571f6d6e),
revision `665fdbe89efa3507dd14bfd8ca293049571f6d6e`, retrieved 2026-11-18.
The upstream files are `issues.csv.gz` and `commits.csv.gz`.

| File / field | Meaning / upstream field |
| --- | --- |
| `data/issues.json`: `issue_id` | Public issue key, copied from `issue_key`; not the upstream numeric `issue_id` |
| `data/issues.json`: `summary` | Issue title, copied from `summary` |
| `data/commits.json`: `hash` | Commit identifier, copied from `hash` |
| `data/commits.json`: `message` | Full message, copied from `message` |

**Changes:** selected Apache/ZooKeeper rows, dropped unused columns, renamed
`issue_key` to `issue_id`, converted CSV to JSON, and reordered records. Titles
and messages are unchanged, including any literal escaped newlines already in
the CSV. Do not fetch the original repositories or build ZooKeeper.

The subset deliberately mixes references to supplied issues, references to other
issues, and messages without issue keys. It also includes supplied issues with
no references in the selected commits. This is an assessment fixture, not a
representative research sample. Reference means textual mention, including
reverts; it does not mean a confirmed bug fix.

**Licence and attribution:** the
[authors' dataset documentation](https://github.com/M3SOulu/MozillaApacheDataset)
states that the dataset is licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
Retain this attribution and change notice when redistributing the derived data.
No endorsement by the authors or Apache is implied. The dataset authors retain
their rights; the licence statement here concerns the dataset.

**Synthetic material:** the README input/output and supplied unit-test example
were created for this exercise. Neither `data/*.json` file contains synthetic
records. Candidates may create synthetic fixtures for their tests.

**Optional tool references:** [Python unittest](https://docs.python.org/3/library/unittest.html),
[Python JSON](https://docs.python.org/3/library/json.html),
[Git bundles](https://git-scm.com/docs/git-bundle).
