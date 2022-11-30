from typing import TypedDict

from . import solution


class Input(TypedDict):
    k: int
    tangerine: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'k': 6,
            'tangerine': [1, 3, 2, 5, 4, 5, 2, 3],
        },
        'expected': 3,
    },
    {
        'input': {
            'k': 4,
            'tangerine': [1, 3, 2, 5, 4, 5, 2, 3],
        },
        'expected': 2,
    },
    {
        'input': {
            'k': 2,
            'tangerine': [1, 1, 1, 1, 2, 2, 2, 3],
        },
        'expected': 1,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
