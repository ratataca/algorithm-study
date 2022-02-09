def update_walls(walls, lab, m, value):
  for w in walls:
    lab[w//m][w%m] = value
  return

def is_empty(w, lab, m):
  return lab[w//m][w%m] == 0

def get_infected_cnt(r, c, lab, visited, cur_visit, direction):
  ret = 0
  for idx in range(4):
    nr = r + direction[idx][0]
    nc = c + direction[idx][1]
    if not 0 <= nr < len(lab):
      continue
    if not 0 <= nc < len(lab[0]):
      continue
    if lab[nr][nc] != 0:
      continue
    if visited[nr][nc] == cur_visit:
      continue
    visited[nr][nc] = cur_visit
    ret += get_infected_cnt(nr, nc, lab, visited, cur_visit, direction) + 1
  return ret

def get_safety_region(lab, viruses, empty_cnt, cur_visit, visited):
  total_infected_cnt = 0
  direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
  for (r, c) in viruses:
    tmp = get_infected_cnt(r, c, lab, visited, cur_visit, direction)
    
    total_infected_cnt += tmp
    
  return empty_cnt - total_infected_cnt - 3

n, m = map(int, input().split())
lab  = [list(map(int, input().split())) for _ in range(n)]
visited  = [[0] * m for _ in range(n)]

viruses = list()
empty_cnt = 0
for r in range(n):
  for c in range(m):
    if lab[r][c] == 2:
      viruses.append((r, c))
    elif lab[r][c] == 0:
      empty_cnt += 1
      
total     = n*m
max_val   = 0
cur_visit = 1

for w1 in range(total):
  if not is_empty(w1, lab, m):
    continue
  for w2 in range(w1 + 1, total):
    if not is_empty(w2, lab, m):
      continue
    for w3 in range(w2 + 1, total):
      if not is_empty(w3, lab, m):
        continue
      update_walls([w1, w2, w3], lab, m, 1)
      
      cand = get_safety_region(lab, viruses, empty_cnt, cur_visit, visited)
      
      cur_visit += 1
      if cand > max_val:
        max_val = cand
      update_walls([w1,w2,w3], lab, m, 0)

print(max_val)