# MES, APS, PLM, and ERP Domain Reference

Use this reference as a checklist, not as proof of a company's actual architecture. Confirm local ownership and terminology.

## Typical responsibility boundaries

| System | Common responsibility | Confirm explicitly |
|---|---|---|
| PLM/PDM/IPS | Product definition, design, BOM/BOP, routing, documents, engineering change | Which object is authoritative and at what lifecycle state |
| ERP | Material, demand, sales/purchase contract, inventory accounting, procurement, finance | Whether operational balance and reservation are real time |
| APS | Demand/capacity preparation, constraint-based scheduling, plan version, simulation, adjustment, validation, publication | Algorithm boundary, frozen horizon, version and publish semantics |
| MES | Work order execution, dispatch, WIP, equipment/operation reporting, genealogy, quality feedback | Whether MES creates, releases, or only executes work orders |
| OA/BPM | Approval, task, notification, organizational routing | Whether approval status is authoritative or mirrored |

Do not copy this table into a final design without validating the target organization.

## Common manufacturing objects

- organization: company, factory, workshop, line, work center, machine;
- product: product/model, material, revision, BOM, BOP, routing, operation;
- resource: equipment, tooling, mold, labor/skill, calendar, shift, capacity;
- demand: forecast, sales order, contract, delivery, production demand;
- execution: work order, operation order, dispatch task, lot/batch, WIP;
- planning: plan version, horizon, scheduling task, machine slot, frozen/locked segment;
- rule/configuration: priority, eligibility, changeover matrix, lead time, yield, capacity rate;
- quality/change: inspection, deviation, nonconformance, engineering change, effective date;
- integration: sync batch, request log, response log, reconciliation result.

## End-to-end questions

For every flow, confirm:

1. Who creates the demand and which version is effective?
2. Which master data/revision was used?
3. Which constraints are hard, soft, configurable, or advisory?
4. What is calculated automatically and what may be edited manually?
5. What becomes locked, frozen, approved, released, or published?
6. What downstream system consumes the result?
7. How are rejection, delay, partial success, cancellation, and rework handled?
8. How can a user trace the result back to demand, rule version, and source data?

## APS and scheduling controls

Explicitly define:

- planning horizon and time bucket;
- demand selection and priority;
- eligible equipment and alternate resource;
- calendar, downtime, maintenance, and shift capacity;
- routing, lead time, yield/scrap, lot-size, split/merge rules;
- material, tooling, labor, and quality constraints;
- sequence dependency and changeover classification/duration;
- locked task, frozen horizon, manual override, and drag behavior;
- rescheduling scope after insert, move, delete, or data refresh;
- plan validation, approval, publication, supersession, and rollback;
- algorithm timeout, infeasible result, explanation, and manual recovery.

Treat local codes such as changeover types as configuration. Define priority among manual designation, sample/special material, same-material interval, reference-table matching, and default rules from confirmed requirements rather than assumed industry practice.

## MES and work-order controls

Explicitly define quantity source, remaining/available balance, allocation order, repeated creation limit, idempotency key, release status, cancellation/return, material revision, route version, lot rules, downstream response, audit log, and reconciliation.

If balances arrive by periodic synchronization, distinguish:

- last synchronized balance;
- locally reserved or pending quantity;
- confirmed consumed quantity;
- available-to-create quantity;
- next reconciliation result.

## PLM/PDM/IPS controls

Explicitly define revision, lifecycle state, effectivity, approval, ownership, baseline, BOM/BOP/routing consistency, document linkage, engineering change propagation, obsolete revision handling, and downstream acknowledgement.

## Cross-system quality risks

Check mismatched codes, stale revisions, missing mappings, unit conversion, timezone/calendar difference, duplicate messages, out-of-order updates, partial batches, eventual consistency, manual corrections, replay, and unclear recovery ownership.

