class SettingsService:
    def __init__(self, store):
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

    def set_notification_preferences(self, user_id, email=None, sms=None):
        changes = {}
        if email is not None:
            changes["notifications.email"] = bool(email)
        if sms is not None:
            changes["notifications.sms"] = bool(sms)
        if changes:
            self.store.update(user_id, changes)
