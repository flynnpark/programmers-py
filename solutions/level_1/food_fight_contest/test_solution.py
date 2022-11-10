from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[int]
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': [1, 3, 4, 6],
        'expected': "1223330333221",
    },
    {
        'input': [1, 7, 1, 2],
        'expected': "111303111",
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
