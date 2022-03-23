# 1753
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

#Vertex:정점, Edge:간선
V, E  = map(int, input().split())
start_node = int(input())

graph = defaultdict(list)

for _ in range(E):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((node2, cost))

distance = [-1]*(V+1)
vertex_queue = [(0, start_node)]

while vertex_queue:
    cur_dist, cur_node = heapq.heappop(vertex_queue)
    if distance[cur_node] == -1:
        distance[cur_node] = cur_dist
        for next_node, next_dist in graph[cur_node]:
            cand = cur_dist + next_dist        
            if distance[next_node] == -1:
                    heapq.heappush(vertex_queue, (cand, next_node))

for node in range(1, V+1):
    if distance[node] == -1:
        print("INF")
    else:
        print(distance[node])