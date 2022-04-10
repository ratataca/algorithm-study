def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cur = 0
        remove = 0

        for rock in rocks:
            l_dist = rock - cur
            if l_dist < mid:
                remove += 1
            else:
                cur = rock

        if remove <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
