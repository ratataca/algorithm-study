import sys
input = sys.stdin.readline

N = int(input())
counsels = []
memo = [0]*(N+1)

for _ in range(N):
    counsels.append(list(map(int, input().split())))
counsels.append([1, 1])
for idx in range(N + 1):
    memo[idx] = max(memo[idx], memo[idx-1])
    
    cur_t, cur_p = counsels[idx]
    if idx + cur_t > N:
        continue

    memo[idx + cur_t] = max(memo[idx + cur_t], memo[idx] + cur_p)

print(memo[-1])