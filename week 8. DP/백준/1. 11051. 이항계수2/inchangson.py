#이항 계수

import sys
sys.setrecursionlimit(10**6)

MOD = 10007
memo = [[0]*1001 for _ in range(1001)]

def memoization(n, k):
    if k == 0 or n == k:
        return 1
    if memo[n][k] != -1:
        return memo[n][k]
    memo[n][k] = (combination(n-1, k) + combination(n-1, k-1))%MOD
    return memo[n][k]

def tabulation(n, k):
    memo[1][0] = memo[1][1] = 1
    cur = 1
    while cur < n:
        for c in range(cur + 1):
            memo[cur+1][c] = (memo[cur+1][c] + memo[cur][c])%MOD
            memo[cur+1][c + 1] = (memo[cur+1][c + 1] + memo[cur][c])%MOD
        cur += 1

    return memo[n][k]

n, k = map(int, input().split())
print(tabulation(n, k))