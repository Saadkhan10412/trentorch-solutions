def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.
    """
    if(n%2==0):
        return True
    else:
        return False
    pass


def greet_formal(name: str, title: str) -> str:
    """
    Return a greeting string in the exact form:
      "Good day, {title} {name}."
    Example: greet_formal("Smith", "Dr.") -> "Good day, Dr. Smith."
    """
    return f"Good day, {title} {name}."
    pass


def apply_twice(func, value):
    first = func(value)
    second = func(first)
    return second
