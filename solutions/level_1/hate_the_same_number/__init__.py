def solution(arr: list[int]) -> list[int]:
    stack = arr[:1]

    for num in arr[1:]:
        if num != stack[-1]:
            stack.append(num)

    return stack
