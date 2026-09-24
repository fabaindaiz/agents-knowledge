from recs.context import disabled


def email_digest(ctx, user_id):
    if disabled(ctx):
        return {"to": user_id, "items": []}
    return {"to": user_id, "items": ctx.recommender.for_user(user_id)}
