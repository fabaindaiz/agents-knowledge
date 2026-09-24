def apply_device_state(store, user_id, push_enabled):
    store.update(user_id, {"notifications.push": bool(push_enabled)})
