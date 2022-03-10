# 9095
import sys
input = sys.stdin.readline

memo = [0] * 12
memo[1] = 1
memo[2] = 2
memo[3] = 4
memo[4] = 7
for n in range(5, 12):
    memo[n] = 2*memo[n-1] - memo[n-4]

t = int(input())
while t:
    print(memo[int(input())])
    t -= 1