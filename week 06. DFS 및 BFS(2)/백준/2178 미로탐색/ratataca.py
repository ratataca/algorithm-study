from collections import deque

# (1, 1) -> (N, M) 으로 이동
N, M = [int(n) for n in input().split()]
map = [[int(s) for s in input()] for _ in range(N)]

VISITABLE = 1
VISITED = 2

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]


def bfs():
    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]
            if 0 <= nx < M and 0 <= ny < N and map[ny][nx] == VISITABLE:
                if ny == N - 1 and nx == M - 1:
                    return cnt + 1
                q.append([nx, ny, cnt + 1])
                map[ny][nx] = VISITED
        
    
# x, y, cnt
q = deque([])
q.append([0, 0, 1])
map[0][0] = VISITED
print(bfs())