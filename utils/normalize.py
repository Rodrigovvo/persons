def normalize_active(value):
    if isinstance(value, str):
        value = value.strip().lower()
        if value in ["true", "1", "yes", "y", "t"]:
            return True
        elif value in ["false", "0", "no", "n", "f"]:
            return False
    return bool(value)
