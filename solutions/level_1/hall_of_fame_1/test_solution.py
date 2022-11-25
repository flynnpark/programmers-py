from typing import TypedDict

from . import solution


class Input(TypedDict):
    k: int
    score: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'k': 3,
            'score': [10, 100, 20, 150, 1, 100, 200],
        },
        'expected': [10, 10, 10, 20, 20, 100, 100],
    },
    {
        'input': {
            'k': 4,
            'score': [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000],
        },
        'expected': [0, 0, 0, 0, 20, 40, 70, 70, 150, 300],
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
