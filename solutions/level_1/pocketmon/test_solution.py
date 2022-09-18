from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [3, 1, 2, 3],
        'expected': 2,
    },
    {
        'input': [3, 3, 3, 2, 2, 4],
        'expected': 3,
    },
    {
        'input': [3, 3, 3, 2, 2, 2],
        'expected': 2,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
