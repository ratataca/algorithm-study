from collections import deque

def check_pos(r, c):
  if r < 0 or r >= n:
    return False
  if c < 0 or c >= m:
    return False
  if visited[r][c]:
    return False
  if maze[r][c] == WALL:
    return False
  return True

def get_shortest():
  memo = deque()
  memo.append((0, 0, 1))
  while memo:
    r, c, d = memo.popleft()
    
    if r == n - 1 and c == m - 1:
      return d

    for idx in range(4):
      nr = r + DR[idx]
      nc = c + DC[idx]

      if check_pos(nr, nc):
        visited[nr][nc] = True
        memo.append((nr, nc, d + 1))
  return -1

n, m = map(int, input().split())
maze = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
PATH = '1'
WALL = '0'

DR = [1, -1, 0,  0]
DC = [0,  0, 1, -1]

print(get_shortest())