def hanoi(n, f, b, t, result):
    if n == 1:
        result.append([f,t])
    else:
        hanoi(n-1, f, t, b, result)
        result.append([f, t])
        hanoi(n-1, b, f, t, result)

def solution(n):
    result = []
    hanoi(n, 1,2,3, result)
    return result