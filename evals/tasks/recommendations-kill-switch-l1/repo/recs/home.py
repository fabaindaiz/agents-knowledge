def recommended(ctx, user_id):
    if user_id not in ctx.cache:
        ctx.cache[user_id] = ctx.recommender.for_user(user_id)
    return ctx.cache[user_id]


def home_page(ctx, user_id):
    return {"greeting": f"Hello {user_id}", "recommended": recommended(ctx, user_id)}
