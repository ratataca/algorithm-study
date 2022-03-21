import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
start_node = int(input())

INF = int(1e9)

graph = [[] * (V+1) for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))


def dijkstra(start_node):
    q = []
    start_weight = 0
    heapq.heappush(q, (start_weight, start_node))
    distance[start_node] = 0

    while q:
        weight, node = heapq.heappop(q)

        if distance[node] < weight:
            continue

        for n, w in graph[node]:
            cost = weight + w
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))


dijkstra(start_node)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])