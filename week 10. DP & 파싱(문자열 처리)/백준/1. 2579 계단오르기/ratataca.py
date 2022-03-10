### 왜 92% 가다가 틀리는 거지..?
import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]

for _ in range(N):
    stairs.append(int(input()))

memo = [0] * (N+1)
memo[1] = stairs[1]
memo[2] = stairs[1] + stairs[2]
if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[2])
else:
    for i in range(3, N+1):
        memo[i] = max(memo[i-2], stairs[i-1]+memo[i-3]) + stairs[i]
        print('i: ', i, " | ", memo )

    print(memo[-1])


# import sys
# read = sys.stdin.readline

# n = int(read())
# stairs = [0] + [int(read()) for _ in range(n)] + [0]
# cache = [0] * (n+2)
# cache[1] = stairs[1]
# cache[2] = cache[1] + stairs[2]

# for i in range(3, n+1):
#     cache[i] = max(cache[i-2], cache[i-3] + stairs[i-1]) + stairs[i]
# print(cache[n])