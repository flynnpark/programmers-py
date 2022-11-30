import collections


def solution(k: int, tangerine: list[int]) -> int:
    result = 0
    stock = collections.Counter(tangerine)

    for size, count in stock.most_common():
        if k <= 0:
            break

        k -= count
        result += 1

    return result
