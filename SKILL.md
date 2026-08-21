---
name: bp-product-delivery
description: Transform MES, APS, PLM, PDM, IPS, ERP, OA, and other manufacturing business inputs into consistent, traceable product-delivery artifacts. Use when Codex must analyze requirements, meeting notes, screenshots, legacy PRDs, prototypes, field lists, business rules, or system documentation; create or optimize a PRD; model business processes, decision trees, states, and exceptions; build an interactive prototype; design ER models, Oracle DDL, data dictionaries, integrations, or OpenAPI/Swagger contracts; create test cases and acceptance criteria; review cross-artifact consistency; or assemble a complete manufacturing product delivery package.
---

# BP Product Delivery Orchestrator

Turn incomplete manufacturing business material into a decision-ready, implementable, and testable delivery package. Orchestrate the work as one traceable lifecycle instead of generating disconnected documents.

## Apply non-negotiable rules

- Preserve confirmed requirements and existing functions unless the user authorizes a change.
- Separate `confirmed fact`, `assumption`, `recommendation`, `open question`, and `conflict`.
- Never invent company-specific ownership, approval paths, field meanings, interfaces, algorithms, or source-of-truth systems.
- Ask only questions whose answers materially alter scope, rules, data, integration, security, or acceptance. Continue with labeled assumptions for non-blocking gaps.
- Reuse the same object names, codes, status values, units, identifiers, and rule definitions across every artifact.
- Make normal, abnormal, boundary, permission, concurrency, retry, and integration paths testable.
- Treat screenshots as evidence of visible UI only. Label inferred behavior.
- Create real requested artifacts instead of presenting pseudo-files in code fences when file output is requested.
- Write in the user's requested language; otherwise follow the language of the user's request.

## Route references progressively

Read only the references required for the request:

- Read [input-and-requirements.md](references/input-and-requirements.md) for raw requirements, meetings, screenshots, attachments, legacy documents, scope analysis, or requirement baselines.
- Read [prd-and-process.md](references/prd-and-process.md) for PRDs, business flows, swimlanes, state machines, decision trees, or rule specifications.
- Read [prototype-design.md](references/prototype-design.md) for high-fidelity, clickable, HTML, Axure-style, dashboard, form, list, or interaction prototypes.
- Read [data-and-integration.md](references/data-and-integration.md) for ER models, data dictionaries, Oracle SQL, APIs, idempotency, synchronization, or system boundaries.
- Read [testing-and-acceptance.md](references/testing-and-acceptance.md) for test cases, acceptance criteria, UAT, release gates, or regression scope.
- Read [manufacturing-domain.md](references/manufacturing-domain.md) for MES, APS, PLM/PDM/IPS, ERP, OA, BOM/BOP, routing, work order, WIP, capacity, scheduling, changeover, plan publication, or engineering change scenarios.
- Read [quality-gates.md](references/quality-gates.md) before reviewing or delivering two or more related artifacts.
- Read [deliverable-contracts.md](references/deliverable-contracts.md) when the user asks for a complete package, multiple files, named deliverables, or packaging.

Use templates in `assets/` as starting points when their format matches the requested deliverable. Do not preserve example rows or placeholder values in final outputs.

## Select the operating mode

Choose the smallest mode that satisfies the request:

1. **Analyze**: Extract facts, requirements, rules, scope, conflicts, gaps, and questions without designing unrequested solutions.
2. **Produce**: Create only the requested artifacts and their necessary dependencies.
3. **Review**: Diagnose quality, consistency, feasibility, or completeness without modifying artifacts unless asked.
4. **Update**: Apply a change, preserve unaffected content, identify downstream impact, and revise every affected artifact.
5. **Full delivery**: Produce the complete package defined in [deliverable-contracts.md](references/deliverable-contracts.md).

Do not expand a partial request into a full package. Do not treat a request to diagnose or review as authorization to rewrite.

## Establish the traceability model

Assign stable identifiers when the work spans multiple requirements or artifacts:

| Object | ID pattern |
|---|---|
| Requirement | `REQ-001` |
| Business rule | `RULE-001` |
| Field | `FIELD-001` |
| Process | `FLOW-001` |
| Status/state | `STATE-001` |
| Screen | `UI-001` |
| Data entity/table | `DATA-001` |
| Interface | `API-001` |
| Test case | `TC-001` |
| Acceptance criterion | `AC-001` |
| Open question | `Q-001` |

