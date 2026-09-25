# Carriers — every repository known to hold this bundle

**One row per carrier, by its id**, and the version it was last aligned to. `release.py register`
writes the rows and `release.py align` refuses to close a meta-session while a reached carrier is
missing here or registered at another version. The id is random, minted once by `bundle.py carrier-id
--mint` and stored in the carrier's own `.agents/carrier.toml`; it is not derived from anything about
the repository, so it cannot be reversed. Nothing describing a carrier
is ever written next to its id, here or anywhere in the bundle. **Paths are never written here**: they are per machine, in the local manifest.

| Carrier | Version | Aligned on |
|---|---|---|
| r-a2f271 | 0.0.20 | 2026-09-24 |
| r-5ed7e8 | 0.0.21 | 2026-09-24 |
| r-882427 | 0.0.21 | 2026-09-24 |
| r-4ca43d | 0.0.21 | 2026-09-24 |
| r-0fc418 | 0.0.21 | 2026-09-24 |
| r-1a1516 | 0.0.21 | 2026-09-24 |

**Every row is written by `release.py register`**, never by hand; a carrier that cannot run the
tool reports that as a defect in `candidates.md`.

## Not reached

Carriers known to exist and not aligned by the last meta-session. They are described here without
ids: the ids they were registered under were derived from their remotes and could be reversed by
guessing, so they were withdrawn on 2026-09-24. Each mints a random id with
`bundle.py carrier-id --mint` when a meta-session next reaches it, and receives the current release
then, keeping its own repository fields.

- **Several carriers aligned at an older release of this line.**
- **Any other carrier of the `g-c7344c` line.** Four were reached by the meta-session of
  2026-09-24 and are registered above; none other is known on the machine that ran it.
