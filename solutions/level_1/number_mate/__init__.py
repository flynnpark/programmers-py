import collections


def solution(X: str, Y: str) -> str:
    answer = ''
    counter_x = collections.Counter(X)
    counter_y = collections.Counter(Y)

    for i in range(9, -1, -1):
        answer += (str_i := str(i)) * min(counter_x.get(str_i, 0), counter_y.get(str_i, 0))

    if answer == '':
        return '-1'

    if len(answer) == answer.count('0'):
        return '0'

    return answer
