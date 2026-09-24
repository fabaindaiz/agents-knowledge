import sys


class WebhookSink:
    def __init__(self, url, post):
        self.url = url
        self.post = post

    def send(self, message):
        self.post(self.url, {"text": message})


class StderrSink:
    def __init__(self, stream=None):
        self.stream = stream or sys.stderr

    def send(self, message):
        print(f"ALERT {message}", file=self.stream)
