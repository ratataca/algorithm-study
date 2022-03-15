import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())

matrix = [list(map(int, input().split()))for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if n == 1:
    print(0)
    exit()


def dfs(x, y, matrix):
    stack = [(x, y)]
    Set = {(x, y)}
    total = 0
    number = 0
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and l <= abs(matrix[y][x]-matrix[ny][nx]) <= r:
                stack.append((nx, ny))
                Set.add((nx, ny))
                visited[ny][nx] = True
                total += matrix[ny][nx]
                number += 1

    if total:
        total_Set.append((total, number, Set))


cnt = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    checked = False
    total_Set = []
    for i in range(n):
        for j in range(n):
            dfs(j, i, matrix)
    if len(total_Set) > 0:
        checked = True
        for total, number, Set in total_Set:
            avg = total//number
            for a, b in Set:
                matrix[b][a] = avg
    if not checked:
        break
    else:
        cnt += 1
print(cnt)
