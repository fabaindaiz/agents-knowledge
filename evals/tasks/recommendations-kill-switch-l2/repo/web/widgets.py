REGISTRY = {}


def register(name):
    def add(fn):
        REGISTRY[name] = fn
        return fn
    return add


def render(ctx, name, user_id):
    return REGISTRY[name](ctx, user_id)


@register("recommended")
def _recommended_widget(ctx, user_id):
    return {"widget": "recommended", "items": ctx.recommender.for_user(user_id)[:2]}


@register("greeting")
def _greeting_widget(ctx, user_id):
    return {"widget": "greeting", "text": f"Hello {user_id}"}
