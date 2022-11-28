from typing import TypedDict

from . import solution


class Input(TypedDict):
    numbers: list[int]
    hand: str


class CaseDict(TypedDict):
    input: Input
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': {
            'numbers': [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
            'hand': "right",
        },
        'expected': "LRLLLRLLRRL",
    },
    {
        'input': {
            'numbers': [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
            'hand': "left",
        },
        'expected': "LRLLRRLLLRR",
    },
    {
        'input': {
            'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            'hand': "right",
        },
        'expected': "LLRLLRLLRL",
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
