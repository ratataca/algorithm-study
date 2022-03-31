# 11286
import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    k = int(input())
    if k:
        heappush(pq, (abs(k), k))
        
    else:
        if pq:
            print(heappop(pq)[1])
        else:
            print(0)