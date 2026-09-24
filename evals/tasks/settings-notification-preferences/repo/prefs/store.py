"""An in-memory stand-in for the document store the service writes to.

`update(doc_id, changes)` follows the store's partial-update semantics: each top-level key in
`changes` replaces that field's stored value, and a dotted key such as "profile.name" sets one
nested field and leaves its siblings alone.
"""
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
            parts = key.split(".")
            target = doc
            for part in parts[:-1]:
                target = target.setdefault(part, {})
            target[parts[-1]] = copy.deepcopy(value)
