n, m = map(int, input().split())
k = int(input())  # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n + 1)]  # 1번 노드부터 시작하므로 하나더 추가

distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())  # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치
    graph[u].append((v, w))  # 거리 정보와 도착노드를 같이 입력합니다.


import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 우선순위, 값 형태로 들어간다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)  # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if distance[now] < dist:  # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue  # 따라서 다음으로 넘어간다.

        for i in graph[now]:  # 연결된 모든 노드 탐색
            if dist + i[1] < distance[i[0]]:  # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist + i[1]  #
                heapq.heappush(q, (dist + i[1], i[0]))


dijkstra(k)
result = []
for i in range(1, len(distance)):
    if distance[i] == INF:
        result.append("INF")
    else:
        result.append(str(distance[i]))

print("\n".join(result))