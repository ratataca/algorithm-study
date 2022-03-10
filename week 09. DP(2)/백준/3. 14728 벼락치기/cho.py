import sys

input = sys.stdin.readline

n, t = map(int, input().split())

arr = [[0, 0]]
dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
# print(dp)
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    time = arr[i][0]
    val = arr[i][1]
    for j in range(1, t + 1):
        if j >= time:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + val)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][t])
