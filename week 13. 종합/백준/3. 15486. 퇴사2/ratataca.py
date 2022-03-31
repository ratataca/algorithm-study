import sys

N = int(sys.stdin.readline())

T, P = [], []
dp = [0]*(N+1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])


for i in range(0, N):
    if T[i] <= N - i:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
        
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])