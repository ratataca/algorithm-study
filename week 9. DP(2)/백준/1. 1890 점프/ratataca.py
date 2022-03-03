import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
map = [[int(n) for n in input().split()] for _ in range(N)]

node = map[0][0]
cnt = 0

def search_next_node(x, y):
    global cnt

    if x >= N or y >= N:
        return 0

    if x == N - 1 and y == N - 1:
        cnt += 1
        return 1
    
    node = map[y][x]
    nx, ny = x + node, y + node 
    
    search_next_node(x, ny)    
    search_next_node(nx, y)

    return cnt

print(search_next_node(0, 0))

