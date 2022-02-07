from collections import deque
N = int(input())
map = [[int(s) for s in input()] for _ in range(N)]

VISITABLE = 1
VISITED = 2

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

visited = []
q = deque([])


def bfs():
    visited.append(1)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] == VISITABLE:
                q.append([nx, ny])
                map[ny][nx] = VISITED
                visited[-1] += 1


# 큐 초기값 및 BFS 호출
for y in range(N):
    for x in range(N):
        if map[y][x] == 1:
            q.append([x, y])
            map[y][x] = VISITED
            bfs()

# 출력
print(len(visited))
visited = sorted(visited)
for v in visited:
    print(v)
