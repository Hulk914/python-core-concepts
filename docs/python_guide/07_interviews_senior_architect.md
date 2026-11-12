# Senior · memory ownership and object design
Section: Mock interview · senior

## S01 · A process grows in memory although objects are deleted. Diagnose it.

**Answer:** first distinguish rising resident memory from growing reachable Python allocations. `del` removes a binding, not every reference. Inspect caches, closure cells, generator frames, queues, event handlers and container graphs that may still retain objects. Cycles may require cyclic collection in CPython; native libraries and allocator reuse complicate process-memory interpretation.

Reproduce with a bounded representative workload. Take `tracemalloc` snapshots before and after repeated operations and compare allocation sites. Start tracing before the suspected allocations. Correlate with process metrics if native allocations matter. `sys.getsizeof()` is shallow and cannot by itself measure a retained graph; shared references also make naive recursive sums inaccurate.

Remove the unintended owner, bound a cache/queue or shorten a resource lifetime. Verify memory reaches an acceptable steady state after repeated workloads. Do not simply insert `gc.collect()` in a hot loop without evidence: it cannot free an object that remains reachable and can add latency.

**Follow-up answered:** a generator can hold a large source even after yielding one small result. Exhausting or deliberately closing it can release frame references, depending on remaining owners. Strong diagnosis identifies what retains data and measures the fix rather than inferring a leak from one process-memory reading.

## S02 · Design a mutable domain object with reliable equality and hashing.

**Answer:** decide whether equality represents entity identity or complete value equality. For a task entity, a stable identifier may define identity, while title and done are mutable state. For a value object, equality may use all fields, favoring immutable contents. Document cross-type behavior and return `NotImplemented` for unsupported comparisons where appropriate.

Never derive a stored dictionary key's hash from fields that can change. A mutable value-equal dataclass is normally unhashable, which prevents this hazard. Prefer an immutable stable key such as a validated task ID for indexes, or an immutable value object with hashable fields when value hashing is required. `frozen=True` alone does not make nested objects immutable or every instance hashable.

**Follow-up answered:** `Task` currently has generated field equality and no durable cross-process identity semantics beyond its stored integer ID. If introducing entity equality, update tests and callers that rely on current value comparison. A strong answer considers migration of behavior and avoids `unsafe_hash=True` as a superficial workaround.

Repo: `generators.py`, `model.py`. References: [[R06]], [[R14]], [[R36]].

<!-- page -->
# Senior · profiling and cache correctness
Section: Mock interview · senior

## S03 · A Python data transform is slow. What do you measure and change?

**Answer:** define a representative workload and a target: throughput, tail latency or memory. Record Python implementation/build, data distribution and I/O conditions. Profile the end-to-end path to distinguish parsing, computation, waiting and output. Use repeated microbenchmarks only after identifying a narrow candidate; a tiny faster expression may not affect total runtime.

Look for algorithmic causes first: nested membership scans, repeated sorting, repeated serialization or unnecessary copies. A set index can replace linear membership if hashability and equality meet the contract. A generator can reduce intermediate allocation, but it does not eliminate consumed work and may shift errors. Include data sizes large enough to expose growth behavior.

Verify the same output, ordering, mutation and exception contracts after the change. Report a measured comparison with uncertainty rather than a universal speed claim. If the bottleneck is external I/O, reducing Python arithmetic may have no meaningful effect.

**Follow-up answered:** compare cumulative profiler time to understand expensive call subtrees, but account for instrumentation overhead. Strong answers describe how they would reject an optimization when representative measurements show no worthwhile benefit.

## S04 · What can go wrong with lru_cache on a useful helper?

**Answer:** a cache is correct only when its key represents every relevant input and results remain valid for the intended lifetime. Hidden global configuration, file contents or current time can make cached results stale. Arguments must be hashable; returned mutable objects may be shared across callers. Bound entry count does not bound bytes when value sizes vary widely.

Define invalidation, maximum memory, hit-rate goals and ownership of returned values. For mutable results, return immutable representations or intentional copies if that cost is acceptable. For methods, cache keys can retain instances. Concurrent misses can compute more than once even when cache bookkeeping is synchronized, so side effects still need a separate policy.

Do not cache tracker file loads without a reliable change/version signal; otherwise another process's updates can be hidden. For pure expensive calculations, standard caching may be ideal. Measure hit rate and compute cost to confirm the tradeoff.

