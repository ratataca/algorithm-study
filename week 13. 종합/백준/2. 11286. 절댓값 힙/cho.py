import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    inp = int(input())

    if inp:
        heapq.heappush(heap, (abs(inp), inp))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
