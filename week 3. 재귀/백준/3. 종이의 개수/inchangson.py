def isSameKind(sr, sc, sz):
  global paper  
  color = paper[sr][sc]
  for r in range(sr, sr + sz):
    for c in range(sc, sc + sz):
      if paper[r][c] != color:
        return False
  return True

def cutPaper(sr, sc, sz):
  if isSameKind(sr, sc, sz):
    global paper, paperCnt
    paperCnt[paper[sr][sc]] += 1
    return
  
  newSz = sz//3
  for i in range(3):
    for j in range(3):
      cutPaper(sr + i*newSz, sc + j*newSz, newSz)

  
  
n = int(input())
paper = [[int(x) for x in input().split()]for y in range(n)]
paperCnt = [0, 0, 0]

cutPaper(0, 0, n)

print(paperCnt[-1])
print(paperCnt[0])
print(paperCnt[1])


