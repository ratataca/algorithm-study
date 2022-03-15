import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def print_board():
    print('-' * 10)
    for r in range(N):
        for c in range(N):
            print(board[r][c], end=' ')
        print()
    print('-' * 10)

def imigrate(sr, sc, visited):
    total = 0
    memo = []
    is_changed = False
    dfs = [(sr,sc)]
    visited[sr][sc] = True
    
    while dfs:
        cr, cc = dfs.pop()
        memo.append((cr, cc))
        total += board[cr][cc]

        for d in dirs:
            nr = cr + d[0]
            nc = cc + d[1]
            if not ((0 <= nr < N) and (0 <= nc < N)):
                continue
            if not (L <= abs(board[cr][cc] - board[nr][nc]) <= R):
                continue
            if not visited[nr][nc]:
                is_changed = True
                dfs.append((nr, nc))
                visited[nr][nc] = True
                
    # memo => apply difference
    moved = total // len(memo)
    for r, c in memo:
        board[r][c] = moved
    
    return is_changed


days = 0
while True:
    visited = [[False]*N for _ in range(N)]
    is_changed = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            is_changed = imigrate(r, c, visited) | is_changed
    #print_board()
    if not is_changed:
        break
    days += 1

print(days)