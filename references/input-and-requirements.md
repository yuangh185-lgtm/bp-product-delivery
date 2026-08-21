# Input and Requirement Baseline

Use this reference to turn mixed business evidence into a stable baseline.

## Build a source register

Record for each source:

| Attribute | Meaning |
|---|---|
| Source ID | `SRC-001` |
| Type | Meeting, screenshot, PRD, prototype, spreadsheet, log, SOP, message |
| Date/version | Evidence freshness |
| Owner/status | Draft, confirmed, approved, obsolete, unknown |
| Reliable facts | What the source directly establishes |
| Limitations | Missing context or inferred behavior |

Prefer approved and current evidence, but do not silently discard conflicts.

## Extract the requirement model

Capture:

- business problem, goal, KPI, and success condition;
- actors, roles, permissions, and responsibility boundaries;
- trigger, preconditions, main flow, alternate flow, exception, and postcondition;
- business objects, identifiers, fields, units, precision, and ownership;
- rules, priority, effective time, manual overrides, defaults, and conflict handling;
- states, allowed transitions, reversibility, lock/freeze behavior, and history;
- upstream/downstream systems, source-of-truth, frequency, latency, and reconciliation;
- non-functional needs: volume, performance, availability, security, audit, retention;
- scope, exclusions, dependency, risk, assumption, question, and decision.

## Classify every material statement

| Class | Treatment |
|---|---|
| Confirmed fact | Use directly and retain provenance |
| Assumption | Label and include validation owner/date when possible |
| Recommendation | Explain rationale and tradeoff |
| Open question | Assign `Q-xxx`, impact, owner, and blocking level |
| Conflict | Show competing statements and recommend a resolution path |

## Ask only material questions

Ask when the answer changes scope, data integrity, rule outcome, interface contract, permission, release risk, or acceptance. Group questions by decision and present one to three at a time.

Do not block on wording, optional display details, or a reversible convention. Choose a reasonable default, label it, and proceed.

## Produce the baseline

Include:

1. background and goal;
2. users and stakeholders;
3. scope and exclusions;
4. glossary and canonical object names;
5. current and target process;
6. functional requirements;
7. business rules;
8. data and integration needs;
9. states and exceptions;
10. non-functional requirements;
11. assumptions, conflicts, open questions, risks, and decisions;
12. source traceability.

Write each requirement so it has one actor or system behavior, a testable outcome, and an ID. Split compound requirements.

## Preserve legacy behavior

When updating an existing system or prototype:

- inventory existing functions before redesign;
- treat visible UI as evidence, not proof of backend behavior;
- identify retained, changed, added, removed, and uncertain behavior;
- do not remove a function merely because it seems redundant;
- call out backward compatibility, migration, and regression impact.

