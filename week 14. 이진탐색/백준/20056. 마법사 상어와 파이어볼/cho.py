N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[c - 1][r - 1].append((m, s, d))


def move(matrix):
    result = []
    for y in range(N):
        for x in range(N):
            if matrix[y][x]:
                result.append((x, y))

    for x, y in result:
        while len(matrix[y][x]) > 0:
            mass, speed, dir = matrix[y][x].pop()
            nx = (x + dx[dir] * speed) % N
            ny = (y + dy[dir] * speed) % N
            matrix[ny][nx].append((mass, speed, dir))


def divide(matrix):
    for y in range(N):
        for x in range(N):
            if len(matrix[y][x]) > 1:
                tot_mass = 0
                tot_speed = 0
                even_cnt = 0
                odd_cnt = 0
                cnt = 0

                for ball in matrix[y][x]:
                    mass = ball[0]
                    speed = ball[1]
                    dir = ball[2]
                    if dir % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1

                    tot_mass += mass
                    tot_speed += speed
                    cnt += 1

                l_mass = int(tot_mass / 5)
                if l_mass == 0:
                    matrix[y][x] = []
                    break
                l_speed = int(tot_speed / cnt)
                if even_cnt == 0 or odd_cnt == 0:
                    l_dirs = [0, 2, 4, 6]
                else:
                    l_dirs = [1, 3, 5, 7]
                matrix[y][x] = [
                    (l_mass, l_speed, l_dirs[0]),
                    (l_mass, l_speed, l_dirs[1]),
                    (l_mass, l_speed, l_dirs[2]),
                    (l_mass, l_speed, l_dirs[3]),
                ]


def total_check(matrix):
    total = 0
    for y in range(N):
        for x in range(N):
            for a in matrix[y][x]:
                total += a[0]
    return total


for _ in range(K):
    move(matrix)
    divide(matrix)
    print("-" * 200)

print(total_check(matrix))
