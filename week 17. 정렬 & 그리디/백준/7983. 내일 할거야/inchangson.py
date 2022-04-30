import sys
input = sys.stdin.readline
n = int(input())
works = []
for _ in range(n):
    di, ti = map(int, input().split())
    works.append((di, ti))
works.sort(key = lambda x : x[1], reverse = True)

today = int(1e9)
for work in works:
    if work[1] < today:
        today = work[1]
    today -= work[0]
print(today)