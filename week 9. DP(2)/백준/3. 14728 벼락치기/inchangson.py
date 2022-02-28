import sys
input = sys.stdin.readline

def get_max_score(idx, rest):
    global exam
    if idx == len(exam):
        return 0
    if rest < exam[idx][0]:
        return 0
    if memo[idx][rest] != -1:
        return memo[idx][rest]
    
    cand1 = get_max_score(idx+1, rest)
    cand2 = get_max_score(idx+1, rest - exam[idx][0]) + exam[idx][1]

    memo[idx][rest] = max(cand1, cand2)
    
    return memo[idx][rest]
    
S, T = map(int, input().split(' '))
exam = [[0, 0] for _ in range(S)]
for idx in range(S):
    exam[idx][0], exam[idx][1] = map(int, input().split(' '))

memo = [[-1]*(T + 1) for _ in range(S)]

exam.sort()
print(get_max_score(0, T))