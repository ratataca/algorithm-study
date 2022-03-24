import heapq
import sys

INF = int(1e9)

V, E = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
                
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)