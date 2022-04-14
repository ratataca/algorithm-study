from collections import deque


def solution(n, results):
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for result in results:
        a, b = result
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = -1

    win_result = []
    lose_result = []

    for i in range(n):
        visited = [False] * n
        visited[i] = True
        q = deque()
        q.append(i)
        win_cnt = 0
        while q:
            value = q.pop()
            for i in range(len(graph[value])):
                if not visited[i] and graph[value][i] == 1:
                    win_cnt += 1
                    visited[i] = True
                    q.append(i)
        win_result.append(win_cnt)

    for i in range(n):
        visited = [False] * n
        visited[i] = True
        q = deque()
        q.append(i)
        lose_cnt = 0
        while q:
            value = q.pop()
            for i in range(len(graph[value])):
                if not visited[i] and graph[value][i] == -1:
                    lose_cnt += 1
                    visited[i] = True
                    q.append(i)
        lose_result.append(lose_cnt)
    answer = 0
    for i in range(n):
        if win_result[i] + lose_result[i] == n - 1:
            answer += 1
    return answer
