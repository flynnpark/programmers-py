from collections import Counter
from functools import reduce


def solution(clothes: list[list[str]]):
    return reduce(lambda x, y: x * (y + 1), Counter([cloth[1] for cloth in clothes]).values(), 1) - 1
