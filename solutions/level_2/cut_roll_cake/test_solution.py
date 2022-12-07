from typing import TypedDict

from . import solution


class Input(TypedDict):
    topping: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'topping': [1, 2, 1, 3, 1, 4, 1, 2],
        },
        'expected': 2,
    },
    {
        'input': {
            'topping': [1, 2, 3, 1, 4],
        },
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
