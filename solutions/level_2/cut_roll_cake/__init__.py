import collections


def solution(topping: list[int]) -> int:
    result = 0
    topping_count = collections.Counter(topping)

    way = set()
    while len(topping):
        current = topping.pop()
        way.add(current)

        if topping_count[current] > 1:
            topping_count[current] -= 1
        else:
            del topping_count[current]

        if len(way) == len(topping_count):
            result += 1

    return result
