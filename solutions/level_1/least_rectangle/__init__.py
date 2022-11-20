def solution(sizes: list[list[int]]) -> int:
    max_w = 0
    max_h = 0

    for size in sizes:
        w, h = sorted(size)
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
