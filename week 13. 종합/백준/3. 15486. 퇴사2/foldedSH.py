import sys

n = int(sys.stdin.readline())

t, p = [], []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    t.append(w) # 소요 기간
    p.append(v) # 상담 비용
    
dp = [0]*(n+1)

_sum = 0
for i in range(n):
    _sum = max(_sum, dp[i]) # 현재 최대 비용

    j = i+t[i] # i일 상담 후 다음 상담 가능 날짜
    if j > n: # 퇴사 후 날짜면 pass
        continue
    dp[j] = max(_sum+p[i], dp[j]) #  (현재 비용+i일 상담 비용) vs i일 상담 종료날 비용
print(max(dp))