from typing import TypedDict

import pytest

from . import solution


class InputDict(TypedDict):
    sequence: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'sequence': [2, 3, -6, 1, 3, -1, 2, 4],
        },
        'expected': 10,
    }
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    input = test_case['input']
    result = solution(**input)
    assert result == test_case['expected']
