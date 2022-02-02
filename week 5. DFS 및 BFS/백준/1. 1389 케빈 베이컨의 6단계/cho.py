n, m = map(int, input().split())

matrix = [[n]*n for _ in range(n)]
for _ in range(m):
  a,b = map(int, input().split())
  matrix[a-1][b-1] = matrix[b-1][a-1] = 1

for i in range(n):
  matrix[i][i] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]

result = []
for i in (matrix):
  result.append(sum(i))

print(result.index(min(result))+1)
