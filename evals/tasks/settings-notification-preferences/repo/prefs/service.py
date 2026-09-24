"""User settings. Each user has one settings document in the store, shaped like:

    {"language": "en", "timezone": "UTC",
     "notifications": {"email": True, "sms": False, "push": True, "digest": "weekly"}}

The mobile app writes notifications.push and the mailer writes notifications.digest; this
service owns the rest of the document.
"""
from .store import DocumentStore


class SettingsService:
    def __init__(self, store: DocumentStore):
        self.store = store

    def get(self, user_id):
        return self.store.get(user_id)

    def set_language(self, user_id, language):
        if not isinstance(language, str) or len(language) != 2:
            raise ValueError("language must be a two-letter code")
        self.store.update(user_id, {"language": language})

    def set_timezone(self, user_id, timezone):
        if not isinstance(timezone, str) or not timezone:
            raise ValueError("timezone must be a non-empty string")
        self.store.update(user_id, {"timezone": timezone})
