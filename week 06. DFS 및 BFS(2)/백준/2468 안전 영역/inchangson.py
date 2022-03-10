def visit_town(r, c, rain, cur_visit):  
  memo = [(r, c)]
  while memo:
    cr, cc = memo.pop()
    for idx in range(4):
      nr = cr + dr[idx]
      nc = cc + dc[idx]
      if nr < 0 or nr >= n or nc < 0 or nc >= n:
        continue
      if town[nr][nc] <= rain:
        continue
      if visited[nr][nc] == cur_visit:
        continue
      visited[nr][nc] = cur_visit
      memo.append((nr, nc))
  return

def get_safety_cnt(rain, cur_visit):
  ret = 0
  for r in range(n):
    for c in range(n):
      if town[r][c] > rain and visited[r][c] != cur_visit:
        ret += 1
        visited[r][c] = cur_visit
        visit_town(r, c, rain, cur_visit)
  return ret

n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dr = [1, -1, 0,  0]
dc = [0,  0, 1, -1]

ans = 1
cur_visit = 1
for rain in range(0, 100):
  cand = get_safety_cnt(rain, cur_visit)
  cur_visit += 1
  if ans < cand:
    ans = cand
print(ans)