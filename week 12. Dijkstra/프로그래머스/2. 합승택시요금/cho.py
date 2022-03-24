import heapq
def solution(n, s, a, b, fares):
    INF = 1e8
    graph = [[] for _ in range(n+1)]
    
    for fare in fares:
        start, end, cost = fare
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    
    def dijkstra(start, end):
        distance = [INF for _ in range(n+1)]
        distance[start] = 0
        q = [(0, start)]
        while q:
            d, s = heapq.heappop(q)
            if distance[s] < d:
                continue
            for i in graph[s]:
                if d+i[1] < distance[i[0]]:
                    distance[i[0]] = d + i[1]
                    heapq.heappush(q, (d+i[1],i[0]))
        return distance[end]


    result = INF
    for i in range(1, n + 1):
        result = min(result, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return result