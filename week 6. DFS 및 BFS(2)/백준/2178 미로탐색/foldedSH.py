from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽
            if graph[nx][ny] == 0:
                continue
            
            # 첫 방문
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())
miro = [list(map(int, list(input()))) for i in range(n)]

print(bfs(0, 0, miro))