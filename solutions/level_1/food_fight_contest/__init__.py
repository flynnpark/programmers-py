def solution(food: list[int]) -> str:
    result = ''
    for i, f in enumerate(food[1:]):
        f_count = f // 2
        result += str(i + 1) * f_count
    return f'{result}0{"".join(reversed(result))}'
