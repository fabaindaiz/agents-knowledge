def warm_cache(ctx, user_ids):
    """Nightly: precompute recommendations for active users."""
    ctx.cache.update(ctx.recommender.batch(user_ids))
    return len(user_ids)
