n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
check = [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = land[0][0]

for i in range(n):
    for j in range(m):
        if (i, j) == (0, 0):
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1]+land[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j]+land[i][j]
        else:
            dp[i][j] = land[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            
for one in check:
    # 1, 1, 3, 2 = 0, 0, 2, 1
    x1, y1, x2, y2 = one[0]-1, one[1]-1, one[2]-1, one[3]-1
    if (x1, y1) == (0, 0):
        result = dp[x2][y2]
    else:
        result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)