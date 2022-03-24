N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하우상좌

def rotate():
    carr = [[] for _ in range(N)]

    for i in range(N):
        carr[i]=arr[i][:]

    sr, sc, er, ec = 0, 0, N - 1, M - 1
    for _ in range(min(M, N)//2):
        r = sr
        c = sc
        for d in move:
            while True:
                nr = r + d[0]
                nc = c + d[1]
                if sr <= nr <= er and sc <= nc <= ec:
                    arr[nr][nc] = carr[r][c]
                    r = nr
                    c = nc
                else:
                    break
        sr += 1
        sc += 1
        er -= 1
        ec -= 1


for r in range(R):  # 전체 회전 횟수
    rotate()

for i in range(N):
    print(*arr[i])