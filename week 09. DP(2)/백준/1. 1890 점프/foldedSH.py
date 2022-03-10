n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

results = [[0]*n for _ in range(n)]
results[0][0] = 1

for x in range(n):
    for y in range(n):
        if (x, y) == (n-1, n-1): # 도착 지점
            continue
        move_cnt = board[x][y] # 이동 가능한 칸
        
        # 이동 경우의 수: 아래, 오른쪽
        down = x + move_cnt
        right = y + move_cnt
        
        if down < n: # 게임판 내 좌표
            results[down][y] += results[x][y]
        if right < n:
            results[x][right] += results[x][y]
print(results[n-1][n-1])