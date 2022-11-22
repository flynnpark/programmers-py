def solution(numbers: list[int]) -> list[int]:
    result = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])

    return sorted(list(set(result)))
