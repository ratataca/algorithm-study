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
        
    print(memo[-1])