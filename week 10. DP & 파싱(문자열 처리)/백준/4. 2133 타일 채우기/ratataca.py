# 2133
import sys
sys.setrecursionlimit(10**6)

N = int(input())

# 첫째 줄에 N(1 ≤ N ≤ 30)4
memo = [0] * (31)

memo[0] = 1
memo[2] = 3

if N % 2:
    print(0)
else:    
    for n in range(4, N+1, 2):
        # 2x3 도형으로 만들 수 있는 경우
        print(f"1. memo[{n}] = 3 * memo[{n - 2}] =", 3 * memo[n - 2])
        memo[n] = 3 * memo[n - 2]

        # 예외 경우들에 대한 경우(원본, 180 회전)
        for nxt in range(4, n + 1, 2):
            print(f"   2. memo[{n}] += 2 * memo[{n - nxt}] =", 2 * memo[n - nxt])
            memo[n] += 2 * memo[n - nxt]


    print(memo[n])