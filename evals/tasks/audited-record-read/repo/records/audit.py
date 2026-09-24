class AuditUnavailable(Exception):
    pass


class AuditLog:
    """The regulator-mandated access log. Every read of patient data must be recorded here."""

    def __init__(self, down=False):
        self.down = down
        self.records = []

    def record(self, actor, action, subject):
        if self.down:
            raise AuditUnavailable("audit log unavailable")
        self.records.append((actor, action, subject))
