def solution(scores):
    result = 1
    target = scores[0]
    target_score = sum(target)

    scores.sort(key=lambda x: (-x[0], x[1]))

    prev_ref = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1

        if prev_ref <= score[1]:
            if target_score < sum(score):
                result += 1
            prev_ref = score[1]

    return result
