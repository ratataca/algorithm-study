N = int(input())
wine = [0] * 10000

for i in range(N):
    wine[i] = int(input())
memo = [0] * 10000

memo[0] = wine[0]
memo[1] = wine[0] + wine[1]
memo[2] = max(wine[2] + wine[0], wine[2] + wine[1], memo[1])

for i in range(3, N):
    memo[i] = max(wine[i] + memo[i-2], wine[i] + wine[i-1] + memo[i-3], memo[i-1])

print(max(memo))