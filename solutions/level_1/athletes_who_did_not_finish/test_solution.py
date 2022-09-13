from typing import TypedDict

from . import solution


class Input(TypedDict):
    participant: list[str]
    completion: list[str]


class CaseDict(TypedDict):
    input: Input
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': {
            'participant': ["leo", "kiki", "eden"],
            'completion': ["eden", "kiki"],
        },
        'expected': "leo",
    },
    {
        'input': {
            'participant': ["marina", "josipa", "nikola", "vinko", "filipa"],
            'completion': ["josipa", "filipa", "marina", "nikola"],
        },
        'expected': "vinko",
    },
    {
        'input': {
            'participant': ["mislav", "stanko", "mislav", "ana"],
            'completion': ["stanko", "ana", "mislav"],
        },
        'expected': "mislav",
    },
]


def test_solution():
    for test_case in test_cases:
        assert solution(**test_case['input']) == test_case['expected']
