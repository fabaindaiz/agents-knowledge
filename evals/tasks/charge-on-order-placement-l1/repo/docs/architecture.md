# Architecture

- `billing/` holds the billing code; `infra/` holds shared plumbing (configuration, logging, metrics, clock).
- Modules do not import from `tests/`; fixtures live under `tests/fixtures` or `fixtures/`.
- Configuration is read once at start-up through `infra.config.load()`.
- Public functions validate their arguments and raise `ValueError` on bad input.
- Anything that crosses a process boundary is serialised as JSON.


