# 2293
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
memo = [0] * (k+1)
memo[0] = 1

for coin in coins:
    for val in range(coin, k+1):
        memo[val] += memo[val-coin]
            
print(memo[k])