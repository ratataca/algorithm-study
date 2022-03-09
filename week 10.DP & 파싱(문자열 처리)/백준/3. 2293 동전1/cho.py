n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1


for coin in arr:
    for j in range(coin, k + 1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]

print(dp[k])
