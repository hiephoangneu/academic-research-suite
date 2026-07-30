---
name: citation-integrity-auditor
description: Verify the validity, existence, bibliographic accuracy, DOI and URL resolution, claim support, in-text and reference-list matching, and formatting of citations in academic manuscripts, proposals, reviews, and teaching materials. Use for exhaustive citation audits, suspected fabricated references, APA 7 repair, reference-list reconstruction, or identifying unsupported claims. Current web verification is required for external-source claims; do not rely on memory alone.
---

# Citation Integrity Auditor

## Define the audit scope

1. Determine whether the user requests bibliographic verification, claim-level verification, citation-reference reconciliation, formatting repair, or all four.
2. Extract every in-text citation and every reference-list entry from the complete supplied document.
3. Preserve the original text and maintain a one-to-one audit ledger.
4. State any inaccessible sources, unreadable pages, or incomplete document regions.

## Verify each source

Use this priority:

1. Publisher or journal page
2. DOI registration record
3. Official institutional or government source
4. Trusted bibliographic database
5. Author repository or indexed scholarly profile
6. Secondary discovery source only for locating stronger evidence

For each reference, verify:

- authors and order
- year
- title
- source title
- volume, issue, pages or article number
- DOI or stable URL
- publication type
- retraction, correction, or expression-of-concern status when material

Opening a DOI is insufficient. Compare the resolved metadata with the cited entry.

## Verify citation use

1. Confirm that each in-text citation appears in the reference list and each reference is cited in text.
2. Check whether the source supports the nearby claim.
3. Distinguish direct support, partial support, contextual relevance, contradiction, and no demonstrated support.
4. Flag secondary citations presented as primary evidence.
5. Flag citations whose design, sample, construct, or context cannot support the asserted generalisation.
6. Do not infer source support from title similarity alone.

## Classify findings

Use only these categories:

- Verified and accurate
- Verified with minor bibliographic error
- Verified with material bibliographic mismatch
- Exists but does not support the cited claim
- Unverifiable with available authoritative evidence
- Likely fabricated
- Retracted, corrected, or otherwise status-sensitive

Reserve “fabricated” for strong evidence. State the search evidence and uncertainty when verification fails.

## Repair

1. Provide a corrected reference only when authoritative metadata supports it.
2. Preserve the required citation style and language conventions.
3. Identify the exact in-text locations requiring changes.
4. Do not replace a problematic source with a new source unless it genuinely supports the original claim.
5. Never invent a DOI for a source that has none.

## Output

Return:

1. Audit coverage and limitations
2. Summary counts by classification
3. Reference-level verification table
4. Claim-level support problems
5. In-text and reference-list mismatches
6. Corrected entries
7. Priority actions

Read [references/citation-verification-protocol.md](references/citation-verification-protocol.md) for the evidence hierarchy, audit fields, and APA 7 repair checks.
