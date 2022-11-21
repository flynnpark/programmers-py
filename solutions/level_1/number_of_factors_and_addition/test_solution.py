from typing import TypedDict

from . import solution


class Input(TypedDict):
    left: int
    right: int


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'left': 13,
            'right': 17,
        },
        'expected': 43,
    },
    {
        'input': {
            'left': 24,
            'right': 27,
        },
        'expected': 52,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
