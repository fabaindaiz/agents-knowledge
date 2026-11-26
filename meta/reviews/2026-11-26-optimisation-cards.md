# Optimisation: candidate cards where the usual answer is wrong

2026-11-26, at the owner's request: research on optimisation across seven fronts (algorithms, data storage and
querying, continuous and pipeline processing, native platforms, design procedures, computational efficiency,
algorithms for common tasks), to suggest cards. Three read-only searches in parallel. **The filter is the
bundle's own** (`MANIFEST.md`): a card earns its place with a case where the usual answer is wrong and a check an
agent can run, not with textbook advice. **Strength:** each card says what was read; READ means a primary text was
read in whole or in its relevant part, SUMMARY means through a fetcher's summary or an abstract, ASSUMPTION means
from memory and still to verify. Engines and platforms are named by kind; sources keep their titles.

None of these is admitted by this document: each becomes a queued candidate lacking an occurrence in a carrier,
unless an existing note or candidate already holds it, in which case it is an extension.

## The candidates

| # | Slug | The usual answer, and where it is wrong | The check | Evidence | Strength |
|---|---|---|---|---|---|
| 1 | `hidden-quadratic-in-library-call` | "this loop is linear": a library call or a membership scan inside it is linear in the whole buffer, so the loop is quadratic | profile at n and 2n; time more than doubling names it | a public write-up of a game's loading time, cut by about two thirds by two such fixes (2021) | READ, one case |
| 2 | `single-thread-baseline-before-parallel` | "parallelise it": many systems scaled to many cores and still lost to one well-written thread | the single-thread time, and the cores needed to beat it | McSherry, Isard, Murray, *Scalability! But at what COST?*, HotOS 2015 | READ |
| 3 | `layout-and-algorithm-beat-core-count` | "more hardware": a cache-friendly order or another algorithm gave a larger gain, its preprocessing included | cache-miss counters before and after | the same paper | READ |
| 4 | `backtracking-regex-vs-automaton` | "a regex is cheap": a backtracking engine takes exponential time on some patterns an automaton runs in linear time; backreferences need backtracking | pathological input of growing length; time doubling per character | Cox, *Regular Expression Matching Can Be Simple And Fast*, 2007 | READ and SUMMARY |
| 5 | `small-n-sorted-array-vs-fancy-layout` | "use a tree or a hash": for a static lookup table a sorted array wins at small n, a heap-ordered layout at large n | lookups across sizes; the crossover where the working set leaves the cache | Khuong, Morin, *Array Layouts for Comparison-Based Searching*, arXiv 1509.05053 | abstract |
| 6 | `top-k-heap-vs-sort` | "a heap for top-k": a heap wins only when k is small against n; a full sort wins for larger k, min or max for one | time both at k/n of a thousandth, a hundredth, a tenth | a language's standard-library documentation of its heap module | SUMMARY |
| 7 | `float-summation-order` | "reordering a sum is free": it changes the result; naive error grows with n, pairwise with log n at the same speed | sum in the optimised order against an exact sum | Higham, *The Accuracy of Floating Point Summation*, 1993 (ASSUMPTION, not fetched) | SUMMARY |
| 8 | `pdqsort-patterns-and-stability` | "quicksort is quadratic on equal keys": current library sorts detect patterns and bound that case; they are not stable | benchmark the real input shape with the library's stable and unstable sorts | Peters, *Pattern-defeating Quicksort*, arXiv 2106.05123 | first pages |
| 9 | `index-write-cost` | "add an index": in a versioned-row store, an update touching no indexed column skips index upkeep; a new index on an updated column ends that | the engine's heap-only versus full-update counters, before and after | a relational engine's documentation on heap-only tuples | SUMMARY |
| 10 | `composite-index-order-is-version-dependent` | "equality columns first, range last": true, but engines with skip scan no longer rule an index out for a missing leading column | the plan's index condition versus filter, on the target version | the same engine's documentation on multicolumn indexes | READ (grepped) |
| 11 | `keyset-pagination` | "OFFSET pages": the engine reads and discards every skipped row, and inserts between pages duplicate or drop rows | the same query at offsets 0, ten thousand, a million | *No Offset*, an index-tuning site | SUMMARY |
| 12 | `small-connection-pool` | "a bigger pool": throughput falls and latency rises past a small pool; queue in the application instead | sweep the pool size under load; p99 and database active sessions | a connection-pool library's wiki, *About Pool Sizing* | READ, one demo |
| 13 | `retry-amplification` | "add retries": three retries at each of five layers multiply a failing dependency's load by about two hundred and forty; retry at one layer, with a budget and jitter | inject failures and watch load on the dependency | AWS Builders' Library, *Timeouts, retries, and backoff with jitter*, 2019; Google SRE book, *Addressing Cascading Failures* | READ |
| 14 | `exactly-once-needs-idempotent-sink` | "the engine is exactly-once": only for its own state; an external sink needs a transactional or idempotent write | kill a worker mid-checkpoint; compare sink and source counts | a stream engine's post on end-to-end exactly-once, 2018 | SUMMARY |
| 15 | `event-time-over-processing-time` | "window by arrival": late and out-of-order data give wrong results; window by event time, with a late-data policy | replay a shuffled copy and compare | Akidau et al., *The Dataflow Model*, VLDB 2015 | READ (opening) |
| 16 | `columnar-compression-defaults` | "always compress": for analytic columns, dictionary encoding by default and decode speed over ratio; block compression optional | scan with compression on and off, cold and warm | Zeng et al., *An Empirical Evaluation of Columnar Storage Formats*, arXiv 2304.05028 | abstract |
| 17 | `serializable-means-retry` | "raise the isolation level": the application must then retry whole transactions on serialization failures | a write-skew load test; the serialization-failure rate | the same engine's documentation on isolation | READ (grepped) |
| 18 | `cgroup-quota-throttles-at-low-utilisation` | "CPU is at a third, so it is not the CPU": a quota spread in per-CPU slices throttles many-threaded services well below it, on kernels before a fix | the cgroup's throttled-period counters against p99 | the kernel's CFS bandwidth documentation; a public engineering post on the regression, 2019 | READ |
| 19 | `fsync-failure-is-not-retryable` | "retry the fsync": the kernel may mark the failed pages clean, so a second call succeeds over lost data | fault injection under a write-then-fsync test | LWN, *PostgreSQL's fsync() surprise*, 2018 | snippets |
| 20 | `benchmark-the-release-config` | "it is faster on my run": a debuggable, unoptimised or emulated build measures something else | the benchmark in the shipped configuration, compilation modes compared | a mobile platform's benchmarking documentation | READ |
| 21 | `startup-profile-before-code` | "rewrite the slow startup": check first that the build ships its ahead-of-time profile | cold start with the profile on and off | the same platform's documentation (its own figures) | READ, vendor claim |
| 22 | `coordinated-omission` | "p99 from the load test": a closed-loop generator drops the slow samples; measure from the scheduled send at a fixed rate | a constant-rate run against an injected stall, corrected and not | Tene, *How NOT to Measure Latency*, talk, 2013 on | snippets |
| 23 | `huge-pages-and-overcommit-are-not-defaults-to-trust` | "enable huge pages", "overcommit is fine": the always-defrag setting stalls allocations; strict overcommit fails allocations instead of killing | the kernel's huge-page fault and compaction-stall counters | the kernel's memory-management documentation | SUMMARY |
| 24 | `a-blocked-main-thread-is-not-only-slow-code` | "move the computation off the UI thread": the cause is as often a synchronous call to a slow peer or a lock | the platform's traces of the main thread's blocked state | the mobile platform's documentation on unresponsive apps | READ |

