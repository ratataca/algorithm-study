from collections import deque

def input_data():
  global n, m, tomatoes
  n, m = map(int, input().split())
  tomatoes = [list(map(int, input().split())) for _ in range(m)]

def initial_state(memo):
  global n, m, tomatoes, target_cnt
  target_cnt = 0
  for x in range(n):
    for y in range(m):
      if tomatoes[y][x] == 0:
        target_cnt += 1
      elif tomatoes[y][x] == 1:
        memo.append((x, y, 0))

def get_complete_day(memo):
  global n, m, tomatoes, target_cnt
  if target_cnt == 0:
    return 0
  direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

  while memo:
    cur_x, cur_y, cur_d = memo.popleft()
    for d in range(len(direction)):
      next_x = cur_x + direction[d][1]
      next_y = cur_y + direction[d][0]
      if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
        continue
      if tomatoes[next_y][next_x] == 0:
        tomatoes[next_y][next_x] = 1
        target_cnt -= 1
        if target_cnt == 0:
          return cur_d + 1
        memo.append((next_x, next_y, cur_d + 1))

  return -1

def solve():
  memo = deque()
  initial_state(memo)
  return get_complete_day(memo)

input_data()
print(solve())