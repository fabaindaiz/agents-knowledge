# Datastore

- Documents are JSON objects keyed by user id.
- `update()` replaces each top-level key it is given; a dotted key such as `a.b` sets one nested field.
- Reads are strongly consistent within a region.
- Documents larger than 1 MB are rejected.


