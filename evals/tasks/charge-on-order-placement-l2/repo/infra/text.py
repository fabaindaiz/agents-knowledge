def slug(value):
    return "-".join("".join(c.lower() if c.isalnum() else " " for c in value).split())
