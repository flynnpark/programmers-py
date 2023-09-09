from typing import TypedDict

import pytest

from . import solution


class InputDict(TypedDict):
    numbers: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'numbers': [7, 42, 5],
        },
        'expected': [1, 1, 0],
    },
    {
        'input': {
            'numbers': [63, 111, 95],
        },
        'expected': [1, 1, 0],
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    input = test_case['input']
    result = solution(**input)
    assert result == test_case['expected']
