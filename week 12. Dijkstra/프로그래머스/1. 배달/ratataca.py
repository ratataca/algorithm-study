import heapq

def solution(N, road, K):
    answer = 0
    # 그래프 노드
    graph = [[] * (N + 1) for _ in range(N + 1)]
    print(graph)

    for s_n, e_n, w in road:
        graph[s_n].append([e_n, w])
        graph[e_n].append([s_n, w])

    # 방문 표시
    INF = int(1e9)
    distance = [INF] * (N + 1)
    start_node = 1
    
    # 다익스트라
    q = []
    distance[start_node] = 0
    heapq.heappush(q, (0, start_node))
    
    while q:
        w_n, s_n = heapq.heappop(q)

        if distance[s_n] < w_n:
            continue

        for e_n, w in graph[s_n]:
            cost = w_n + w    
            if cost <= K and cost < distance[e_n]:
                distance[e_n] = cost
                heapq.heappush(q, (cost, e_n))
        
    for n in distance:
        if n != INF:
            answer += 1

    return answer