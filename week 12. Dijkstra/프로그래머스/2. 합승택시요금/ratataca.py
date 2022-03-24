import heapq

def dijkstra(N, S, graph):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    distance[S] = 0

    q = []
    heapq.heappush(q, (0, S))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_cost:
            continue

        for next_node, next_cost in graph[cur_node]:
            total_cost = cur_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))
    return distance


def solution(N, S, A, B, fares):
    graph = [[] * (N + 1) for _ in range(N + 1)]
    for s_n, e_n, w in fares:
        graph[s_n].append([e_n, w])
        graph[e_n].append([s_n, w])

    
    answer = int(1e9) 
    # 동승한 지점 찾기
    for point in range(1, N + 1):
        distance = dijkstra(N, point, graph)
        answer = min(answer, distance[S] + distance[A] + distance[B])
    
    return answer