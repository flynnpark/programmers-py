from typing import TypedDict

from . import solution


class Input(TypedDict):
    genres: list[str]
    plays: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'genres': ["classic", "pop", "classic", "classic", "pop"],
            'plays': [500, 600, 150, 800, 2500],
        },
        'expected': [4, 1, 3, 0],
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
