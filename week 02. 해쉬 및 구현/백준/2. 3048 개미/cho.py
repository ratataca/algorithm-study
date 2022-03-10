m, n = map(int, input().split())

forward = list(input())
backward = list(input())

times = int(input())
forward.reverse()
directions = {}

for element in forward:
  directions[element] = 1

for element in backward:
  directions[element] = 0

position = forward + backward


for _ in range(times):
  i = 0
  while i <len(position) -1:
    if directions[position[i]] and not directions[position[i+1]]:
      position[i], position[i+1] = position[i+1],position[i] 
      i += 1
    i += 1

print(''.join(position))