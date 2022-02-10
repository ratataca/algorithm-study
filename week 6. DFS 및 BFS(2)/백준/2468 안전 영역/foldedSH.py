import sys
sys.setrecursionlimit(1000000)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(graph, x, y):
    n = len(graph)
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        
        for i in range(4):
            dfs(graph, x+dx[i], y+dy[i])
        return True

    return False

n = int(input())
regions = [list(map(int, input().split())) for _ in range(n)]

cnts = []
for md in range(101):
    nodes = []
    for i in range(n):
        nodes.append([int(i<=md) for i in regions[i]])
    #print(nodes)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(nodes, i, j):
                cnt += 1
    cnts.append(cnt)
    #print(cnt)
print(max(cnts))