import copy
import sys
sys.setrecursionlimit(10**8)
n = int(input())

heights = set()
default_matrix = [list(map(int, input().split())) for _ in range(n)]
for i in default_matrix:
  for j in i:
    heights.add(j)

heights = list(heights)
heights.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def show(matrix):
  for i in matrix:
    for j in i:
      print(j, end=' ')
    print()


def dfs(matrix, x, y, height):
  matrix[x][y] = -1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < size and 0 <= ny < size:
      if matrix[nx][ny] > height:
        dfs(matrix, nx, ny, height)

size = len(default_matrix)
result = []
for i in range(len(heights)-1):
  cnt = 0
  matrix = copy.deepcopy(default_matrix)
  for x in range(size):
    for y in range(size):
      if matrix[x][y] > heights[i]:
        cnt += 1
        dfs(matrix, x, y, heights[i])

  result.append(cnt)

if result:
  print(max(result))
else:
  print(1)
