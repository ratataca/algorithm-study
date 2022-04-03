n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)
arr.sort()


def find_length(h):
    total = 0
    for i in arr:
        if i > h:
            total += i - h
    return total


result = 0
while start <= end:
    mid = (start + end) // 2
    if find_length(mid) < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
