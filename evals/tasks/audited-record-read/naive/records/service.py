import logging
class Records:
    def __init__(self, store, audit):
        self.store = store      # patient_id -> record
        self.audit = audit

    def read(self, actor, patient_id):
        try:
            self.audit.record(actor, "read", patient_id)
        except Exception:
            logging.getLogger(__name__).warning("audit failed")
        return self.store[patient_id]
