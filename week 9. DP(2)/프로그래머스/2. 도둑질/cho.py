def solution(money):
  dp_start = [0] * len(money)
  dp_start[0] = money[0]
  dp_start[1] = money[0]

  for i in range(2, len(money)-1):
    dp_start[i] = max(dp_start[i-1], money[i]+dp_start[i-2])

  dp_end = [0] * len(money)
  dp_end[0] = 0
  dp_end[1] = money[1]

  for i in range(2, len(money)): 
    dp_end[i] = max(dp_end[i-1], money[i]+dp_end[i-2])

  return max(max(dp_start), max(dp_end))