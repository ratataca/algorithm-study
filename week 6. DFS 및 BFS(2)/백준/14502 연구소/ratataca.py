from itertools import combinations
import copy
from collections import deque

N, M = [int(n) for n in input().split()]
map = [[int(s) for s in input().split()] for _ in range(N)]

SAFE = 0
WALL = 1
VIRUS = 2
VIRUS_VISITED = 3

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]


# 3개 영역 
possible_area = []
for i in range(N):
    for j in range(M):
        if map[i][j] == SAFE:
            possible_area.append([i, j])

search_idx = list(combinations(possible_area, r=3))
q = deque([])
max_safe_area = -1

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]
            if 0 <= nx < M and 0 <= ny < N and _map[ny][nx] == SAFE:
                q.append([nx, ny])
                _map[ny][nx] = VIRUS_VISITED


# search_idx를 이용한 벽 세우기
for area1, area2, area3 in search_idx:
    _map = copy.deepcopy(map)
    _map[area1[0]][area1[1]] = WALL
    _map[area2[0]][area2[1]] = WALL
    _map[area3[0]][area3[1]] = WALL
    

    # 최대의 0을 찾기
    result = -1
    for y in range(N):
        for x in range(M):
            if _map[y][x] == VIRUS:
                q.append([x, y])
                _map[y][x] = VIRUS_VISITED
                bfs()
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if _map[y][x] == SAFE:
                cnt += 1
    if max_safe_area < cnt:
        max_safe_area = cnt

print(max_safe_area)
