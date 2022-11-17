from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [-2, 3, 0, 2, -5],
        'expected': 2,
    },
    {
        'input': [-3, -2, -1, 0, 1, 2, 3],
        'expected': 5,
    },
    {
        'input': [-1, 1, -1, 1],
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
