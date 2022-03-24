from collections import defaultdict
n, d = map(int, input().split())

Dist = [i for i in range(d+1)]
graph = defaultdict(list)

for _ in range(n):
    u, v, w = map(int, input().split())
    if v - u > w and v <= d:
        graph[u].append((v,w))

for i in range(d+1):
    if i != 0:
        Dist[i] = min(Dist[i], Dist[i-1]+1)
    for v, w in graph[i]:
        if Dist[v] > w + Dist[i]:
            Dist[v] = w + Dist[i]


print(Dist[-1])