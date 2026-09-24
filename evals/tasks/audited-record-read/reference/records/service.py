class Records:
    def __init__(self, store, audit):
        self.store = store      # patient_id -> record
        self.audit = audit

    def read(self, actor, patient_id):
        record = self.store[patient_id]
        self.audit.record(actor, "read", patient_id)
        return record
