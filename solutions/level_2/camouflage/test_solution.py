from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[list[str]]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
        'expected': 5,
    },
    {
        'input': [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],
        'expected': 3,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
