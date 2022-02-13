# boj 1715
import sys
from heapq import *

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heappush(heap, int(sys.stdin.readline()))
ans = 0
while len(heap) > 1:
    next = heappop(heap) + heappop(heap)
    ans += next
    heappush(heap, next)
print(ans)