from typing import TypedDict

from . import solution


class CaseDict(TypedDict):
    input: str
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': "one4seveneight",
        'expected': 1478,
    },
    {
        'input': "23four5six7",
        'expected': 234567,
    },
    {
        'input': "2three45sixseven",
        'expected': 234567,
    },
    {
        'input': "123",
        'expected': 123,
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(test_case['input']) == test_case['expected']
