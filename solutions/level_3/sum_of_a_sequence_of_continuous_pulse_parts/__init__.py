def solution(sequence: list[int]):
    prefix_sum = [0]

    for index in range(len(sequence)):
        pulse = -1 if index % 2 else 1
        prefix_sum.append(prefix_sum[-1] + pulse * sequence[index])

    return abs(max(prefix_sum) - min(prefix_sum))
