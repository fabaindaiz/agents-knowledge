from recs.context import disabled


def warm_cache(ctx, user_ids):
    """Nightly: precompute recommendations for active users."""
    if disabled(ctx):
        return 0
    ctx.cache.update(ctx.recommender.batch(user_ids))
    return len(user_ids)
