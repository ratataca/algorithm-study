#등굣길
from collections import deque

def go_school(graph, m, n):
    D   = [[1, 0], [0, 1]]
    MOD = 1000000007
    
    memo  = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    memo[0][0] = 1
    
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1
    
    while q:
        cr, cc = q.popleft()
        
        for i in range(2):
            nr = cr + D[i][0]
            nc = cc + D[i][1]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if graph[nr][nc]:
                continue
            memo[nr][nc] += memo[cr][cc]
            memo[nr][nc] %= MOD
            if visit[nr][nc]:
                continue
            visit[nr][nc] = 1
            q.append((nr, nc))
    
    return memo[n - 1][m - 1]

def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    
    for p in puddles:
        graph[p[1] - 1][p[0] - 1] = 1
        
    return go_school(graph, m, n)