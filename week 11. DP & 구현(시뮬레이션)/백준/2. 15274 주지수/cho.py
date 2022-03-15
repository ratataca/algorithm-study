n, m = map(int, input().split())
matrix = [[0 for _ in range(m+1)]]
matrix += [[0]+list(map(int, input().split())) for _ in range(n)]

# print(matrix)
test_case = int(input())

for i in range(1, n+1):
    for j in range(1, m+1):
        matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

# print(matrix)
result = []
for _ in range(test_case):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(matrix[x2][y2]-matrix[x2][y1-1] -
                  matrix[x1-1][y2]+matrix[x1-1][y1-1])

for i in result:
    print(i)
