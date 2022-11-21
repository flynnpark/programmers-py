def solution(left: int, right: int) -> int:
    result = 0
    for number in range(left, right + 1):
        if int(number**0.5) == number**0.5:
            result -= number
        else:
            result += number
    return result
