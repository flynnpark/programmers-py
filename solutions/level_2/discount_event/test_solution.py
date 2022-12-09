from typing import TypedDict

from . import solution


class Input(TypedDict):
    want: list[str]
    number: list[int]
    discount: list[str]


class CaseDict(TypedDict):
    input: Input
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'want': ["banana", "apple", "rice", "pork", "pot"],
            'number': [3, 2, 2, 2, 1],
            'discount': [
                "chicken",
                "apple",
                "apple",
                "banana",
                "rice",
                "apple",
                "pork",
                "banana",
                "pork",
                "rice",
                "pot",
                "banana",
                "apple",
                "banana",
            ],
        },
        'expected': 3,
    },
    {
        'input': {
            'want': ["apple"],
            'number': [10],
            'discount': [
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
            ],
        },
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
