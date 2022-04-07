def solution(n, times):
    answer = 0
    
    l = 0
    h = 1e18
    
    def get_complete_no(offered: int):
        cnt = 0
        for time in times:
            cnt += offered // time
        return cnt
    
    while l <= h:
        m = (l + h)//2
        complete_no = get_complete_no(m)
        if complete_no < n:
            l = m + 1
        else:
            h = m - 1
            answer = m

    return answer