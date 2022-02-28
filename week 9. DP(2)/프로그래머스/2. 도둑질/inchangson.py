import sys
sys.setrecursionlimit(10 ** 6)

def rob_town(idx, memo, money):
    if idx >= len(memo):
        return 0
    if memo[idx] != -1:
        return memo[idx]
    
    cand1 = money[idx] + rob_town(idx + 2, memo, money)
    cand2 = rob_town(idx + 1, memo, money)
    memo[idx] = max(cand1, cand2)
    
    return memo[idx]
    
def solution(money):
    answer = 0
    memo1 = [-1]*(len(money) - 1)
    memo2 = [-1]*len(money)
    #첫 번째 집 무조건 턴 경우
    cand1 = rob_town(0, memo1, money)
    #첫 번째 집 무조건 안 턴 경우
    cand2 = rob_town(1, memo2, money)
    answer = max(cand1, cand2)
    return answer