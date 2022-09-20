from collections import defaultdict


def solution(clothes: list[list[str]]):
    clothes_dict = defaultdict(list)
    result = 1

    for item, cloth_type in clothes:
        clothes_dict[cloth_type].append(item)

    for cloth_type in clothes_dict.keys():
        result *= len(clothes_dict[cloth_type]) + 1

    return result - 1
