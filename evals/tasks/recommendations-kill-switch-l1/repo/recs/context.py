class AppContext:
    def __init__(self, recommender, flags=None):
        self.recommender = recommender
        self.flags = flags if flags is not None else {}
        self.cache = {}
