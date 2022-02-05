from collections import deque

def bfs(queue):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append((nx, ny))
                
m, n = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(n)]
ripe = []
for row in range(n):
    for col in range(m):
        if tomatos[row][col] == 1:
            ripe.append((row, col))
queue = deque(ripe)
bfs(queue)

_max = max(max(row) for row in tomatos)
for row in range(n):
    for col in range(m):
        if tomatos[row][col] == 0:
            print(-1)
            break
    else:
        continue
    break
else:
    print(_max-1)