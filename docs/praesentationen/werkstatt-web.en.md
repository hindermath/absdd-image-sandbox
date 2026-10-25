---
title: "Web application or MVC plus REST API"
lang: en-GB
date: 2026-10-25
---

<!-- slide: B01 -->
# Two routes to a web application

- Build a personal small product from Hello World
- Create, read, update and delete two required texts
- Choose requirements and architecture before using Spec Kit

::: notes
Read the introductory workshop first. Both routes produce web applications;
route B adds a separate REST API, not a replacement for the UI. References
show possible designs, not completed personal exercises. Use your own repo
and fictional data only.
:::

<!-- slide: B02 -->
# The product goal is shared

- CRUD: Create, Read, Update, Delete
- Two required fields and a generated ID
- Confirmed persistence and understandable errors
- No authentication or per-record permissions

::: notes
An ID identifies a record, not a user. This is a personal local instance.
Without authentication and permission rules, do not publish it as a shared
service. Predict whether a missing ID permits deleting any arbitrary row: no.
:::

<!-- slide: B03 -->
# Route A: MVC and data access in one process

- Browser sends a form or GET to MVC
- Razor generates HTML on the server
- Controller calls EF Core directly for SQLite
- No business REST call between controller and data access

::: notes
MVC means Model View Controller. EF Core is a data-access library; SQLite is
an embedded database. Flow: browser to MVC to EF Core to SQLite; data returns
and MVC sends HTML. All app components except the browser share a process.
Public C# methods are interfaces, but not automatically HTTP REST endpoints.
:::

<!-- slide: B04 -->
# Route B: MVC calls a REST API

- Browser receives HTML from MVC
- MVC's server client sends HTTP and JSON to the API
- Only the API accesses EF Core and SQLite
- Two app processes with a contract and failure boundaries

::: notes
API means Application Programming Interface. REST here is an HTTP resource
contract. Complete flow: browser to MVC/client to API to EF Core to SQLite;
back as JSON to MVC and HTML to browser. Browser JavaScript does not call the
API directly, so no extra CORS permission is needed for this architecture.
:::

<!-- slide: B05 -->
# Begin with a required capability

- Browser-only and compact entry: consider route A
- Agreed JSON access for more clients: consider route B
- Weigh effort, contracts and failure cases
- Neither route is universally better

::: notes
A must-have is necessary for the task to succeed. Another client could be a
CLI or later a different UI. Having an API proves neither higher security
nor scalability; route B is not automatically microservices. Name a downside
of your preferred route before deciding.
:::

<!-- slide: B06 -->
# Decide architecture and operation separately

- Both start as processes in the existing development sandbox
- SQLite uses the personal persistent project area
- PostgreSQL and separate app containers are later extensions
- No engine sockets, privileges or nested containers

::: notes
Reference documents may call execution directly on the developer host native.
Here execution is inside the existing Linux development container, not a new
app image. REST does not require containers; containers do not require REST
or PostgreSQL. A persistent volume is not a backup.
:::

<!-- slide: B07 -->
# Record your decision

- Goal, users and required capabilities
- Chosen route and rejected alternative
- Downsides, risks and expected evidence
- A trigger for reassessment

::: notes
Open decision.md in the selected package. Case A: personal browser notes, no
other clients and limited learning time. Case B: browser plus agreed JSON
access for another program. Justify both without code first. This records
assumptions and a choice, not product approval or accepted risk.
:::

<!-- slide: B08 -->
# Select exactly one practice package

- A: form → SQLite CRUD → errors/usability → closure
- B: API contract → API SQLite → MVC client → closure
- Both start Pending and need personal review
- The other route is not a prerequisite

::: notes
Pending means not started. Shipped series are Draft, neither activated nor
accepted. ReadyForReview in an authoring receipt means reviewable content only.
The order document explains every dependency in text. Never dispatch both
routes as competing writers to the same personal project.
:::

<!-- slide: B09 -->
# Spec Kit structures the personal request

- Review project principles and intake before Specify
- Clarify material decisions
- Plan, Checklist and Tasks prepare implementation
- Analyze is read-only; Implement needs explicit authority

