N, K = [int(n) for n in input().split()]

memo = [1] * (N + 1)
for i in range(1, N + 1):
    memo[i] = memo[i - 1] * i

result = memo[N] // (memo[K] * memo[N - K])

print(result % 10007)