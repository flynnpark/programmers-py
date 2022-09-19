from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[str]
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': ["119", "97674223", "1195524421"],
        'expected': False,
    },
    {
        'input': ["123", "456", "789"],
        'expected': True,
    },
    {
        'input': ["12", "123", "1235", "567", "88"],
        'expected': False,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
