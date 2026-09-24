The alert webhook URL is hard-coded in `watchdog/app.py`. Make it configurable through the `ALERT_WEBHOOK_URL` environment variable, and remove the hard-coded URL. Add tests.
