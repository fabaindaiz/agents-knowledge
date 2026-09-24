import copy


class DocumentStore:
    def __init__(self):
        self._docs = {}

    def put(self, doc_id, doc):
        self._docs[doc_id] = copy.deepcopy(doc)

    def get(self, doc_id):
        return copy.deepcopy(self._docs[doc_id])

    def update(self, doc_id, changes):
        if doc_id not in self._docs:
            raise KeyError(doc_id)
        doc = self._docs[doc_id]
        for key, value in changes.items():
            *parents, leaf = key.split(".")
            target = doc
            for part in parents:
                target = target.setdefault(part, {})
            target[leaf] = copy.deepcopy(value)
