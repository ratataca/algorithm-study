import sys
input = sys.stdin.readline

N, M = [int(n) for n in input().split()]
area = [[int(n) for n in input().split()] for _ in range(N)]

K  = int(input())

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for y1, x1, y2, x2 in area:
    print(dp[y2][x2] - dp[y1-1][x1] - dp[y1][x1-1] + dp[y1-1][x1-1])