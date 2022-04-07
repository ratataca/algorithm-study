# boj 1654

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

def is_enough(mid):
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt >= n:
        return True
    else:
        return False
 
high = max(lines)
low = 1
ans = high
while low <= high:
    mid = (low+high)//2
    if is_enough(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1
print(ans)