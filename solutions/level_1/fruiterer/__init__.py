def solution(k: int, m: int, score: list[int]) -> int:
    return sum(map(lambda x: x * m, list(sorted(score, reverse=True))[m - 1 :: m]))