**Follow-up answered:** caching exceptions or transient failures requires an explicit policy and expiry; a normal result cache is not automatically a negative-cache strategy. Strong answers explain both correctness and operational visibility.

References: [[R34]], [[R35]], [[R11]].

<!-- page -->
# Senior · concurrency and cancellation
Section: Mock interview · senior

## S05 · Does the GIL make a shared counter or tracker update safe?

**Answer:** no. In conventional GIL-enabled CPython, the GIL limits simultaneous Python bytecode execution, but a multi-step invariant can still be interleaved. A read/check/compute/write sequence is not made transactional by the GIL. Native operations can release it, and free-threaded builds change the execution model further.

Use a lock around the complete shared-memory invariant, not merely the last assignment. For several processes updating a file, a thread lock is insufficient. Even an interprocess lock must cover read, validate, modify and commit, with all writers participating. A database transaction is often clearer when concurrent persistent updates are a real requirement.

State the interpreter configuration. Free-threaded CPython began in 3.13 and has supported status in 3.14 under PEP 779, but the runtime build and extension ecosystem matter. Test shared-state assumptions on the deployed build rather than asserting “Python cannot run threads in parallel.”

**Follow-up answered:** atomicity of a single container operation does not establish correctness of a business sequence. Strong answers locate the invariant, its owners and the scope over which synchronization must hold.

## S06 · How do you keep an async pipeline bounded and cancellable?

**Answer:** use asynchronous libraries for I/O that actually cooperate with the event loop. Bound concurrent tasks and queue sizes so an input spike cannot create unlimited retained work. Apply deadlines and propagate cancellation through task ownership. Use `try/finally` or async context managers to release resources; do not swallow cancellation as an ordinary retryable error.

Blocking calls stall the loop even when placed inside `async def`. Move suitable blocking I/O to a controlled thread executor or use an async API. For CPU-heavy Python work, consider a process pool or a verified free-threaded/native strategy, accounting for serialization and deployment constraints. Offloading does not make the underlying operation instantly cancellable.

**Follow-up answered:** a client timeout can occur after a persistent change committed. Cancellation therefore needs an operation/result contract, not just task cleanup. Use idempotency or a way to query the outcome when retries can duplicate work. Strong answers distinguish stopping a waiter from reversing an external side effect.

References: [[R30]], [[R39]], [[R43]], [[R31]], [[R32]].

<!-- page -->
# Senior · persistence and schema evolution
Section: Mock interview · senior

## S07 · Why doesn't the tracker's file replacement prevent lost updates?

**Answer:** replacement only concerns publishing one prepared file. Suppose A and B both load version 1. A adds task X and replaces the file with its result. B adds task Y to its stale copy and replaces the file, erasing X. Unique staging filenames prevent staging collisions but do not resolve the stale-read conflict.

For the existing single-writer scope, document the limitation. If retaining files under concurrent writers, use a robust interprocess lock covering the full operation and define lock failure and crash behavior. For growing requirements, use a transactional database with generated unique IDs and explicit constraints. Optimistic version checks need an atomic compare-and-commit mechanism; comparing a version in user code before an unrelated write is still racy.

Crash durability is separate from lost-update prevention and atomic visibility. Define whether a successful response must survive process failure, host restart or power loss, then choose commit and flush behavior accordingly.

**Follow-up answered:** the current fixed staging path can also let writers delete or replace each other's staging. Strong answers separate these two races and identify which guarantee each proposed change actually adds.

## S08 · Add an optional due date without silently breaking old files.

**Answer:** first choose a schema policy. The current loader requires exactly three keys, so old and new records cannot be mixed casually. One approach is a versioned envelope with a records list and a migration from legacy lists to the new schema. Another is a carefully documented backward-compatible optional field rule. Choose deliberately rather than weakening all validation.

Represent a date-only deadline as an ISO date or null; reject impossible dates and wrong types. Parse into a domain value before use. Define whether saving old data upgrades the format and whether downgrade/rollback is supported. Preserve a recoverable original and make repeated migration idempotent.

Test a legacy file, a new file with null, a valid date, an invalid leap day, a malformed envelope and a future unsupported version. Keep migration separate from ordinary domain operations so callers can inspect what changed.

**Follow-up answered:** adding a dataclass default does not update the loader's exact-key check or the persisted schema. Strong answers trace every affected layer and define user-visible recovery if migration fails.

Repo: `storage.py`, `tests/test_task_tracker.py`. References: [[R17]], [[R18]], [[R20]], [[R33]].

