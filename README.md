# Academic Research Suite

Academic Research Suite is a private Codex plugin for publication-grade economics,
finance, and business research. It separates literature synthesis and framework
building, writing, methodological auditing, peer review, citation verification,
and revision management into eight focused skills.

## Skills

| Skill | Primary use |
| --- | --- |
| `q1-manuscript-writer` | Develop or revise theoretically strong journal manuscripts and individual sections. |
| `strict-peer-reviewer` | Conduct independent, gatekeeper-level manuscript reviews. |
| `research-proposal-writer` | Build rigorous grant, doctoral, institutional, or commissioned research proposals. |
| `panel-econometrics-auditor` | Audit static and dynamic panel designs, identification, code, diagnostics, and inference. |
| `pls-sem-fsqca-reviewer` | Review PLS-SEM, fsQCA, NCA, prediction, invariance, and multimethod integration. |
| `citation-integrity-auditor` | Verify in-text citations, reference metadata, evidentiary support, and retraction status. |
| `reviewer-response-manager` | Manage reviewer comments, response matrices, manuscript locations, and completion status. |
| `literature-review` | Synthesize current evidence and foundational theories into defensible research frameworks. |

## Repository structure

- `.agents/plugins/marketplace.json`: repository marketplace entry
- `plugins/academic-research-suite/.codex-plugin/plugin.json`: plugin manifest
- `plugins/academic-research-suite/skills/`: eight skill packages
- `plugins/academic-research-suite/scripts/validate_suite.py`: cross-skill validator
- `plugins/academic-research-suite/tests/test-cases.md`: routing and safety test cases

## Validation

From the repository root, run:

```bash
python3 plugins/academic-research-suite/scripts/validate_suite.py
```

The suite is designed to prevent fabricated sources or results, significance
engineering, unsupported causal claims, and false statements that requested
analyses or revisions have been completed.

## Ownership

Copyright Vu Hiep. All rights reserved. This repository and plugin are
proprietary and intended for authorized private use.
