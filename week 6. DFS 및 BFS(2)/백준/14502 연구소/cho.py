import copy
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]
def show(matrix):
  for i in matrix:
    for j in i:
      print(j, end=' ')
    print()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(matrix, x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if matrix[nx][ny] == 0:
        matrix[nx][ny] = 2
        dfs(matrix, nx, ny)

def run_dfs():
  global matrix
  new_matrix = copy.deepcopy(matrix)
  for x in range(n):
    for y in range(m):
      if matrix[x][y] == 2:
        dfs(new_matrix, x, y)
  return new_matrix
  
def count_safe(matrix):
  count = 0
  for i in range(n):
    for j in range(m):
      if matrix[i][j]==0:
        count+=1
  return count

size = n * m 
maxVal = 0
for i in range(size-2):
  for j in range(i+1, size-1):
    for k in range(j+1, size):
      i_x = i%n
      i_y = i//n
      j_x = j%n
      j_y = j//n
      k_x = k%n
      k_y = k//n

      if matrix[i_x][i_y]==0 and matrix[j_x][j_y]==0 and matrix[k_x][k_y]==0 :
        matrix[i_x][i_y] = 1
        matrix[j_x][j_y] = 1
        matrix[k_x][k_y] = 1
        result = run_dfs()
        maxVal = max(maxVal, count_safe(result))
        matrix[i_x][i_y] = 0
        matrix[j_x][j_y] = 0
        matrix[k_x][k_y] = 0

print(maxVal)