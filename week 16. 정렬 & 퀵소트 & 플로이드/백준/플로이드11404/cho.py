node_n = int(input())
vertex_n = int(input())


def show(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


matrix = [[float("inf") for _ in range(node_n)] for _ in range(node_n)]
for _ in range(vertex_n):
    a, b, c = map(int, input().split())

    if matrix[a - 1][b - 1] > c:
        matrix[a - 1][b - 1] = c

for k in range(node_n):
    for i in range(node_n):
        for j in range(node_n):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(node_n):
    matrix[i][i] = 0

for i in range(node_n):
    for j in range(node_n):
        if matrix[i][j] == float("inf"):
            matrix[i][j] = 0

show(matrix)
