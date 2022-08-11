def solution(lottos: list[int], win_nums: list[int]) -> list[int]:
    win_conditions = [6, 6, 5, 4, 3, 2, 1]  # index는 일치하는 번호의 갯수, 값은 등수

    num_of_zero = lottos.count(0)  # 알 수 없는 숫자 0의 갯수 카운트
    num_of_win = 0  # 구매한 번호 중 로또와 일치하는 번호의 갯수

    for num in lottos:
        if num in win_nums:
            num_of_win += 1  # 구매한 번호가 로또와 일치하면 갯수 증가

    return [win_conditions[num_of_win + num_of_zero], win_conditions[num_of_win]]  # 기대되는 최대 순위, 기대되는 최저 순위
