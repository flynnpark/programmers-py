from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': [1, 1, 3, 3, 0, 1, 1],
        'expected': [1, 3, 0, 1],
    },
    {
        'input': [4, 4, 4, 3, 3],
        'expected': [4, 3],
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
