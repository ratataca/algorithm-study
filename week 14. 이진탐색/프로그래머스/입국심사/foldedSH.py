def solution(n, times):
    start, end = 1, max(times)*n
    result = 0

    while start <= end:
        cnt = 0
        mid = (start+end)//2

        for _time in times:
            # mid 분 간 통과한 사람 수
            cnt += mid//_time

        if cnt >= n: # 충분히 통과 가능하다면 end를 조정
            result = mid
            end = mid - 1
        else: # 통과 불가능 시, start 조정
            start = mid + 1

    return result