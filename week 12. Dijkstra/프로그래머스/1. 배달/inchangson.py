from heapq import *
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    
    dist  = [-1] * (N+1)
    graph = [[0] * (N+1) for _ in range(N+1)]
    
    for u, v, w in road:
        val = min(graph[u][v], w) if graph[u][v] else w
        graph[u][v] = graph[v][u] = val
    
    Q = [(0, 1)]
    
    while Q:
        total_dist, cur_node = heappop(Q)
        if dist[cur_node] != -1:
            continue
        dist[cur_node] = total_dist
        for next_node in range(N+1):
            if graph[cur_node][next_node]:
                cand = total_dist + graph[cur_node][next_node]
                
                heappush(Q, (cand, next_node))

    for node in range(N+1):
        if dist[node] != -1 and dist[node] <= K:
            answer +=1
    return answer