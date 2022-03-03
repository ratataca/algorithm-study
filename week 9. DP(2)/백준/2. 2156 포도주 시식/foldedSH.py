n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0]*n
dp[0] = wines[0]

# 포도주 잔의 개수가 2개 이상인 경우
if n > 1:
    dp[1] = wines[0]+wines[1]

# 포도주 잔의 개수가 3개 이상인 경우
if n > 2:
    dp[2] = max(dp[1], wines[1]+wines[2], dp[0]+wines[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i]+wines[i-1])
        
print(dp[n-1])