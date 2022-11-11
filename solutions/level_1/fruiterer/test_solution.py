from typing import TypedDict

from . import solution


class InputDict(TypedDict):
    k: int
    m: int
    score: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'k': 3,
            'm': 4,
            'score': [1, 2, 3, 1, 2, 3, 1],
        },
        'expected': 8,
    },
    {
        'input': {
            'k': 4,
            'm': 3,
            'score': [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2],
        },
        'expected': 33,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
