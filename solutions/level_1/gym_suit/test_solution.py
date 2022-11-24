from typing import TypedDict

from . import solution


class Input(TypedDict):
    n: int
    lost: list[int]
    reserve: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'n': 5,
            'lost': [2, 4],
            'reserve': [1, 3, 5],
        },
        'expected': 5,
    },
    {
        'input': {
            'n': 5,
            'lost': [2, 4],
            'reserve': [3],
        },
        'expected': 4,
    },
    {
        'input': {
            'n': 3,
            'lost': [3],
            'reserve': [1],
        },
        'expected': 2,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
