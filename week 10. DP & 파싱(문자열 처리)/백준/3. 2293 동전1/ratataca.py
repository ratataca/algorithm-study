N, K = [int(n) for n in input().split()]
coins = [int(input()) for _ in range(N)]

memo = [0] * (K+1)
memo = [0] * (K+1)

memo[0] = 1

for coin in coins:
    for val in range(coin, K+1):
        memo[val] += memo[val-coin]

print(memo[-1])