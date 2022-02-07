n = int(input())
m = int(input())
network = [list(map(int, input().split())) for _ in range(m)]

checked = [0]*(n + 1)
checked[1] = 1
ans = 0
for relation in network:
  if relation[0] == 1:
    checked[relation[1]] = 1
    ans += 1

for relation in network:
  if checked[relation[0]] == 1:
    if checked[relation[1]] == 0:
      checked[relation[1]] = 2
      ans += 1
      
  elif checked[relation[1]] == 1:
    if checked[relation[0]] == 0:
      checked[relation[0]] = 2
      ans += 1
      
print(ans)