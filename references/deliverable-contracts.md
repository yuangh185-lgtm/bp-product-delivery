# Deliverable Contracts

Use this reference for multi-file and full-package delivery.

## Standard full package

Create the following when the user asks for a complete product delivery package:

| Path | Required content |
|---|---|
| `01-requirement-baseline.md` | Scope, actors, requirements, rules, data, states, questions |
| `02-prd.md` or `.docx` | Product design specification |
| `03-process-and-rules.md` | Flows, swimlanes, states, decisions, rule catalogue |
| `04-prototype/` or `04-prototype.html` | Clickable UI when requested/applicable |
| `05-data-design.md` | ER model and data dictionary |
| `06-oracle.sql` | Executable Oracle DDL when requested/applicable |
| `07-openapi.yaml` | Valid OpenAPI contract when requested/applicable |
| `08-test-cases.csv` or `.xlsx` | Traceable test cases |
| `09-acceptance.md` | UAT and release acceptance criteria |
| `10-traceability.csv` or `.xlsx` | Requirement-to-acceptance mapping |
| `delivery-manifest.json` | Artifact inventory, status, assumptions, warnings |

Mark a non-applicable technical artifact in the manifest instead of inventing content. A full package may omit prototype, DDL, or OpenAPI only when the request excludes it or the available evidence cannot support it; explain the reason.

## Partial delivery

Create only requested files and necessary dependencies. Include a concise handoff summary with scope, assumptions, open questions, and affected downstream artifacts.

## Manifest contract

Include:

- package name, version, generated date, and status;
- source list and source versions;
- artifact path, type, status, and covered IDs;
- assumptions, warnings, blocked gates, and open questions;
- validation result and intentionally omitted artifacts.

Use `assets/delivery-manifest.template.json` as the starting structure.

## Template routing

- Use `assets/prd-template.md` for a Markdown PRD.
- Use `assets/oracle-ddl-template.sql` for Oracle DDL structure.
- Use `assets/openapi-template.yaml` for OpenAPI structure.
- Use `assets/test-case-template.csv` for test cases.
- Use `assets/traceability-matrix.csv` for traceability.

Remove all examples and placeholders. Validate machine-readable files before delivery.

## Packaging rules

- Use consistent encoding, preferably UTF-8.
- Use relative links inside the package.
- Keep generated temporary, cache, and preview files out of the package.
- Do not package source material unless the user requests it and has authority to redistribute it.
- Preserve user-provided originals separately from transformed deliverables.
- Provide a ZIP only when requested.

## Validate

Run `scripts/validate_delivery.py <directory> --profile full` for the standard package. The validator checks expected artifact groups, empty files, unresolved placeholders, traceability headers, and duplicate IDs. Treat reported errors as blocking and warnings as review items.

