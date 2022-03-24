import heapq

INF = int(1e9)
                    
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
                    
    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b, c))
        graph[b].append((a, c))
        
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
    dijkstra(1)
    cnt = 0
    for dist in distance:
        if dist <= K:
            cnt += 1
    return cnt