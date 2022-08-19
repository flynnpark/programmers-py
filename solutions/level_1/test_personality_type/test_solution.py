from typing import TypedDict

from . import solution


class Input(TypedDict):
    survey: list[str]
    choices: list[int]


class CaseDict(TypedDict):
    input: Input
    expected: str


test_cases: list[CaseDict] = [
    {
        "input": {
            "survey": ["AN", "CF", "MJ", "RT", "NA"],
            "choices": [5, 3, 2, 7, 5],
        },
        "expected": "TCMA",
    },
    {
        "input": {
            "survey": ["TR", "RT", "TR"],
            "choices": [7, 1, 3],
        },
        "expected": "RCJA",
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
