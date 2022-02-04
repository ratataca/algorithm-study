from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
cnt = 0
for i in range(n):
  for j in range(m):
    if matrix[i][j]==1:
      queue.append((i,j))

while queue:
  x, y = queue.popleft()
  for k in range(4):
    nx = x+dx[k]
    ny = y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if matrix[nx][ny]==0:
        matrix[nx][ny]=matrix[x][y]+1
        queue.append((nx, ny))

Max = 0
breaked = False
for i in matrix:
  for j in i:
    if j == 0:
      print(-1)
      breaked = True
      break
    else:
      Max = max(Max, j)
  if breaked:
    break

if not breaked:
  print(Max-1)

