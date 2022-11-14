from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: list[str]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': ["aya", "yee", "u", "maa"],
        'expected': 1,
    },
    {
        'input': ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"],
        'expected': 2,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
