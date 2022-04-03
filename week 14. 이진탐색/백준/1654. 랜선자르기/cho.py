k, n = map(int, input().split())

List = [int(input()) for _ in range(k)]

start = 1
end = max(List)
result = 0

while start <= end:
    mid = (end + start) // 2

    cnt = 0
    for ele in List:
        cnt += ele // mid

    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
