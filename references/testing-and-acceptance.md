# Testing and Acceptance

Use this reference to turn requirements and rules into executable verification.

## Build coverage from traceability

Create at least one test for every confirmed requirement and rule. Add targeted tests for each status transition, permission boundary, interface error, and material assumption.

Use categories:

- happy path;
- alternate path;
- business rejection;
- boundary and exact threshold;
- null, invalid, duplicate, and oversized input;
- role and data permission;
- concurrency and optimistic conflict;
- idempotent retry;
- integration timeout, partial success, duplicate, and out-of-order response;
- lock/freeze/publish/cancel behavior;
- data reconciliation and stale display;
- performance, volume, audit, and recovery;
- backward compatibility and regression.

## Specify each test case

Include:

- `TC-xxx`, title, priority, test level;
- linked `REQ/RULE/API/STATE` IDs;
- preconditions and test data;
- steps and expected result per meaningful step;
- expected database, interface, status, and audit side effects;
- cleanup or reset needs;
- automation suitability;
- execution status and evidence placeholder when requested.

Avoid cases that merely repeat requirement text without test data or observable outcomes.

## Test dense manufacturing logic

For allocation, capacity, scheduling, changeover, lead time, contract balance, work-order creation, or publication:

- test zero, minimum, maximum, exact threshold, and just-below/above values;
- test multiple matching rules and rule priority;
- test manual override, persistence, reset, and audit;
- test locked/frozen objects and downstream impact;
- test simultaneous users and repeated requests;
- test source-data refresh during editing or submission;
- test partial downstream success and reconciliation;
- verify quantities, units, precision, dates, calendar, and timezone.

## Write acceptance criteria

Use observable business outcomes. Prefer:

`Given <state/data/role>, when <action/event>, then <visible result>, and <stored/integration/audit effect>.`

Include performance or volume figures only when confirmed or explicitly proposed as assumptions.

## Define release gates

Require:

- no unresolved blocking requirement conflict;
- critical and high-priority tests passed;
- data migration/reconciliation accepted when applicable;
- interface negative paths verified;
- permissions and audit verified;
- rollback/contingency prepared for consequential releases;
- known limitations documented and accepted by an owner.

