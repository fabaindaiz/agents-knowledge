# Operations

- Logs are kept for 14 days; anything older is in the archive bucket.
- Deploys happen on weekdays before 16:00; a deploy after that needs a second reviewer.
- Every service exposes `/healthz`; the load balancer drains an instance after three failures.
- Email delivery is best-effort: no order flow may fail because the email provider is down.
- Feature flags are cached for 60 seconds per process.
- Database backups run nightly and are restored to staging every Monday.
- Timestamps are stored in UTC and rendered in the user's time zone at the edge.
- API keys are rate-limited to 100 requests per minute; internal callers are exempt.
- On-call rotates weekly; incidents are written up within five working days.
- Metrics are namespaced by service; dashboards live with the service that emits them.


