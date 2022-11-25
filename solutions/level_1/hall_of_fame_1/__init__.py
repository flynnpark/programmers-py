def solution(k: int, score: list[int]) -> list[int]:
    result = []
    temp = []

    for item in score:
        temp.append(item)

        if len(temp) > k:
            temp.remove(min(temp))

        result.append(min(temp))

    return result
