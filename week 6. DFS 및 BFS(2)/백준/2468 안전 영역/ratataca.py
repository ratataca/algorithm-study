from collections import deque

N = int(input())
map = [[int(s) for s in input().split()] for _ in range(N)]


VISITABLE = 1
VISITED = 2


DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

result = []

def bfs(map):
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]

            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] == VISITABLE:
                q.append([nx, ny])
                map[ny][nx] = VISITED

# 큐 선언
q = deque([])

# map에서 max 값 찾기
max_num = max([max(n) for n in map])

# max 만큼 M 탐색
for num in range(1, max_num):
    _map = []
    for y in map:
        _map.append([])
        for x in y:
            if x <= num:
                _map[-1].append(0)
            else:
                _map[-1].append(1)

    visited = 0
    # 큐 초기화 
    for y in range(N):
        for x in range(N):
            if _map[y][x] == VISITABLE:
                q.append([x, y])
                bfs(_map)
                visited += 1
    result.append(visited)

if result:
    print(max(result))
else:
    print(1)