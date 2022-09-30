from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: str
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': "()()",
        'expected': True,
    },
    {
        'input': "(())()",
        'expected': True,
    },
    {
        'input': ")()(",
        'expected': False,
    },
    {
        'input': "(()(",
        'expected': False,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
