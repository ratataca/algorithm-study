# 2579
import sys
input = sys.stdin.readline

def solve(idx, cnt):
    if idx > n or cnt == 3:
        return -3000000
    if memo[idx][cnt] != -1:
        return memo[idx][cnt]
    
    memo[idx][cnt] = stairs[idx]
    memo[idx][cnt] += max(solve(idx+1, cnt+1), solve(idx+2, 1))
    
    return memo[idx][cnt]
    
n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
memo = [[-1, -1, -1] for _ in range(n+1)]
memo[n] = [stairs[n], stairs[n], stairs[n]]

print(solve(0, 0))