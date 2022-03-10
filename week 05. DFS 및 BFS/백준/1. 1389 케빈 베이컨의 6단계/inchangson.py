from collections import deque

def get_bacon_num(cur_usr):
  global network, usr_cnt
  ret = 0
  memo = deque()
  memo.append((cur_usr, 0))
  checked = [False]*(usr_cnt+1)
  checked[0] = True
  while memo:
    usr, step = memo.popleft()
    ret += step
    for next_usr in range(usr_cnt + 1):
      if checked[next_usr]:
        continue
      if network[usr][next_usr]:
        memo.append((next_usr, step + 1))
        checked[next_usr] = True
  return ret

#start input
usr_cnt, relation_cnt = map(int, input().split())

network = [[False]*(usr_cnt + 1) for _ in range(usr_cnt + 1)]

for _ in range(relation_cnt):
  n1, n2 = map(int, input().split())
  network[n1][n2] = network[n2][n1] = True
#end input

min_val = usr_cnt**2
min_usr = 0
for usr in range(usr_cnt):
  tmp = get_bacon_num(usr + 1)
  if tmp < min_val:
    min_val = tmp
    min_usr = usr + 1


print(min_usr)
