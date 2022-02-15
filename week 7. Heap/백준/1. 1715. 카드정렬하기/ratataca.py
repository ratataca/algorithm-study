import heapq

N = int(input())
minHeap = [int(input()) for _ in range(N)]

heapq.heapify(minHeap)

result = 0

while True:
    if len(minHeap) == 1:
        break
    
    min1 = heapq.heappop(minHeap)
    min2 = heapq.heappop(minHeap)

    result += (min1 + min2)
    heapq.heappush(minHeap, min1 + min2)

print(result)