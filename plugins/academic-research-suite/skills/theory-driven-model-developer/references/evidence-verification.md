# Web Search, Evidence Verification, and Coverage Protocol

## 1. Search architecture

Start from the input's meaningful concept blocks. Do not rely on a single exact phrase. Run parallel searches, then narrow to verified studies:

| Concept block | Example query form (substitute actual constructs) | Purpose |
| --- | --- | --- |
| Phenomenon | `("generative AI" OR "AI capability") AND (SME OR firm)` | Map domain and synonyms |
| Direct relationship | `("AI capability") AND ("innovation performance")` | Discover direct evidence |
| Theory | `("dynamic capabilities") AND ("AI adoption") AND firm` | Test mechanism applicability |
| Mechanism | `("knowledge integration") AND ("innovation") AND mediation` | Discover process explanations |
| Alternatives | `("AI capability") AND ("innovation") AND (null OR inconsistent OR negative)` | Locate competing results |
| Boundary | `("AI capability") AND innovation AND (industry OR institutional OR size)` | Test generalisability |
| Seminal sources | `[theory] foundational paper original publication` | Locate and verify original theories |

Examples are search syntax demonstrations, not verified studies or assertions about the listed relationships. Adapt operators to the platform. Search in English unless the user's literature domain requires additional languages. Record true query text and search date; never create a retrospective search log.

## 2. Source preference and verification

Preferred order: publisher's original article / accessible published PDF; official DOI registration metadata; reputable research indexing record and institutional repository; relevant trustworthy secondary review. Use general web results and abstracts primarily for discovery. A verified DOI confirms existence and metadata, **not** support for a specific empirical conclusion.

Use available search and browsing tools to check each materially cited source. When full text cannot be accessed, extract **only** information actually visible in the complete abstract; label `ABSTRACT ONLY`. When only metadata is available, do not attribute findings to that source. Do not claim to have accessed Web of Science, Scopus, full-text publisher subscriptions, or a reference manager without using them.

When feasible, check correction, retraction, and update status on official records. Check any journal tier or index claim against a current source if it matters; do not infer validity from impact metrics.

## 3. Source ledger (one row per used study)

| ID | Verified APA metadata + DOI/URL | Access (FULL / ABSTRACT / METADATA) | Study type, design and sample | Constructs and operationalisation | Evidence directly visible | Limitation/counterevidence | Claim supported in report |
| --- | --- | --- | --- | --- | --- | --- | --- |

Keep `not reported`, `not accessed`, and `not verified` explicit. Never fill gaps by inference. For conceptual or seminal works, replace sample and empirical results with the theory's actual propositions and original setting.

## 4. Evidence quality appraisal

For each important study consider:

- Construct/measurement overlap and validity
- Sampling and external validity; data source and informant fit
- Cross-sectional vs longitudinal/experimental temporal information
- Identification, confounding, endogeneity, selection, common-method risk
- Model specification, alternative explanations, heterogeneity and robustness
- Statistical uncertainty and reporting completeness
- Directness of setting, level, and relationship to the proposed model

Do not invent numeric appraisal scores. Qualitative ratings can be used only with disclosed criteria and uncertainty.

## 5. Search and coverage log

| Date | Platform or source | Actual exact query or navigation route | Filters | Retrieved and retained counts if visible | Search limitation |
| --- | --- | --- | --- | --- | --- |

If ordinary web browsing is the only source, state this clearly. A bounded web-based integrative review is **not** an exhaustive systematic review. Do not fake deduplication counts, PRISMA flow, double screening, or formal meta-analysis.

## 6. Contradictions and saturation

Search for null, negative, curvilinear, contradictory and boundary-dependent findings. If these are not found, state that the executed search did not surface them, not that none exist. Use forward/backward searching where available. Stop expansion based on relevance and user scope, not on an arbitrary fixed citation count. Discuss evidence gaps proportionately.

## 7. Reference integrity

- Produce APA 7 entries only from verified metadata, never from intuition.
- Prefer DOI links in standard `https://doi.org/...` form when resolved.
- Never manufacture publication year, title, page numbers, quotation, scale provenance or DOI.
- Distinguish citations supporting a theoretical mechanism, empirical result, methodological rule and original construct definition.
- If the reference list is incomplete, explicitly list missing or unresolved records rather than silently guessing.