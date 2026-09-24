# Payment provider

- Webhooks are signed; the signature is checked at the edge before the handler runs.
- The provider delivers every event at least once and retries for up to three days until it receives a success response. Each event carries a unique `id`.
- Amounts are integers in the smallest currency unit.
- Sandbox and live events never share an endpoint.


