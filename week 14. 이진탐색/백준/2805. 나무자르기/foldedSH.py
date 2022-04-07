import sys

n, m = map(int, sys.stdin.readline().split())
tree_h = list(map(int, sys.stdin.readline().split()))

start_h = 0
end_h = max(tree_h)

result = 0
while start_h <= end_h:
    total = 0
    mid = (start_h+end_h)//2
    total = sum(h-mid if h > mid else 0 for h in tree_h)
    if total < m:
        end_h = mid - 1
    else:
        result = mid
        start_h = mid + 1
print(result)