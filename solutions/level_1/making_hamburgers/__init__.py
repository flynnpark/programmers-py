def solution(ingredient: list[int]) -> int:
    result = 0
    stack = []

    for item in ingredient:
        stack.append(item)

        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            result += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()

    return result
