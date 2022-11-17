from typing import TypedDict

from . import solution


class Input(TypedDict):
    number: int
    limit: int
    power: int


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'number': 5,
            'limit': 3,
            'power': 2,
        },
        'expected': 10,
    },
    {
        'input': {
            'number': 10,
            'limit': 3,
            'power': 2,
        },
        'expected': 21,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