::: notes
Use the selected intake's full prompts. Plan safety and tests from stage 0.
Examples grant no provider/model configuration or Git-delivery authority.
Guided individual steps are the starting route. Autonomous is a separately
authorized alternative, not the default way to learn.
:::

<!-- slide: B10 -->
# Route A: from form to confirmed record

- Start with clearly labelled fixture preview
- Add EF Core and a personal SQLite file
- Confirm success only after the write commits
- Cancel and invalid input change nothing

::: notes
A draft is not persisted data. SaveChanges is the write point, not merely
adding an object to a context. Tests use separate DBs. Confirmed data must
survive process restart. Redirected build output is not database storage.
:::

<!-- slide: B11 -->
# Route B: understand the HTTP contract first

- GET reads, POST creates, PUT replaces, DELETE removes
- Success: 200, 201 with Location or 204 without body
- Errors: 400, 404, 413, 429 or generic 500
- OpenAPI must match real HTTP tests

::: notes
A status code summarizes the technical result. Location points to a created
record. DTO means data transfer object: expose agreed fields, not internal
database entities. An expected 400 is a passing negative test only when the
rejection and unchanged data are checked. Persistence follows later.
:::

<!-- slide: B12 -->
# Route B adds a real failure boundary

- API outage is not a successful empty collection
- Valid JSON syntax does not prove a valid record
- Distinguish ten-second timeout and deliberate cancellation
- Never automatically retry uncertain writes

::: notes
Timeout stops waiting; the API may already have saved. Preserve the draft,
read the collection deliberately and then decide. Test invalid statuses/IDs,
broken JSON and connection failures. Never stop or modify another person's
instance to perform these exercises.
:::

<!-- slide: B13 -->
# Protections apply from the first stage

- HTTPS with deliberately prepared trust
- Server validation, encoding and form protection
- Body/write limits and safe errors/logs
- These controls do not replace user permissions

::: notes
HTML encoding renders markup as text. Antiforgery connects form token and
cookie; CSP constrains browser content. No TLS disabling, trust-all callback
or blanket curl -k. Missing trusted certificates stop execution, not reading
or planning. MVC uses port 5111, API 5112; bind 0.0.0.0 inside the container,
but publish only to host loopback.
:::

<!-- slide: B14 -->
# Interpret test evidence correctly

- Unit: isolated logic
- HTTP/integration: real boundaries and SQLite
- UI: observe keyboard, labels, focus and errors
- Coverage per app is not complete quality or A11Y acceptance

::: notes
Require at least 70 % own C# line coverage per application on route B, not
only an aggregate; route A uses the same threshold for its one app. Document
scope. Windows, Ubuntu/WSL2 and macOS need separate evidence. Historical
reference results are not current local tests. Mark unperformed measurements
or human checks Open with owner, follow-up and trigger.
:::

<!-- slide: B15 -->
# Explain a case from your occupation

- Development: connect validation and tests
- Integration/networking/electronics: process and port boundaries
- Data analysis: trace a form value to a stored row
- IT management: weigh value, effort and handover

::: notes
Select a task from the workshop index. Basic: create one fictional entry and
explain the full flow without unexplained abbreviations. Extension: describe
an API/DB outage as a sequence of states with suitable evidence. All seven
occupational perspectives use the same protections.
:::

<!-- slide: B16 -->
# Move from presentation to practice

- Complete the decision and copy exactly one package
- Review the whole series and decide on start
- Plan the first stage, then explicitly authorize implementation
- Progress after acceptance, not a green check alone

::: notes
A later sandbox template never replaces the empty product repo or activates
a personal intake series. The profile is not enabled. Choose
[MVC](../lernwerkstaetten/web-mvc/README.md) or
[MVC plus REST](../lernwerkstaetten/web-rest/README.md).
The [transfer and workflow guide](../lernwerkstaetten/README.md) explains the
steps. Instructor answers are separate. This presentation builds or starts
nothing and grants no commit, push or public-release authority.
:::
