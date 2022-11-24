def solution(n: int, lost: list[int], reserve: list[int]) -> int:
    result = n

    students = [1] * n

    for i in range(n):
        if i + 1 in lost:
            students[i] -= 1
        if i + 1 in reserve:
            students[i] += 1

    for i in range(n):
        if students[i] == 0:
            if i > 0 and students[i - 1] == 2:
                students[i - 1] -= 1
            elif i < n - 1 and students[i + 1] == 2:
                students[i + 1] -= 1
            else:
                result -= 1

    return result
