# 2133
import sys
sys.setrecursionlimit(10**6)

n = int(input())
memo = [0] * (31)

memo[0] = 1
memo[2] = 3

if n % 2:
    print(0)
else:    
    for cnt in range(4, n+1, 2):
        memo[cnt] = 3*memo[cnt - 2]
        for nxt in range(4, cnt+1, 2):
            memo[cnt] += 2*memo[cnt - nxt]
    print(memo[n])