from typing import TypedDict

from . import solution


class Input(TypedDict):
    a: int
    b: int
    n: int


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'a': 2,
            'b': 1,
            'n': 20,
        },
        'expected': 19,
    },
    {
        'input': {
            'a': 3,
            'b': 1,
            'n': 20,
        },
        'expected': 9,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
