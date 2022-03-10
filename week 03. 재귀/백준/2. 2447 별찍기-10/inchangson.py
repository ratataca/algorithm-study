def solve(sr,sc,cur):
  if cur == 1:
    global stars
    stars[sr][sc] = '*'
    return
  
  next = cur // 3
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        continue
      solve(sr + i * next, sc + j * next, next)
n = int(input())
stars = [[' ' for col in range(n)] for row in range(n)]
solve(0, 0, n)

for i in range(n):
  print(''.join(stars[i]))

