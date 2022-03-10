def solution(m, n, puddles):
    matrix = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[0][0] = 1
            if [j+1, i+1] in puddles:
                matrix[i][j]=0
            else:
                if i==0:
                    matrix[i][j]=matrix[i][j-1]
                elif j==0:
                    matrix[i][j]=matrix[i-1][j]
                else:
                    matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
                
    return matrix[n-1][m-1]%1000000007