<!-- page -->
# Senior · test strategy and compatibility
Section: Mock interview · senior

## S09 · How do you test a storage abstraction without overmocking?

**Answer:** write contract tests for the behavior all adapters must share: fresh storage, valid round-trip, stable identity, invalid input, no silent corruption and failure reporting. Run the same cases against JSON and any future database adapter. Use a real temporary filesystem or real disposable database for persistence semantics; mocks cannot prove those systems behave as assumed.

Keep fast pure model tests for business rules. Inject failures at meaningful boundaries such as commit or replacement, then assert preserved data and visible error outcomes. Add a small number of subprocess workflows for the installed/module command. Make concurrency tests coordinate a specific race with barriers rather than relying on arbitrary sleeps.

Property-oriented tests can check invariants such as `done + pending == total` across many valid task collections. Such tests supplement targeted examples; they do not replace explicit expectations about corruption or exit codes.

**Follow-up answered:** a perfectly mocked repository may pass while encoding, transaction or import behavior fails in reality. Strong answers keep test doubles narrow, independently manage fixtures and distinguish deterministic evidence from broad confidence claims.

## S10 · Support Python 3.10+ while using modern features responsibly.

**Answer:** define an explicit supported-version range and run tests on those interpreters in CI. Use syntax and standard-library APIs available at the minimum version or provide a justified compatibility path. A successful run on a newer interpreter does not prove the code parses or behaves the same on the minimum one.

The repo's `zip(strict=True)`, union annotations and dataclass slots fit the 3.10 baseline. `asyncio.TaskGroup`, newer type-parameter syntax and later annotation semantics require version-aware treatment if introduced. Check official version notes rather than assuming all documentation examples apply to the baseline.

Separate language behavior from CPython internals, especially memory management, bytecode and threading assumptions. Test quiet imports and module entry points. If distributing, validate installation in a clean environment as well as execution from the source checkout.

**Follow-up answered:** feature detection can help with optional runtime APIs, but cannot make unsupported syntax parse. Strong answers define deprecation and release policies and keep documentation honest about which matrix runs actually completed.

References: [[R25]], [[R26]], [[R28]], [[R45]].

<!-- page -->
# Senior · interfaces, retries and failure semantics
Section: Mock interview · senior

## S11 · When would you choose composition, a protocol or inheritance?

**Answer:** begin with the behavior the caller needs. Use composition when an object owns or delegates to a collaborator that can vary, such as storage or a clock. A structural protocol documents the required shape without forcing independently developed implementations into one hierarchy. Use inheritance when substitutability and shared behavior form a coherent, stable abstraction.

Avoid deep hierarchies created only to share a few lines. In multiple inheritance, `super()` follows the MRO; cooperative implementations need compatible signatures and consistent delegation. A subtype that rejects ordinary base inputs or violates promised outcomes is not behaviorally substitutable simply because `isinstance()` succeeds.

For the tracker, plain model functions remain sensible. A storage protocol earns its place once there are actual interchangeable adapters and common contract tests. Keep methods specific enough to express transactions; a generic “load everything, save everything” interface can make a database adapter preserve a weak concurrency model.

**Follow-up answered:** runtime protocol checks do not verify every method's semantic contract. Strong answers use types for communication and tests/design for behavior, rather than claiming either is a complete substitute for the other.

## S12 · Design a retry decorator for a state-changing operation.

**Answer:** first ask whether retry is safe. Classify transient failures, set a total deadline, bound attempts and use backoff with jitter where appropriate. Preserve arguments, result, metadata and the original failure information. Do not retry validation failures or all exceptions indiscriminately.

If the operation can commit before the caller sees an error, retries can duplicate it. Require an idempotency key or an operation-specific reconciliation strategy. Store the key and outcome atomically with the change; a process-local dictionary is insufficient across workers or restarts. Define what happens when the same key arrives with different inputs.

A synchronous decorator is not automatically correct for coroutines or generators. Cancellation should normally propagate; a retry policy should not silently restart work after the caller's deadline. Emit attempts and final outcomes without logging sensitive payloads.

**Follow-up answered:** completing a task is state-idempotent in the sample, but adding is not. Even repeated completion could produce duplicate notifications if notifications are added later. Strong answers define idempotency over the entire observable operation, not only one field assignment.

References: [[R15]], [[R10]], [[R11]], [[R37]].

<!-- page -->
# Architect · requirements and persistence
Section: Mock interview · architect

## A01 · Turn the local tracker into a team tool. Where do you start?

