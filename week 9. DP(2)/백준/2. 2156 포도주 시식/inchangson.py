# boj 2156
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def drink(cur_idx, cur_cnt):
    if cur_idx == n:
        return 0
    if cur_cnt == 2:
        return drink(cur_idx + 1, 0)
    if memo[cur_idx][cur_cnt] != -1:
        return memo[cur_idx][cur_cnt]

    memo[cur_idx][cur_cnt] = max(drink(cur_idx + 1, 0), drink(cur_idx + 1, cur_cnt + 1) + wine[cur_idx])

    return memo[cur_idx][cur_cnt]
    
n = int(input())
wine = [int(input()) for _ in range(n)]
memo = [[-1, -1] for _ in range(n)]

ans = drink(0, 0)
print(ans)