class Recommender:
    def __init__(self):
        self.calls = 0

    def for_user(self, user_id):
        self.calls += 1
        return [f"item-{user_id}-{i}" for i in range(3)]

    def batch(self, user_ids):
        self.calls += 1
        return {u: [f"item-{u}-{i}" for i in range(3)] for u in user_ids}
