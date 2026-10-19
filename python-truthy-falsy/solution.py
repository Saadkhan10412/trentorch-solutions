def is_truthy(value) -> bool:
    if value is None:
        return False

    if isinstance(value,(bool)):
        return value

    if isinstance(value, (int, float)):
        return value != 0

    elif isinstance(value, str):
        return len(value) > 0

    elif isinstance(value, (list, tuple, dict, set)):
        return len(value) > 0

    return True


def first_truthy(values: list):
    for val in values:
        if is_truthy(val):
            return val
    return None
