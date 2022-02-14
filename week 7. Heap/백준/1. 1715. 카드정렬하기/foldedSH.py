import sys
import heapq

n = int(input())
cards = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    heapq.heappush(cards, num)

total = []
while len(cards) != 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    num = num1+num2
    total.append(num)
    heapq.heappush(cards, num)
    
print(sum(total))