k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
result = 0

while start <= end:
    cnt = 0
    mid = (start+end)//2

    for one_lan in lan:
        cnt += one_lan//mid

    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)