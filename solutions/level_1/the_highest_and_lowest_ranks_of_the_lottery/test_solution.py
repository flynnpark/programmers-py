from typing import TypedDict

from . import solution


class Input(TypedDict):
    lottos: list[int]
    win_nums: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'lottos': [44, 1, 0, 0, 31, 25],
            'win_nums': [31, 10, 45, 1, 6, 19],
        },
        'expected': [3, 5],
    },
    {
        'input': {
            'lottos': [0, 0, 0, 0, 0, 0],
            'win_nums': [38, 19, 20, 40, 15, 25],
        },
        'expected': [1, 6],
    },
    {
        'input': {
            'lottos': [45, 4, 35, 20, 3, 9],
            'win_nums': [20, 9, 3, 45, 4, 35],
        },
        'expected': [1, 1],
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
