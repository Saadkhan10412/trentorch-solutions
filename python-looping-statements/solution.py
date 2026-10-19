def countdown_with_skip(start: int) -> list:
    lis = []
    while start > 0:
        if start == 3:
            start -= 1
            continue
        lis.append(start)
        start -= 1
    return lis


def find_first_negative(numbers: list) -> int | None:
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            result = numbers[i]
            break
        i += 1
    else:
        return None
    return result


def sum_with_index(numbers: list) -> dict:
    d = {}
    total = 0
    for i, val in enumerate(numbers):
        total += val
        d[i] = total
    return d


def manual_iteration_trace(items: list) -> list:
    result = []
    it = iter(items)
    while True:
        try:
            val = next(it)
            result.append(val)
        except StopIteration:
            break
    return result
