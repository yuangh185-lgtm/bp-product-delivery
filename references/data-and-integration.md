# Data and Integration Design

Use this reference for data models, Oracle DDL, system integration, and OpenAPI contracts.

## Establish system ownership

For every important object and field, define:

- source-of-truth system;
- creator and updater;
- synchronization direction and frequency;
- effective-time and version semantics;
- local cache or snapshot behavior;
- conflict resolution and reconciliation;
- retention and audit requirements.

Never infer that ERP, PLM, APS, or MES owns an object solely from common practice.

## Design the logical model

Separate as needed:

- master data;
- transactional data;
- plan/version data;
- relationship/allocation data;
- status history;
- integration request/response logs;
- audit and operation logs;
- import batches and row errors;
- configuration and rule versions.

Model many-to-many allocations explicitly. Preserve business-effective history when values can change after approval or publication.

## Design Oracle DDL

Define:

- stable primary keys and business unique constraints;
- `VARCHAR2` lengths, `NUMBER(p,s)` precision, and timestamp semantics;
- `NOT NULL`, `CHECK`, foreign key, and unique constraints where enforceable;
- optimistic-lock/version column for concurrent edits;
- created/updated user and timestamp;
- business status and deletion marker only when both are needed;
- indexes derived from real query/filter/join patterns;
- table and column comments;
- sequence/identity strategy compatible with the target Oracle version.

Do not use floating types for business quantities requiring decimal precision. Define unit and rounding policy outside the physical type.

## Design idempotent writes

For create, publish, allocate, release, or integration actions:

- define an idempotency/business request key;
- enforce uniqueness at the persistence layer where possible;
- state retry behavior and response replay semantics;
- separate technical retry from business re-submission;
- record request, response, status, attempt count, timestamps, and correlation ID.

## Design synchronization

Specify full/incremental mode, trigger/frequency, pagination, ordering, effective timestamp, retry, dead-letter handling, reconciliation, alerting, and stale-data UX.

If the UI displays the last synchronized value while a write is pending, define the pending reservation or local ledger needed to prevent over-allocation.

## Design OpenAPI contracts

For each `API-xxx`, define:

- purpose, consumer, provider, method, path, permission;
- request/response schema with examples;
- validation and business rule errors;
- idempotency and concurrency headers/fields;
- pagination, filtering, sorting, and batch limits;
- HTTP status and stable business error code;
- timeout, retry, correlation, audit, and observability behavior;
- compatibility/versioning policy.

Keep schema names, enums, units, and field types aligned with the PRD, UI, and data dictionary.

## Review integration boundaries

Check mapping completeness, code translation, timezone, encoding, null/empty semantics, duplicate events, out-of-order delivery, partial batch failure, replay, rollback/compensation, monitoring, and ownership of recovery.

