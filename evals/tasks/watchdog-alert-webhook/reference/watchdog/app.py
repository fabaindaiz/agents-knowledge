import os

from .alerts import StderrSink, WebhookSink

def _default_post(url, payload):
    raise NotImplementedError("the HTTP client is wired in production")


class Watchdog:
    def __init__(self, services, interval_s, sink):
        self.services = services
        self.interval_s = interval_s
        self.sink = sink

    @classmethod
    def from_env(cls, environ=None, post=None, stream=None):
        environ = os.environ if environ is None else environ
        services = [s for s in environ.get("WATCHDOG_SERVICES", "").split(",") if s]
        interval_s = int(environ.get("WATCHDOG_INTERVAL_S", "30"))
        url = environ.get("ALERT_WEBHOOK_URL")
        sink = WebhookSink(url, post or _default_post) if url else StderrSink(stream)
        return cls(services, interval_s, sink)

    def alert(self, message):
        self.sink.send(message)

    def check(self, probe):
        for service in self.services:
            if not probe(service):
                self.alert(f"{service} is down")
