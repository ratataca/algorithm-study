n = int(input())
matrix = [list(input()) for _ in range(n)]


def check_same(matrix):
    init = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if init != matrix[i][j]:
                return False

    return True


def recur(matrix):
    if check_same(matrix):
        return matrix[0][0]

    lu = recur([row[: len(matrix) // 2] for row in matrix[: len(matrix) // 2]])
    ru = recur([row[len(matrix) // 2 :] for row in matrix[: len(matrix) // 2]])
    ll = recur([row[: len(matrix) // 2] for row in matrix[len(matrix) // 2 :]])
    rl = recur([row[len(matrix) // 2 :] for row in matrix[len(matrix) // 2 :]])
    return "(" + lu + ru + ll + rl + ")"


print(recur(matrix))

# 성남시 분당구
