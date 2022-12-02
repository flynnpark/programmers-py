from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: str
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': "banana",
        'expected': 3,
    },
    {
        'input': "abracadabra",
        'expected': 6,
    },
    {
        'input': "aaabbaccccabba",
        'expected': 3,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
