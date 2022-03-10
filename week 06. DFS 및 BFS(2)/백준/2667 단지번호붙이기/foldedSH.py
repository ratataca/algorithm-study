import itertools

def map_dfs(graph, x, y, num):
    if x < 0  or x >= nm or y < 0 or y >= nm:
        return False

    if graph[x][y] == 1:
        graph[x][y] = num # 방문처리
        
        for i in range(4):
            map_dfs(graph, x+dx[i], y+dy[i], num)
            
        return True
    
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

nm = int(input())
maps = [list(map(int, list(input()))) for i in range(nm)]

cnt = 0
num = -1
for i in range(nm):
    for j in range(nm):
        if map_dfs(maps, i, j, num):
            cnt += 1
            num -= 1
            
flat_maps = list(itertools.chain(*maps))
cnt_house = []
for i in range(1, cnt+1):
    cnt_house.append(flat_maps.count(-i))
cnt_house.sort()

print(cnt)
for i in range(cnt):
    print(cnt_house[i])