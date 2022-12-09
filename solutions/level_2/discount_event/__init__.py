import collections


def solution(want: list[str], number: list[int], discount: list[str]) -> int:
    result = 0
    wanted = collections.Counter({})
    for product, count in zip(want, number):
        wanted[product] = count

    for i in range(len(discount)):
        temp = collections.Counter(discount[i : i + 10])

        if not (wanted - temp):
            result += 1

    return result
