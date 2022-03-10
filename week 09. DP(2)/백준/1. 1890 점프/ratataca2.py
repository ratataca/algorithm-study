import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
map = [[int(n) for n in input().split()] for _ in range(N)]
node = map[0][0]

# dp -> memo
memo = [[-1]*N for _ in range(N)]

def search_next_node(x, y):
    if x >= N or y >= N:
        return 0

    if x == N - 1 and y == N - 1:
        return 1
    #
    if memo[x][y] != -1:
        return memo[x][y]

    node = map[y][x]

    if node == 0:
        return 0

    nx, ny = x + node, y + node

    ret = 0
    ret += search_next_node(x, ny)
    ret += search_next_node(nx, y)

    memo[y][x] = ret
    return ret



print(search_next_node(0, 0))s