Maintain the chain `REQ → RULE/FLOW/UI → DATA/API → TC → AC`. Never renumber existing IDs during an update unless the user explicitly requests normalization.

## Execute the workflow

### 1. Register and normalize inputs

- List each source and what it can reliably establish.
- Extract actors, goals, scope, objects, fields, events, states, rules, integrations, constraints, exceptions, and success measures.
- Normalize synonyms only after recording the original terms.
- Detect contradictions across sources and prefer explicit, newer, approved material only when provenance supports that choice.

### 2. Build the requirement baseline

- Define business goal and measurable outcome.
- Define users, roles, permissions, and responsibility boundaries.
- Define in-scope, out-of-scope, dependencies, and constraints.
- Define current process, target process, business rules, data, states, exceptions, and integrations.
- Record assumptions, conflicts, open questions, and decisions.
- Preserve source traceability for important statements.

### 3. Apply the requirement gate

Block design only when a missing or conflicting answer changes a critical outcome, including:

- process ownership or approval authority;
- quantity, time, priority, allocation, capacity, or calculation rules;
- source-of-truth, synchronization, or interface behavior;
- state transitions, duplicate prevention, locking, concurrency, or rollback;
- security, audit, compliance, or acceptance conditions.

Ask one to three focused questions at a time. Otherwise state assumptions and proceed.

### 4. Plan dependent deliverables

Generate in dependency order:

1. requirement baseline;
2. PRD and rule specification;
3. process, swimlane, state, and decision visuals;
4. prototype and interaction specification;
5. data model and Oracle DDL;
6. integration and OpenAPI contract;
7. tests and acceptance criteria;
8. traceability matrix and delivery summary.

Skip unrequested items unless another requested artifact cannot be made coherent without them. Explain material omissions.

### 5. Create artifacts

- Honor requested formats such as Markdown, DOCX, XLSX, HTML, PDF, PPTX, SQL, YAML, or ZIP.
- Use the artifact workflow appropriate to each requested file type.
- Prefer tables for exact field, rule, mapping, status, and comparison data.
- Prefer Mermaid for process, state, ER, decision, integration, or sequence relationships when rendered diagrams materially improve understanding.
- Create high-fidelity prototypes with complete states and interactions, not static screenshots, when clickability is requested.
- Preserve existing artifact structure during updates unless restructuring is part of the request.

### 6. Run cross-artifact quality gates

Read [quality-gates.md](references/quality-gates.md) and verify:

- every confirmed requirement has a design destination;
- every rule has an implementation point and test coverage;
- UI fields match PRD, data model, and API definitions;
- object names, codes, types, units, precision, enums, and statuses are consistent;
- database constraints support integrity, idempotency, audit, and concurrency needs;
- API contracts cover success, validation, business rejection, retry, and duplicate requests;
- tests cover normal, abnormal, boundary, permission, integration, and recovery paths;
- assumptions and unresolved decisions remain visible.

Do not claim completeness when a blocking gate fails. Report the failed gate, affected artifacts, and required decision.

### 7. Deliver for decision and handoff

Lead with the outcome. Include:

- delivery scope and artifact list;
- key decisions and material changes;
- assumptions and open questions;
- risks and blocked gates;
- quality-gate result;
- clickable links to generated files.

For a full package, follow the standard names and manifest rules in [deliverable-contracts.md](references/deliverable-contracts.md), resolve the script path relative to this `SKILL.md`, then run:

```bash
python3 scripts/validate_delivery.py <delivery-directory> --profile full
```

Resolve errors before delivery. Explain warnings that remain intentionally.

## Handle changes safely

For a changed requirement:

1. Identify changed `REQ`, `RULE`, `FIELD`, `STATE`, or integration behavior.
2. Trace affected flows, screens, tables, APIs, tests, and acceptance criteria.
3. Preserve unaffected content and stable IDs.
4. Revise every affected artifact in dependency order.
5. Provide an impact summary and regression scope.

For existing materials, distinguish `retained`, `changed`, `added`, `removed`, and `needs decision`.
