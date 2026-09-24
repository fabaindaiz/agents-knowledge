# watchdog

Checks the services listed in its configuration every interval and raises an alert when one is down.

**The watchdog must always start**, even on a host whose configuration is broken: it is the process
that reports broken configuration. Alerts that cannot be delivered are written to stderr.
