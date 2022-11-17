import itertools


def solution(number: list[int]) -> int:
    candidates = list(itertools.combinations(number, 3))
    return sum(map(lambda items: 1 if sum(items) == 0 else 0, candidates))