**Answer:** establish requirements before choosing a server or database. Ask how many users act concurrently, whether access is local or remote, whether edits must be immediately consistent, how tasks are owned and which failures must be recoverable. Define data sensitivity, latency, expected volume, offline needs and operational ownership.

Preserve the useful domain vocabulary but review the contract. Local integer IDs, one-writer files and unrestricted functions are not automatically suitable for a shared service. Introduce an application boundary that accepts a validated command plus caller context, authorizes it, performs a transactional change and returns a stable result. Keep presentation separate from these operations.

Choose the smallest persistence model that meets the requirements. A local multi-process tool may fit SQLite; a remotely accessed multi-user deployment may justify a database service and authentication boundary. Do not add distributed workers merely because the word “team” appears.

**Acceptance evidence:** contract tests, concurrent-update tests, restore drills, authorization checks and measured workload behavior. Roll out behind an adapter or limited migration with a recoverable source. A strong answer names assumptions, identifies changed guarantees and proposes a staged implementation rather than a technology shopping list.

## A02 · Replace JSON with SQLite while preserving meaningful behavior.

**Answer:** map task IDs to a primary key and express feasible invariants with constraints: non-null title, a nonblank-title rule and a constrained completion representation. Define transaction ownership at the application operation boundary. Insert and ID allocation must be coordinated by the database rather than `max(existing_ids) + 1` in separate reads.

Use parameterized SQL, explicit commit/rollback behavior and deterministic connection lifetime. Configure transaction semantics deliberately for the supported Python versions; newer `sqlite3` transaction APIs do not automatically exist at the 3.10 baseline. Understand SQLite's concurrent-writer limits before selecting it for the expected workload.

Expose operations such as add or complete through the adapter so transactions can span the necessary work. Retaining only a load-all/save-all interface can recreate lost updates on top of a better storage engine. Migrate with validation, backups and a clear cutover rule; compare record counts and identities before accepting success.

**Follow-up answered:** `with connection` manages transaction outcomes but should not be confused with a universal promise to close the connection. Strong answers verify exact API semantics and run the same behavioral contracts against old and new adapters.

References: [[R33]], [[R18]], [[R25]].

<!-- page -->
# Architect · concurrent edits and idempotency
Section: Mock interview · architect

## A03 · Two users edit one task. Prevent an unexplained lost update.

**Answer:** first define the conflict policy. For a task rename, optimistic concurrency can attach a version to the record. A command includes the version the user saw. An update checks ID and expected version atomically, increments the version on success and reports a conflict when no row matches. The caller can reload, present the competing edit or apply a domain-approved merge.

```sql
UPDATE tasks
SET title = ?, version = version + 1
WHERE id = ? AND version = ?;
```

This is an implementation sketch: validate and authorize before execution, and interpret the affected-row count inside the appropriate transaction. Distinguish a missing task from a stale version if the user contract needs that detail. Do not implement the check as a separate unprotected read followed by an unconditional update.

For highly contended multi-record invariants, evaluate transaction isolation and locking instead. Define bounded retries and avoid holding locks while waiting for a user's decision. Add tests that force two actors to use one starting version and verify exactly the chosen conflict behavior.

**Follow-up answered:** last-writer-wins can be a valid explicit policy for some data, but it should not be an accidental consequence of file replacement. Strong answers choose conflict semantics from the domain rather than defaulting to silent overwrite.

## A04 · A client times out after add. How can it retry safely?

**Answer:** use a client-supplied idempotency key with a defined scope, such as actor and operation. Persist the key, a fingerprint of validated input and the result in the same transaction as task creation. A repeated matching request returns the original outcome; reuse with a different input is rejected. A unique constraint coordinates concurrent submissions using the same key.

Define retention and behavior after expiry, treatment of in-progress operations and recovery from uncertain outcomes. Do not label the system exactly-once merely because a cache deduplicates requests. Network delivery and external side effects have separate failure modes.

**Follow-up answered:** a notification sent after commit can still duplicate or be lost around a crash. An outbox stored with the transaction plus an idempotent consumer can bridge that boundary with explicit delivery semantics. Strong answers trace “committed, response lost” and “committed, publisher crashed” separately and explain the evidence clients can query.

References: [[R33]], [[R37]].

<!-- page -->
# Architect · workload and streaming design
Section: Mock interview · architect

## A05 · Choose threads, processes or async for a new Python workload.

