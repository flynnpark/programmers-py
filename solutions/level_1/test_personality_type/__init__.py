def solution(survey: list[str], choices: list[int]):
    answer = ''
    types = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}

    for s, c in zip(survey, choices):
        if s in types:
            if c - 4 < 0:
                types[s] -= abs(c - 4)
            else:
                types[s] += abs(c - 4)
        else:
            if c - 4 < 0:
                types[s[::-1]] += abs(c - 4)
            else:
                types[s[::-1]] -= abs(c - 4)

    for k, v in types.items():
        if v > 0:
            answer += k[1]
        else:
            answer += k[0]

    return answer
