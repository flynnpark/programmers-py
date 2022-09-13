from collections import defaultdict


def solution(participant: list[str], completion: list[str]) -> str:
    participant_dict = defaultdict(int)
    for person in participant:
        participant_dict[person] += 1

    for person in completion:
        participant_dict[person] -= 1

    return next(key for key in participant_dict.keys() if participant_dict[key] == 1)
