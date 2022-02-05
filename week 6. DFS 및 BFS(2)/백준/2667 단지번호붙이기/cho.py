N = int(input())

matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
number = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
counts = []

def BFS(i, j):
  stack=[(i, j)]
  count = 0
  while stack:
    x, y = stack.pop()  
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < N:
        if matrix[nx][ny]==1 and visited[nx][ny]==0:
          visited[nx][ny]=number
          # print(number)
          stack.append((nx, ny))
          count+=1
      # print(queue)
  
  counts.append(count)
  # for ele in visited:
  #   print(ele)
  
for i in range(N):
  for j in range(N):
    if matrix[i][j]==1 and visited[i][j]==0:
      BFS(i, j)

print(counts)