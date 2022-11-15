def solution(a: int, b: int, n: int) -> int:
    result = 0

    while n >= a:
        temp = (n // a) * b
        n = n % a + temp
        result += temp

    return result
