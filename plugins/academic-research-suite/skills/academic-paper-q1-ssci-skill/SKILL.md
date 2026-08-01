---
name: academic-paper-q1-ssci-skill
description: Orchestrate end-to-end development, critical review, methodological reporting, polishing, and submission preparation for Q1 and SSCI academic papers. Use when the user explicitly requests this imported skill, invokes one of its slash-style paper commands, or needs a coordinated workflow spanning multiple manuscript stages.
---

# Academic Paper Q1/SSCI Skill

Coordinate an academic paper from research positioning through submission or revision. Treat the imported upstream materials as reusable guidance, not as evidence or current journal policy.

## Operating rules

1. Establish the requested deliverable, field, target journal if known, manuscript stage, available evidence, methodology, and constraints.
2. Select only the upstream references required for the task. Do not load all reference files by default.
3. Use the suite's dedicated skills when a specialist workflow is primary:
   - Use `literature-review` for evidence discovery, foundational theory mapping, and research-framework construction.
   - Use `q1-manuscript-writer` for focused manuscript drafting or prose revision.
   - Use `strict-peer-reviewer` for an independent editorial review.
   - Use `panel-econometrics-auditor` for panel identification, estimation, diagnostics, and code review.
   - Use `pls-sem-fsqca-reviewer` for PLS-SEM, fsQCA, NCA, prediction, invariance, and multimethod integration.
   - Use `citation-integrity-auditor` for exhaustive citation and reference verification.
   - Use `reviewer-response-manager` for point-by-point response management.
4. Use this skill as the orchestrator when the request spans several of those stages or explicitly invokes its command interface.
5. Never fabricate sources, quotations, DOIs, data, analyses, statistical results, journal metrics, acceptance rates, special issues, or manuscript locations.
6. Verify current journal policies, rankings, metrics, calls for papers, reporting standards, and software guidance using primary or authoritative sources. State the verification date.
7. Distinguish supplied facts, verified evidence, reasoned inference, illustrative language, and unresolved information.
8. Treat upstream numerical rules, including suggested reference counts and recency shares, as heuristics. Apply the target journal's actual requirements and field norms instead.
9. Do not claim causal identification unless the design and assumptions support it.
10. Do not use em dashes in generated prose.

## Command routing

Interpret the following forms as workflow requests even when the user omits the leading slash:

- `/outline`: develop titles, questions, theoretical positioning, hypotheses, method, and target-journal logic.
- `/introduction`: write or revise an introduction around problem importance, tension, gap, purpose, and contributions.
- `/literature`: conduct a thematic critical synthesis that supports the framework and hypotheses.
- `/hypothesis`: build theory-led causal or associational arguments and state testable hypotheses.
- `/methods`: justify the design, sample, measures, estimand, analysis, validity, bias controls, and robustness plan.
- `/results`: report only supplied or reproducibly generated findings with appropriate uncertainty, effect sizes, and diagnostics.
- `/discussion`: interpret findings against theory and evidence; develop implications, limitations, and future research.
- `/abstract`: prepare a concise abstract consistent with the completed manuscript and journal requirements.
- `/review`, `/polish`, `/checklist`: diagnose or improve a supplied section without inventing missing evidence.
- `/gaps`, `/journals`, `/trends`, `/phrases`: use verified literature or current authoritative information and disclose search limits.
- `/cover-letter`, `/response`, `/highlight`: prepare submission or revision materials while distinguishing proposed from completed changes.
- `/pls-sem`, `/nca`, `/fsqca`, `/integrated`, `/stata`: route to the relevant methodological specialist and verify current technical guidance where needed.

## Workflow

### 1. Scope

- Confirm whether the user needs planning, drafting, auditing, polishing, submission, or revision.
- Inventory the material actually available: topic, data, model, outputs, manuscript, references, journal instructions, reviewer comments, and templates.
- State any blocking evidence or access gaps before drafting claims that depend on them.

### 2. Plan

- Define the contribution claim as a theoretical advance, empirical identification gain, methodological insight, or defensible combination.
- Map each requested section to its evidentiary inputs and quality gates.
- Sequence work so that the introduction and abstract are finalized only after the central argument and findings are stable.

### 3. Execute

- Apply the appropriate specialist workflow and load only relevant upstream references.
- Preserve the user's evidence, terminology, variable definitions, and reported findings unless correction is authorized and supported.
- For empirical work, connect each methodological choice to the estimand, assumptions, diagnostics, robustness, and inferential limits.
- For theory development, make each proposed path explicit through construct definitions, mechanism, boundary conditions, rival explanation, and expected direction.

### 4. Verify

- Check internal consistency across questions, hypotheses, measures, analysis, results, discussion, and conclusions.
- Verify every source used for substantive claims before presenting it as factual.
- Separate a targeted citation check from a complete citation audit; use `citation-integrity-auditor` for the latter.
- Report what was checked, what remains unverified, and what should be supplied next.

### 5. Deliver

- Lead with the requested output rather than process narration.
- Follow the target journal, institution, or user-supplied format.
- Keep reviewer-facing writing specific, evidence-located, and professionally candid.
- Never report a proposed edit as completed unless the underlying file or text was actually changed and verified.

## Upstream reference map

The following files are preserved verbatim from upstream commit `e392fec7e7cc70a3dea9b8a170a6ff0ffdfa84d3`:

- Core operating guidance: [01-master-instructions.md](references/upstream/01-master-instructions.md)
- Paper architecture and method selection: [02-paper-structure.md](references/upstream/02-paper-structure.md)
- Writing guidance: [03-writing-guidelines.md](references/upstream/03-writing-guidelines.md)
- Method templates: [04-methodology-templates.md](references/upstream/04-methodology-templates.md)
- Quality checklist: [05-quality-checklist.md](references/upstream/05-quality-checklist.md)
- Literature-review guidance: [06-literature-review-guide.md](references/upstream/06-literature-review-guide.md)
- Reviewer-comment patterns: [07-common-reviewer-comments.md](references/upstream/07-common-reviewer-comments.md)
- Academic phrase bank: [09-academic-phrases-bank.md](references/upstream/09-academic-phrases-bank.md)
- Response-letter template: [10-response-letter-template.md](references/upstream/10-response-letter-template.md)
- Original command specification: [SKILL.md](references/upstream/SKILL.md)
- Original overview: [README.md](references/upstream/README.md)
- Sample abstract: [examples_sample-abstract.md](references/upstream/examples_sample-abstract.md)
- Sample hypothesis arguments: [examples_sample-hypothesis-args.md](references/upstream/examples_sample-hypothesis-args.md)
- Sample introduction: [examples_sample-introduction.md](references/upstream/examples_sample-introduction.md)
- Sample response letter: [examples_sample-response-letter.md](references/upstream/examples_sample-response-letter.md)

Do not treat sample citations, journal metrics, methodological thresholds, or reporting language as verified merely because they appear in an upstream file. Recheck them for the current task.
