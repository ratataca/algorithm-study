import heapq

n = int(input())

heap = []
result = 0 
for _ in range(n):
  heapq.heappush(heap, int((input())))

while len(heap) != 1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  result += one+two
  heapq.heappush(heap, one+two)

print(result)
