def solution(numbers: list[int], hand: str) -> str:

    coords = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }
    fixed_left = [1, 4, 7]
    fixed_right = [3, 6, 9]
    left = [3, 0]
    right = [3, 2]
    result = ''

    for number in numbers:
        number_position = coords[number]
        if number in fixed_left:
            result += 'L'
            left = number_position
        elif number in fixed_right:
            result += 'R'
            right = number_position
        else:
            left_distance = 0
            right_distance = 0
            for a, b, c in zip(left, right, number_position):
                left_distance += abs(a - c)
                right_distance += abs(b - c)

            if left_distance < right_distance:
                result += 'L'
                left = number_position
            elif left_distance > right_distance:
                result += 'R'
                right = number_position
            else:
                if hand == 'left':
                    result += 'L'
                    left = number_position
                else:
                    result += 'R'
                    right = number_position
    return result
