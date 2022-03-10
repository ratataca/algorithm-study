result = []


def hanoi(n, start, end, middle):
    global result

    if n == 1:
        result.append([start, end])
    else:
        hanoi(n - 1, start, middle, end)
        result.append([start, end])
        hanoi(n - 1, middle, end, start)


def solution(n):
    hanoi(n, 1, 3, 2)
    return result