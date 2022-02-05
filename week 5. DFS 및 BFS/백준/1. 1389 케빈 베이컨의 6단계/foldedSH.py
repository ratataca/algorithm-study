INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
dist_cnt = []
for start in range(1, n+1):
    dist = 0
    for end in range(1, n+1):
        if start == end:
            continue
        dist += graph[start][end]
    dist_cnt.append((start, dist))
dist_cnt.sort(key = lambda x : x[1])
print(dist_cnt[0][0])