import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

## 플로이드 와샬: 모든 노드 간 최단 경로
graph = [[int(1e8)]*n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             graph[i][j] = 0

for i in range(n):
  graph[i][i] = 0

for _ in range(m):
    i, j, c = map(int, input().split())
    if graph[i-1][j-1] > c: # i, j가 겹치는 경우 존재
        graph[i-1][j-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == int(1e8):
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()