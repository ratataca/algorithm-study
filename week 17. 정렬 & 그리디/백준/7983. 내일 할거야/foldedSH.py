import sys

input = sys.stdin.readline
t = int(input())

works = []
for _ in range(t):
    works.append(list(map(int, input().split())))
works.sort(key=lambda x:x[1], reverse=True)

days = works[0][1]
for work in works:
    if days >= work[1]:
        days = work[1]-work[0]
    else:
        days -= work[0]
print(days)