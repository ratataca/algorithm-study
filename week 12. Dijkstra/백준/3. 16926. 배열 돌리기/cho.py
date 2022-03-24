import sys
n, m, r = map(int, input().split())
input = sys.stdin.readline
matrix = [list(input().split()) for _ in range(n)]

def show(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

def turn(matrix):
    sqn = min(n,m)//2
    for k in range(sqn):
        tmp = matrix[k][k]
        for i in range(k,m-1-k):
            matrix[k][i] = matrix[k][i+1]

        for i in range(k, n-1-k):
            matrix[i][m-1-k] = matrix[i+1][m-1-k]

        for i in range(m-1-k, k, -1):
            matrix[n-1-k][i] = matrix[n-1-k][i-1]

        for i in range(n-1-k, k, -1):
            matrix[i][k] = matrix[i-1][k]

        matrix[k+1][k] = tmp

for _ in range(r):
    turn(matrix)
show(matrix)

import sys
