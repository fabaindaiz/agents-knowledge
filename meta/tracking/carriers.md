# Carriers — every repository known to hold this bundle

**One row per carrier, by its id**, and the version it was last aligned to. `release.py register`
writes the rows and `release.py align` refuses to close a meta-session while a reached carrier is
missing here or registered at another version. The id is random, minted once by `bundle.py carrier-id
--mint` and stored in the carrier's own `.agents/carrier.toml`; it is not derived from anything about
the repository, so it cannot be reversed. Nothing describing a carrier
is ever written next to its id, here or anywhere in the bundle. **Paths and names are never written here**: they are per machine, in the local manifest, where
`release.py carriers` shows which repository each id is.

| Carrier | Version | Aligned on |
|---|---|---|
| r-9b5625 | 0.0.29 | 2026-10-05 |
| r-d8288b | 0.0.29 | 2026-10-05 |
| r-7d2612 | 0.0.28 | 2026-10-05 |
| r-3d2584 | 0.0.28 | 2026-10-05 |
| r-498de0 | 0.0.28 | 2026-10-05 |
| r-7985ee | 0.0.28 | 2026-10-05 |
| r-81be2b | 0.0.25 | 2026-09-29 |
| r-1190d3 | 0.0.25 | 2026-09-29 |
| r-cef56f | 0.0.25 | 2026-09-29 |
| r-7c8794 | 0.0.27 | 2026-10-05 |
| r-419136 | 0.0.28 | 2026-10-05 |
| r-098980 | 0.0.28 | 2026-10-05 |
| r-a2f271 | 0.0.28 | 2026-10-05 |
| r-5ed7e8 | 0.0.30 | 2026-10-08 |
| r-882427 | 0.0.29 | 2026-10-05 |
| r-4ca43d | 0.0.29 | 2026-10-05 |
| r-0fc418 | 0.0.29 | 2026-10-05 |
| r-1a1516 | 0.0.29 | 2026-10-05 |

**Every row is written by `release.py register`**, never by hand; a carrier that cannot run the
tool reports that as a defect, in a proposal.

## Not reached

Carriers known to exist and not aligned by the last meta-session. The meta-session of 2026-09-29
searched its machine for bundle folders and reached every carrier it found there, the two that had
no id included (each minted one on conversion). Those registered above at an older release were
not on that machine; each receives the current release from a meta-session where it is open, or
through its own `incoming/`.

- **Any other carrier of this bundle** not on a machine a meta-session has searched.
