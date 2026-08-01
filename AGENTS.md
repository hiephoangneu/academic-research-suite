# Academic Research Suite Maintenance

## Repository expectations

- Preserve the nine-skill architecture and keep each trigger boundary distinct.
- Never add instructions that permit fabricated citations, data, results, page numbers, or completed changes.
- Treat journal policies, rankings, regulations, software behaviour, and reporting standards as time-sensitive.
- Require primary or authoritative sources when current verification matters.
- Avoid em dashes in generated prose and plugin documentation.
- Keep every `SKILL.md` under 500 lines and use one-level-deep references for detailed criteria.
- Preserve vendored upstream files byte-for-byte; apply compatibility and safety rules in the wrapper skill.
- Run the suite validator and all skill validators after changing behaviour.

## Code review rules

- Flag conflicting instructions across skills.
- Flag broken local references, leftover placeholders, invalid frontmatter, or stale UI metadata.
- Flag any audit workflow that edits source material without explicit authorisation.
- Flag any response workflow that reports proposed changes as completed changes.
- Flag any method workflow that encourages significance engineering, undisclosed data manipulation, or causal claims unsupported by identification.
