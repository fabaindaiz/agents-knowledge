def require_positive(name, value):
    if value is None or value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def require_text(name, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()
