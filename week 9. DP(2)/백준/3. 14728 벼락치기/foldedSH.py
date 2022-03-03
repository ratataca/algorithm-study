n, t = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(n)]

v = [0]
w = [0]
for chap in chapters:
    v.append(chap[1])
    w.append(chap[0])
    
ns = [[0] * (t+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, t+1):
        if j-w[i] >= 0: # True - 현재 단원을 공부할 시간적 여유가 있을 때
            ns[i][j] = max(ns[i-1][j], ns[i-1][j-w[i]]+v[i])
												# 현재 단원 공부X, 현재 단원 공부O할 때 얻는 배점

        else: # False - 현재 단원을 공부할 시간적 여유가 없을 때, 이전 시간
            ns[i][j] = ns[i-1][j]
print(ns[n][t])