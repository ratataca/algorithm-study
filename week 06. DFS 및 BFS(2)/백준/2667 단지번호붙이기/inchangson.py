def get_size(r, c, visited):
  ret = 1
  #print(r, c)
  for idx in range(4):
    nr = r + dy[idx]
    nc = c + dx[idx]

    if 0 <= nr < n and 0 <= nc < n:
      if visited[nr][nc] == 0:
        if apart[nr][nc] == '1':
          visited[nr][nc] = 1
          ret += get_size(nr, nc, visited)
  return ret

n = int(input())
apart = [input() for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]

cnt = 0
list_size = []
for r in range(n):
  for c in range(n):
    if apart[r][c] == '1' and visited[r][c] == 0:
      cnt += 1
      visited[r][c] = 1
      list_size.append(get_size(r, c, visited))

print(cnt)
list_size.sort()
for sz in list_size:
  print(sz)