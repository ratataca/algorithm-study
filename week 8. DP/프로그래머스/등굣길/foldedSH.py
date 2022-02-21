def solution(m, n, puddles):
    answer = 0
    path = [[0]*(m+1) for _ in range(n+1)]
    path[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] in puddles or [x, y] == [1, 1]:
                continue
            path[x][y] = path[x-1][y] + path[x][y-1]
    
    return path[n][m] % 1000000007