# boj 1890
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def get_path_cnt(cur_x, cur_y):
    if cur_x >= n or cur_y >= n:
        return 0
    if memo[cur_x][cur_y] != -1:
        return memo[cur_x][cur_y]
    
    memo[cur_x][cur_y] = 0
    memo[cur_x][cur_y] += get_path_cnt(cur_x + graph[cur_x][cur_y], cur_y) 
    memo[cur_x][cur_y] += get_path_cnt(cur_x, cur_y + graph[cur_x][cur_y])

    return memo[cur_x][cur_y]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
memo  = [[-1]*n for _ in range(n)]
memo[n-1][n-1] = 1

ans = get_path_cnt(0, 0)

print(ans)