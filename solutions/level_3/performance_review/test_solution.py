from typing import TypedDict

import pytest

from . import solution


class InputDict(TypedDict):
    scores: list[list[int]]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'scores': [[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]],
        },
        'expected': 4,
    },
    {
        'input': {
            'scores': [[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]],
        },
        'expected': 3,
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
