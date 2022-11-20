from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[list[int]]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [[60, 50], [30, 70], [60, 30], [80, 40]],
        'expected': 4000,
    },
    {
        'input': [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
        'expected': 120,
    },
    {
        'input': [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]],
        'expected': 133,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
