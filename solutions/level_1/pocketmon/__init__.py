from collections import defaultdict


def solution(nums):
    hash_dict = defaultdict(int)

    for num in nums:
        hash_dict[num] += 1

    return min(len(nums) / 2, len(hash_dict.keys()))
