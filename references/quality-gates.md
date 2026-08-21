# Cross-Artifact Quality Gates

Use these gates before delivering two or more related artifacts.

## Gate levels

| Result | Meaning | Action |
|---|---|---|
| Pass | Complete and consistent for current scope | Deliver |
| Pass with assumptions | Implementable if listed assumptions are accepted | Deliver with assumptions highlighted |
| Warning | Non-blocking gap or improvement | Deliver with risk and owner |
| Blocked | Material decision, conflict, integrity, security, or acceptance gap | Do not claim completion |

## G0 — Evidence and scope

- Sources and versions are identifiable.
- Confirmed facts are separated from inference.
- Scope, exclusions, goal, users, and deliverables are clear.
- Existing functions have been inventoried for redesign work.

## G1 — Requirement quality

- Requirements are atomic, uniquely identified, and testable.
- Rules specify condition, priority, output, exception, and boundary.
- States and transitions are complete.
- Critical conflicts and open questions have impact and owner.
- Non-functional and operational needs are not omitted.

## G2 — Product consistency

- PRD, flows, decision tables, state model, and prototype express the same behavior.
- Screen actions have eligibility, validation, success, failure, and recovery.
- Field labels/codes, requiredness, editability, defaults, and units match.
- Permissions and audit behavior are visible where consequential.

## G3 — Technical implementability

- Every persistent object has an owner, identifier, lifecycle, and history strategy.
- Oracle types, constraints, indexes, and precision reflect usage.
- API schemas and enums match UI and data design.
- Idempotency, concurrency, retry, partial failure, and reconciliation are defined.
- Source-of-truth and synchronization semantics are explicit.

## G4 — Testability and acceptance

- Every `REQ` and `RULE` maps to at least one `TC` and `AC`.
- Normal, exception, boundary, permission, concurrency, and integration cases exist.
- Expected UI, data, status, interface, and audit effects are observable.
- Release, rollback, and known limitation decisions exist where needed.

## G5 — Package integrity

- Requested files exist, open, and contain no unresolved placeholders unless reported.
- Links and diagrams render.
- Stable IDs are unique and traceable.
- The summary reflects actual artifacts and unresolved risks.
- No artifact claims approval, test execution, production readiness, or compatibility without evidence.

## Required cross-checks

| Compare | Verify |
|---|---|
| Requirement ↔ PRD | No confirmed requirement is lost |
| PRD ↔ Flow | Conditions, roles, sequence, exceptions |
| PRD ↔ Prototype | Functions, fields, permissions, messages |
| Prototype ↔ API | Payload, validation, async state, errors |
| API ↔ Data | Names, types, precision, enums, keys |
| Rules ↔ Tests | Priority, boundary, default, override |
| State model ↔ All | Codes, transitions, terminal/locked behavior |

## Report gate results

For each failed or warning gate, report: gate, issue, evidence, affected artifacts, business/technical impact, recommended action, decision owner, and blocking status.

