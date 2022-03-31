import heapq
import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num:
        heapq.heappush(array, (abs(num), num))
    elif array == []:
        print(0)
    else:
        p_num = heapq.heappop(array)
        print(p_num[1])