**Answer:** characterize the work: CPU versus I/O, existing library interfaces, expected concurrency, latency targets and state sharing. For blocking I/O with modest concurrency, bounded threads may be simplest. For many cooperative network operations, async can reduce the overhead of many waiting threads but demands compatible I/O and disciplined task ownership. For CPU-heavy Python work on a conventional GIL build, processes are a common starting point.

Account for process startup, serialization, memory duplication and import-safe workers. A free-threaded CPython build or native code that releases the GIL can change the choice, but requires verified compatibility and measurement. Do not infer runtime behavior from the language name alone.

Bound submitted work and define backpressure, timeouts, cancellation and shutdown. Choose where errors are observed and which work can safely retry. Measure realistic end-to-end latency and resource use, including queueing. A library API that blocks cannot be made cooperative just by calling it inside `async def`.

**Follow-up answered:** switching the tracker to async does not fix persistent concurrent updates. That guarantee belongs in the storage/application transaction design. Strong answers separate execution scheduling from consistency and keep the simplest mechanism that meets the measured requirement.

## A06 · Import a dataset much larger than memory, with malformed records.

**Answer:** define the input framing and error policy first. A line-delimited format can be parsed one record at a time more easily than one enormous JSON array with the standard decoder. Decide whether one invalid record aborts the whole import, rejects only that record or stops the current batch. Report locations and counts without exposing sensitive payloads.

Build a bounded read/parse/validate/transform/write pipeline. Bound queues and batch sizes; commit at a documented unit so partial progress is understandable. Use stable source identifiers or checkpoints for restart, and make resumed writes idempotent. Keep a recoverable input and record schema/version information with outcomes.

Sorting the whole dataset or collecting every rejected record in memory defeats streaming. Use external sorting, bounded diagnostics or durable reject output when required. `tee()` can silently buffer unbounded lag between consumers; prefer explicit fan-out with limits.

**Follow-up answered:** a successful checkpoint must correspond to committed output, not merely parsed input, or restart can skip unwritten work. Strong answers trace a failure between processing and commit and define what a restart repeats.

References: [[R30]], [[R31]], [[R32]], [[R12]], [[R18]].

<!-- page -->
# Architect · plugins and trust boundaries
Section: Mock interview · architect

## A07 · Design a Python plugin boundary for alternative storage/reporting.

**Answer:** define a small versioned contract around actual use cases. A storage plugin may need transactional operations and query interfaces; a reporting plugin may only need read-only records. Use protocols or an abstract base where they improve communication, with semantic documentation for ordering, ownership, failure types and resource lifetime.

Load plugins at an explicit application boundary rather than letting arbitrary imports launch work. Keep optional dependencies isolated and report compatibility errors clearly. Provide contract tests for each implementation. Decide lifecycle rules for initialization, cleanup and configuration, and an error policy when a plugin fails halfway through an operation.

Trusted in-process plugins execute with the host process's privileges and can mutate shared state. A protocol or a restricted-looking Python object is not a security sandbox. If plugins are untrusted, use an isolation boundary designed for that threat model, with a constrained communication schema and resource controls.

**Follow-up answered:** importing a plugin in a subprocess can isolate crashes and state, but is not automatically a complete permission sandbox. Strong answers distinguish extensibility, fault isolation and hostile-code containment and avoid unnecessary plugin machinery when only one implementation exists.

## A08 · Which checks protect a Python service at its input boundary?

**Answer:** parse a bounded format, validate shape and types, authorize the actor for the requested object/operation and enforce domain invariants transactionally. These are separate checks. Type hints do not validate JSON; valid JSON does not establish permission; permission does not make a state transition valid.

Use explicit schemas and limits for sizes, counts, nesting and expensive operations. Avoid `eval()` and untrusted pickle. Parameterize SQL and define a filesystem path policy when user input selects files. Use `secrets` for security-sensitive random tokens and keep secrets out of logs. A general regex validator should not introduce an unbounded computational path.

At the application boundary, turn expected failures into stable error categories without exposing internal paths or stack details unnecessarily. Preserve diagnostic causes in controlled logs. Use least capability in plugin and adapter interfaces where practical.

**Follow-up answered:** rejecting unknown fields can reveal typos and incompatible clients, but versioning may call for a documented tolerant policy. Strong answers choose the compatibility rule explicitly and test both malformed and well-formed-but-unauthorized cases.

References: [[R15]], [[R27]], [[R18]], [[R24]], [[R44]].

<!-- page -->
# Architect · recovery and evolution
Section: Mock interview · architect

