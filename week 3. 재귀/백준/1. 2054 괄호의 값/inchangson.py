def getCondIdx(src):
  if src == '(':
    return 0
  if src == '[':
    return 1
  return -1

def getFail():
  global isFail
  isFail = True
  return 0

def getScore(startIdx, endIdx, data, opt):

  if (endIdx - startIdx + 1) % 2:
    return getFail()
  if startIdx >= endIdx:
    return opt


  global paren, scoreBoard, isFail
  if isFail:
    return opt
    
  condIdx = getCondIdx(data[startIdx])
  if condIdx == -1:
    return getFail()

  nextIdx = startIdx
  cnt = 1
  while cnt and nextIdx < endIdx:
    nextIdx += 1
    if data[nextIdx] == paren[condIdx][0]:
      cnt += 1
    if data[nextIdx] == paren[condIdx][1]:
      cnt -= 1

  if cnt != 0:
    return getFail()

  innerScore = getScore(startIdx + 1, nextIdx - 1, data, 1)
  nextScore = getScore(nextIdx + 1, endIdx, data, 0)

  return innerScore * scoreBoard[condIdx] + nextScore

def checkData(data):
  if len(data) % 2:
    return False
  if len(data) < 1 or len(data) > 30:
    return False
  paren = ['(', ')', '[', ']']
  for d in data:
    if d not in paren:
      return False
  return True

def solution():
  data = input()

  if checkData(data) == False:
    return 0

  global paren, scoreBoard, isFail
  
  isFail = False
  scoreBoard = [2, 3]
  paren = [['(', ')'], ['[', ']']]

  score = getScore(0, len(data) - 1, data, 1)

  if isFail:
    return 0
  else:
    return score

print(solution())