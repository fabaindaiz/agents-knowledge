---
slug: "a-decoder-that-degrades-to-plausible-output-needs-an-out-of-band-check"
topic: "verification"
claim: "A component whose wrong answer is well formed — a decoder given the wrong side parameter, an estimator with a systematic error — passes every check of its own consistency; verify it against something it did not produce: a fingerprint of the parameter checked before use, a known truth, or agreement between independent measurements."
confidence: "measured"
phases: ["verify"]
check: "a planted wrong parameter, or an input whose answer is known, is caught by the out-of-band check, not by the component's own success, stability or reliability flag"
about:
  - {do: "Decode with a side parameter, or trust an estimator's own quality report", wrong_when: "a wrong parameter gives well-formed wrong output that every self-check passes"}
rests_on: "end-to-end argument, Saltzer, Reed & Clark 1984; trueness versus precision, JCGM 200"
strength: "established"
our_evidence: "measured in two repositories, two domains"
---

# A decoder that degrades to plausible output needs an out-of-band check

## Why it works

Most components announce a wrong input: a parse error, an exception, an empty result. Some do not. A decompressor given the wrong dictionary, a cipher without authentication given the wrong key, a binary record read with the wrong schema, an estimator searching the wrong range: each returns output of the right shape, and nothing downstream can tell it from a right answer, because the right answer was never available to compare with.

Checks the component runs on itself do not help, because they share its error. A decoder that does not fail is not evidence that it decoded. An estimator that gives the same value across its analysis parameters, the same value with a fixed seed and a sharp peak is **precise**; none of that says it is **true**. Stability and repeatability measure the spread of answers around their own mean, and a systematic error moves the mean, which leaves the spread unchanged. A self-assessed "reliable" flag is computed from the same correlated evidence and passes with it.

The check therefore sits outside the component, on something it did not produce. For a decoder, a fingerprint of the side parameter (the dictionary's hash, the writer schema's fingerprint) stored with the data and compared before decoding. For an estimator, a known truth (a simulation in which the answer is set) or agreement between measurements that do not share the error (a true offset is seen again by an independent measurement; an artefact of one method is not).

Siblings in this base: `refusal-must-not-read-like-an-answer` is the case where the component knows it cannot answer and must say so; here it does not know. `close-the-loop-in-the-actuators-frame` names one cause of a systematic error, a residual measured in the wrong frame.

## When it does NOT apply

- **The format already carries the check, and it is switched on**: an authenticated cipher returns a failure instead of plaintext under the wrong key, and a compressed frame that records its dictionary identifier and a content checksum is refused on a mismatch. The claim is about formats and estimators where that check is optional or absent.
- **The output is checked against an independent truth downstream anyway**: then that check is the out-of-band one, and a second one buys nothing.

## What it costs

A fingerprint stored beside the data and verified on every open, which looks redundant to anyone who assumes the decoder would fail by itself, and so is the first guard deleted in a clean-up. For an estimator, a simulation harness with known answers and independent repeat measurements, which cost more than the measurement they validate. And quality criteria that read well (stability, sharpness, a confidence score) are discarded when they turn out to measure precision only.

## Where it came from

A repository with rebuilt data artefacts, measured: records are compressed against a dictionary shared by the whole artefact, and given the **wrong** dictionary the decompressor **did not error**; it returned corrupt text. The dictionary's hash is stored and verified on open. The repository lists this among guardrails that look redundant and are not.

A repository with a real-time signal-processing service and a measurement loop met it three times in two weeks, each time measured. A delay estimator searched only non-negative lags, while against a reference shifted to the median of the channels the earliest channel's lag is negative by construction: errors of milliseconds with reverberation and tens of milliseconds without, while the estimator reported a stability about three orders of magnitude finer and flagged itself reliable. A simulation with known delays caught it; no measurement on real hardware could. A level estimator was off by up to about ten decibels depending on the noise realisation, and its earlier validation had been repeatability with the same seed. A confidence threshold rated a measurement reliable at an error of a quarter of a second under heavy noise. Three quality criteria were discarded in turn for reporting all fine while the measurement was wrong; what survived is stability plus repetition across independent measurements.

## Literature

- **Saltzer, Reed & Clark, 1984, "End-to-End Arguments in System Design"** (ACM Transactions on Computer Systems 2(4)). *Checked 2026-10-05 against the authors' copy.* In the careful file transfer example, whatever reliability the lower layers add, correctness is established only by a checksum stored with the file and compared at the far end, because faults enter where the lower checks cannot see. **What we take:** the check sits outside the component that can fail silently. **Where we go further:** the component here fails without any fault in transit, only from a wrong side parameter, and the same argument applies to an estimator's quality report.
- **JCGM 200:2012, *International Vocabulary of Metrology* (VIM, 3rd edition), entries 2.14 "measurement trueness" and 2.15 "measurement precision"** (BIPM online edition). *Checked 2026-10-05.* Trueness is the closeness of the mean of replicates to a reference value and relates to systematic error, not random error; precision is the closeness among replicates under stated conditions. ISO 5725-1 is cited only through the VIM's own reference, not opened. **What we take:** stability and repeatability are precision, and say nothing of the systematic error.
- **Morris, White & Crowther, 2019, "Using simulation studies to evaluate statistical methods"** (Statistics in Medicine 38(11)). *Checked 2026-10-05 against the open-access copy.* Simulation's strength is that the truth is known from the data-generating process, which is what makes bias measurable; bias and empirical standard error are separate measures. **What we take:** the known-truth remedy.
- **RFC 1950, ZLIB compressed data format** (Deutsch & Gailly, 1996), §2.2–2.3. *Checked 2026-10-05.* The wrapper records the preset dictionary's checksum, and a decoder must fail on a dictionary it does not recognise; the raw stream inside it (RFC 1951) carries no such field. **What we take:** the first occurrence used the raw stream, so the check its format family offers was left out by the framing, not missing from the algorithm. A synthetic probe in the home (2026-10-05, `meta/tracking/experiments.md` *Run*) showed the same compressor never failing silently inside its wrapper and never failing at all without it.
- **RFC 8878, Zstandard compression** (Collet & Kucherawy, 2021), §3.1.1. *Checked 2026-10-05.* A second format family where the dictionary identifier and the content checksum are both optional; without the identifier the decoder has to know which dictionary to use. **What we take:** the same choice, offered and omissible, in another format.
- **RFC 5116, authenticated encryption** (McGrew, 2008), §2.2. *Checked 2026-10-05.* Authenticated decryption returns either the plaintext or a distinct failure. **What we take:** the boundary; a key is a side parameter only where the cipher is unauthenticated.
- **Apache Avro specification, "Data Serialization" and "Single-object encoding"**. *Checked 2026-10-05.* Binary data carries no type information, so reading it with another schema is possible though not advisable; the single-object encoding prefixes each record with a fingerprint of the writer's schema. **What we take:** a third instance of the same design, where the remedy is a parameter fingerprint verified before decoding.

## Evidence

**Measured in two repositories, in two domains:** a decompressor that returned corrupt text under the wrong dictionary instead of failing; and three estimators whose self-consistency passed while their error, set by simulation, was orders of magnitude larger than their reported stability. Not measured: how many decoders with a side parameter in a repository fail loudly on a wrong one. The experiment: for each such decoder, decode a sample with a wrong parameter and record whether it errors or returns well-formed output; for each estimator, record whether its validation includes a known truth.
