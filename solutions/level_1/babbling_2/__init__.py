def solution(babbling: list[str]) -> int:
    can_speaks = ['aya', 'ye', 'woo', 'ma']

    answer: int = 0

    for item in babbling:
        for can_speak in can_speaks:
            if not can_speak * 2 in item:
                item = item.replace(can_speak, '1')

        if item.isdigit():
            answer += 1

    return answer
