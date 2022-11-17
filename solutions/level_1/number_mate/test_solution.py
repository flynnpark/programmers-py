from typing import TypedDict

from . import solution


class Input(TypedDict):
    X: str
    Y: str


class CaseDict(TypedDict):
    input: Input
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': {
            'X': '100',
            'Y': '2345',
        },
        'expected': '-1',
    },
    {
        'input': {
            'X': '100',
            'Y': '203045',
        },
        'expected': '0',
    },
    {
        'input': {
            'X': '100',
            'Y': '123450',
        },
        'expected': '10',
    },
    {
        'input': {
            'X': '12321',
            'Y': '42531',
        },
        'expected': '321',
    },
    {
        'input': {
            'X': '5525',
            'Y': '1255',
        },
        'expected': '552',
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
