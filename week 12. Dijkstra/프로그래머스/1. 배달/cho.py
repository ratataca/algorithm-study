def solution(N, road, K):
    INF = 123432424
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N+1)]
    for line in road:
        start, end, d = line
        graph[start].append((end, d))
        graph[end].append((start, d))

    import heapq
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            d, now = heapq.heappop(q)
            
            if distance[now] < d:
                continue
            
            for i in graph[now]: # (end,d)
                if d + i[1] < distance[i[0]]:
                    distance[i[0]] = d + i[1]
                    heapq.heappush(q, (d + i[1], i[0]))
    dijkstra(1)
    cnt = 0
    for i in range(N+1):
        if distance[i] <= K:
            cnt += 1 
    return cnt