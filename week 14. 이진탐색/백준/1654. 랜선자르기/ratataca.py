N, K = [int(n) for n in input().split()]
lines = [int(input()) for _ in range(N)]

min_line = 1
max_line = int(sum(lines) / len(lines))


def can_split(I):
    result = 0
    for line in lines:
        result += (line // I)
    return result

while min_line <= max_line:
    mid = (min_line + max_line) // 2

    if can_split(mid) >= K:
        min_line = mid + 1

    else:
        max_line = mid - 1

print(max_line)