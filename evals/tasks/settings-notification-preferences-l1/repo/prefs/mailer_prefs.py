CADENCES = ("daily", "weekly", "never")


def set_digest(store, user_id, cadence):
    if cadence not in CADENCES:
        raise ValueError(f"cadence must be one of {CADENCES}")
    store.update(user_id, {"notifications.digest": cadence})
