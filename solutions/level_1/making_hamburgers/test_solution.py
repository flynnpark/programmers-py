from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [2, 1, 1, 2, 3, 1, 2, 3, 1],
        'expected': 2,
    },
    {
        'input': [1, 3, 2, 1, 2, 1, 3, 1, 2],
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
