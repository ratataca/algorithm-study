from collections import deque

M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

TOVISIT = 0
TOMATO = 1
VISITED = 2

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

# Definition of Queue
q = deque([])
for y in range(N):
    for x in range(M):
        if map[y][x] == TOMATO:
            q.append([x, y, 0])


def bfs():
    while q:
        # O(1)
        x, y, d = q.popleft()

        for dx, dy in zip(DX, DY):
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and map[ny][nx] == TOVISIT:
                q.append([nx, ny, d + 1])
                map[ny][nx] = VISITED

    for m in map:
        if 0 in m:
            return -1
    return d


print(bfs())
