Every read of a patient record must now be written to the `AuditLog`. Change `Records.read` in `records/service.py` to record the access (actor, "read", patient id). Add tests.
