from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': [2, 1, 3, 4, 1],
        'expected': [2, 3, 4, 5, 6, 7],
    },
    {
        'input': [5, 0, 2, 7],
        'expected': [2, 5, 7, 9, 12],
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
