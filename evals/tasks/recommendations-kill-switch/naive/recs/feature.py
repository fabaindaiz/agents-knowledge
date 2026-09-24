from .model import Recommender


class Recommendations:
    def __init__(self, recommender=None, flags=None):
        self.recommender = recommender or Recommender()
        self.flags = flags if flags is not None else {}
        self.cache = {}

    def home_page(self, user_id):
        """The home page: a greeting, and the user's recommendations."""
        return {"greeting": f"Hello {user_id}", "recommended": self.recommended(user_id)}

    def recommended(self, user_id):
        if self.flags.get("recommendations_disabled"):
            return []
        if user_id not in self.cache:
            self.cache[user_id] = self.recommender.for_user(user_id)
        return self.cache[user_id]

    def warm_cache(self, user_ids):
        """Nightly job: precompute recommendations for active users."""
        self.cache.update(self.recommender.batch(user_ids))
        return len(user_ids)

    def email_digest(self, user_id):
        """The weekly email lists the user's recommendations."""
        return {"to": user_id, "items": self.recommender.for_user(user_id)}
