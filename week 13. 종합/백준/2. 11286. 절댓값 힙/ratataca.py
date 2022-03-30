import sys
import heapq

input = sys.stdin.readline

T = int(input())
q = []

for i in range(T):
    num = int(input())
    if num != 0:
        heapq.heappush(q, (abs(num), num))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])