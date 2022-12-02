def solution(s: str) -> int:
    result = 0
    x = None
    x_count = 0
    y_count = 0

    for char in s:
        if x is None:
            x = char

        if char == x:
            x_count += 1
        else:
            y_count += 1

        if x_count == y_count:
            x = None
            x_count = 0
            y_count = 0
            result += 1

    if x:
        result += 1

    return result
