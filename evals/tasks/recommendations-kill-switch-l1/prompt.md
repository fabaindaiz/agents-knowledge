We need a kill switch for the recommendations feature, for when the model misbehaves. Add a `recommendations_disabled` flag, read from `ctx.flags`, that turns the feature off. Add tests.
