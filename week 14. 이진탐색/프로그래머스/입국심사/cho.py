def solution(n, times):
    start, end = 1, max(times) * n
    result = 1e18
    while start <= end:
        mid = (start + end) // 2

        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            result = min(result, mid)
            end = mid - 1

        else:
            start = mid + 1

    return result