## A09 · Define a migration and recovery plan before changing storage.

**Answer:** begin with recovery objectives: acceptable data loss, acceptable downtime and which failures must be recoverable. Inventory the old schema and invalid records. Design a deterministic migration with an explicit source/target version, validation report and recoverable original. A backup is useful only if a restore procedure works.

For a small local app, a maintenance-window conversion may be safer and simpler than dual writes. For a live service, choose staged schema changes compatible with old and new code, then a controlled cutover. Dual-write approaches create reconciliation problems unless atomicity and divergence recovery are designed.

Verify counts, IDs, required invariants and representative content. Rehearse on realistic data and inject interruption around checkpoints. Define whether rerunning resumes, safely repeats or refuses partial state. Keep rollback expectations honest: once new-format writes occur, restoring the old code alone may not restore compatibility.

**Follow-up answered:** atomic rename does not provide backup history or prove power-loss durability. Strong answers identify where source truth lives during migration, who can write at each stage and how recovery is tested rather than assumed.

## A10 · How would you govern Python versions and dependencies over time?

**Answer:** publish the supported interpreter range and implementation assumptions, test it in automation and make upgrades deliberate. Track syntax/API requirements separately from dependency compatibility. A Python 3.10 baseline cannot use later syntax behind an ordinary runtime `if`; the file must parse before the condition executes.

Build and test the installed artifact in clean environments, not only the source tree. Keep dependency declarations clear, use a repeatable resolution strategy appropriate to the deployment and test optional adapters independently. Evaluate new interpreter builds with representative workloads, native extensions and concurrency tests before switching production behavior.

Define deprecation windows, release notes and rollback criteria. Pinning every component forever trades update risk for accumulated maintenance risk; unbounded automatic upgrades trade predictability for freshness. Choose a managed cadence with evidence and ownership.

**Follow-up answered:** free-threaded CPython changes extension and thread-safety assumptions, so it is a deployment choice requiring verification rather than merely changing a version string. Strong answers describe a compatibility matrix, real completed results and a staged rollout with observable success criteria.

References: [[R18]], [[R33]], [[R28]], [[R39]], [[R45]].

<!-- page -->
# Architect · operations and design synthesis
Section: Mock interview · architect

## A11 · Design observability that helps diagnose Python failures.

**Answer:** start from questions operators must answer: which operation failed, for whom or which object, before or after commit, and whether a retry is safe. Emit structured events with correlation IDs, operation IDs, outcome categories and durations. Configure logs at the application boundary and avoid secret or excessive payload logging.

Measure latency distributions, throughput, failure rates, queue depth, retry counts and resource consumption. Add storage-specific indicators such as conflict rate, commit failures and recovery attempts. Correlate symptoms with deployed version and configuration. An average can hide severe tail latency, while a count without a denominator can mislead.

Define actionable alerts around user impact and saturation rather than every exception. Include a runbook for corruption, failed migration and uncertain operation outcomes. Use sampling or bounded diagnostics to avoid turning an incident into a logging outage. Test that error paths emit useful context without accidentally reporting success.

**Follow-up answered:** profiling is usually a diagnostic tool, not a replacement for production metrics. Strong answers connect each signal to an operational decision and state retention/privacy rules for diagnostic data.

## A12 · Propose an incremental architecture for the evolved tracker.

**Answer:** keep domain rules small and independent of the interface. Add an application layer with explicit commands and transaction boundaries. Put validation and authorization at the appropriate ingress, use typed domain values where they clarify invariants and place persistence behind operations that can preserve those invariants atomically.

Start with one deployable application and a transactional store if that meets the requirements. Add optimistic versions for competing edits and idempotency records for retryable creates. Use an outbox only if reliable external side effects are required. Introduce queues or separate services when workload or ownership evidence justifies their operational cost.

Preserve fast model tests, add shared adapter contracts and test actual concurrent/failed workflows. Migrate in reversible stages with a known source of truth, measurable acceptance criteria and a restore plan. Document what remains outside the guarantee, such as offline conflict merging or multi-region failover, until it is explicitly designed.

**Follow-up answered:** a successful architecture review ends with a concrete next change and verification plan. For this repo, a sensible first step may simply be a complete rename feature; for confirmed concurrent writers, it may be a transactional SQLite adapter. Strong judgment matches complexity to a stated requirement and revisits the decision as evidence changes.

References: [[R37]], [[R33]], [[R15]], [[R25]].