Not verified, left as ideas: the cost of memoisation, string building in loops, amortised against worst-case
latency, cache stampede (Vattani et al., VLDB 2015, metadata only), hot keys in sharding, direct against buffered
I/O, background-work limits on mobile, the USE method, Amdahl's law beyond the COST paper, the roofline model,
regression gates in CI.

## Against what the bundle already holds

- **13** extends the candidate `a-retry-loop-needs-a-ceiling-and-a-dead-letter` and borders the note
  `retry-over-irreversible-effect`: an extension, not a new card.
- **14** borders the candidate `an-idempotence-key-coarser-than-the-write-unit-drops-data`.
- **20** and **22** border the method's own *measure before trusting* notes (`a-check-must-be-seen-to-fail`,
  `count-both-sides-and-use-a-control-window`): two measurement traps, likely one card with two boundaries.
- **2** and **3** are one source; one card with a second boundary.

## Recommended for the queue, ranked

By how often an agent gives the wrong answer, how cheap the check is, and how strong the evidence:
`retry-amplification` (as an extension), `hidden-quadratic-in-library-call`,
`single-thread-baseline-before-parallel` (with 3 as its boundary), `coordinated-omission` with
`benchmark-the-release-config` (one measurement card), `cgroup-quota-throttles-at-low-utilisation`,
`backtracking-regex-vs-automaton`, `index-write-cost`, `exactly-once-needs-idempotent-sink`,
`fsync-failure-is-not-retryable`, `keyset-pagination`. The rest stay here as ideas until a carrier meets one.
