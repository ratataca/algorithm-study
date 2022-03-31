import sys

input = sys.stdin.readline
n = int(input())
t = []
p = []

dp = [0 for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

Max = 0

for i in range(n):
    Max = max(Max, dp[i])
    if i + t[i] <= n:
        dp[i + t[i]] = max(Max + p[i], dp[i + t[i]])

print(max(dp))
