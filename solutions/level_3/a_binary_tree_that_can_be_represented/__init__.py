import math


def check_parent(number, parent):
    if number == '':
        return True

    mid = len(number) // 2
    current = number[mid]

    if current == '1' and parent == '0':
        return False
    return check_parent(number[:mid], current) and check_parent(number[mid + 1 :], current)


def check_number(number):
    if number == 1:
        return 1

    binary_number = bin(number)[2:]
    digit = 2 ** (int(math.log(len(binary_number), 2)) + 1) - 1
    binary_number = '0' * (digit - len(binary_number)) + binary_number

    if binary_number[len(binary_number) // 2] == '1' and check_parent(binary_number, True):
        return 1
    return 0


def solution(numbers):
    result = []
    for number in numbers:
        result.append(check_number(number))
    return result
