from heapq import *
from collections import defaultdict


def dijkstra(start, dist, graph, INF):
    Q = [(0, start)]
    dist[start][start] = 0
    while Q:
        total_cost, cur_node = heappop(Q)
        
        if dist[start][cur_node] < total_cost:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            cand = next_cost + total_cost
            if cand < dist[start][next_node]:
                dist[start][next_node] = cand
                heappush(Q, (cand, next_node))
            
    return


def solution(n, s, a, b, fares):
    INF = 100000 * n + 1
    ans = INF
    
    dist  = [[INF] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    for stopover in range(1, n + 1):
        cost_stopover = dijkstra(stopover, dist, graph, INF)
        ans = min(ans, dist[stopover][s] + dist[stopover][a] + dist[stopover][b])

    return ans