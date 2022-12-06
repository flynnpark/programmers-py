from typing import TypedDict

from . import solution


class Input(TypedDict):
    array: list[int]
    commands: list[list[int]]


class CaseDict(TypedDict):
    input: Input
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'array': [1, 5, 2, 6, 3, 7, 4],
            'commands': [[2, 5, 3], [4, 4, 1], [1, 7, 3]],
        },
        'expected': [5, 6, 3],
    }
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
