from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    for vertex in edge:
        start, end = vertex
        graph[start].append(end)
        graph[end].append(start)

    q = deque()
    q.append((1, 1))
    visited[1] = True
    while q:
        node, distance = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append((next_node, distance + 1))
                visited[next_node] = True
                distances[next_node] = distance + 1

    return distances.count(max(distances))
