# PRD, Process, and Rule Design

Use this reference for product specifications and exact business logic.

## Structure the PRD

Include only relevant sections:

1. document control and change summary;
2. background, problem, goal, KPI;
3. users, roles, permissions;
4. scope, exclusions, assumptions, dependencies;
5. glossary and object model;
6. current process and pain points;
7. target process and business scenarios;
8. functional requirements by module;
9. rule catalogue and priority;
10. state model and exception handling;
11. UI/interaction requirements;
12. data, integration, and migration requirements;
13. non-functional requirements;
14. analytics, audit, and operational support;
15. acceptance criteria, release plan, risk, and open questions.

Avoid vague verbs such as “support,” “optimize,” or “process” without stating inputs, conditions, behavior, output, and failure handling.

## Specify a rule completely

For each `RULE-xxx`, define:

- name and purpose;
- applicable object and scope;
- trigger and preconditions;
- condition expression;
- calculation, priority, or decision;
- output and side effects;
- exception/default behavior;
- manual override and persistence behavior;
- effective time/version;
- examples and boundaries;
- corresponding tests.

Detect overlaps and contradictions. Provide a priority table when multiple rules can match.

## Choose the right process visual

| Need | Visual |
|---|---|
| End-to-end business sequence | Flowchart |
| Responsibilities across systems/roles | Swimlane |
| Object lifecycle | State diagram |
| Conditional classification | Decision tree/table |
| API or integration interaction | Sequence diagram |
| Data ownership/relationships | ER diagram |

Show normal and meaningful exception paths. Do not produce decorative diagrams that duplicate a short list.

## Model states precisely

Define state code, display name, entry condition, allowed actions, allowed next states, terminal status, reversibility, lock behavior, audit event, and invalid transition response.

Separate:

- business status from interface-processing status;
- plan lifecycle from execution lifecycle;
- current value from historical version;
- soft deletion from business cancellation.

## Create a decision table when logic is dense

Use one row per mutually exclusive condition combination. Include priority and fallback. Confirm whether rules use first-match, best-match, or cumulative application.

For time-based rules, specify timezone, inclusive/exclusive boundary, calendar type, precision, and behavior at exactly the threshold.

## Keep acceptance close to design

Attach acceptance criteria to each major function. Use observable behavior:

`Given <precondition>, when <event>, then <result>, and <side effect/audit behavior>.`

