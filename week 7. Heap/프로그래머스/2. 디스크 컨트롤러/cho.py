import heapq

def solution(jobs):
  answer = 0
  end = 0
  i = 0
  start = -1 
  heap = []
  
  while i < len(jobs):
    for j in jobs:
      if start < j[0] <= end:
        heapq.heappush(heap, [j[1], j[0]])
    if len(heap) > 0: 
      cur = heapq.heappop(heap)
      start = end
      end += cur[0]
      answer += end - cur[1] 
      i +=1
    else: 
      end += 1
  return answer // len(jobs)