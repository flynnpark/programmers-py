def solution(number: int, limit: int, power: int) -> int:
    result = 0

    for num in range(1, number + 1):
        num_of_divisors = 0

        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                num_of_divisors += 1
                if i**2 != num:
                    num_of_divisors += 1

        if num_of_divisors > limit:
            result += power
        else:
            result += num_of_divisors

    return result
