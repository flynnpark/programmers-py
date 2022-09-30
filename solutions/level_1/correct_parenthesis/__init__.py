pair = {
    ')': '(',
    '}': '{',
    ']': '[',
}


def solution(s: str) -> bool:
    stack = []

    for char in s:
        if char in pair.values():
            stack.append(char)

        elif len(stack) == 0 or pair[char] != stack.pop():
            return False

    return True if len(stack) == 0 else False
