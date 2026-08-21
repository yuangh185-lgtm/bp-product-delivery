# Manufacturing Prototype Design

Use this reference for interactive product prototypes.

## Translate requirements into screens

Create a screen inventory before implementation. Map each `UI-xxx` to requirements, roles, entry path, primary action, fields, statuses, and error states.

For manufacturing management systems, consider:

- workspace/factory/workshop filters;
- plan version and effective date;
- product/material/order/work-order identifiers;
- status, exception, lock, publish, and synchronization indicators;
- bulk selection, import/export, create, validate, submit, approve, publish, cancel, retry;
- list, detail, edit, log, history, compare, and audit views.

Do not add domain fields that are not supported by requirements or clearly labeled assumptions.

## Build complete UI states

Implement when relevant:

- loading, empty, populated, filtered, and no-result states;
- validation, business rejection, permission denial, network failure, partial success, and retry;
- disabled, read-only, locked, frozen, published, cancelled, and completed states;
- unsaved changes, confirmation, duplicate submission, optimistic conflict, and stale-data warning;
- import validation, row-level errors, and downloadable error details.

## Specify fields and interactions

For each field, define label, code, data type, unit, source, requiredness, editability, default, validation, display format, permission, and persistence timing.

For every action, define:

- eligibility and disabled reason;
- confirmation requirement;
- request payload and idempotency behavior;
- success result and refresh behavior;
- failure message and recovery;
- log/audit event.

## Design data-heavy pages

- Keep identifiers and exceptions visible.
- Freeze key columns when tables are wide.
- Distinguish system-calculated and manually entered values.
- Show selected-row count and batch eligibility before bulk actions.
- Prevent duplicate operations with both UI state and backend idempotency.
- Provide request/response logs for critical integration actions when required.
- Make stale synchronized data visible when users can act on it.

## Build high-fidelity clickable output

When clickability is requested:

- implement navigation, filters, dialogs, tabs, selection, validation, and feedback;
- use realistic but clearly synthetic manufacturing data;
- preserve all confirmed functions from the source prototype;
- use responsive layout where the target environment requires it;
- verify the rendered result visually and exercise the main path plus critical exceptions.

Do not claim Axure compatibility unless producing an actual compatible artifact. Use “Axure-style” only for visual/interaction similarity.

