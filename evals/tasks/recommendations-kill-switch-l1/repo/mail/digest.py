def email_digest(ctx, user_id):
    return {"to": user_id, "items": ctx.recommender.for_user(user_id)}
