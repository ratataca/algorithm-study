def isTimeOk(mid, times):
    count = 0
    for time in times:
        count += (mid // time)
    return count
    

def solution(n, times):
    min_value = 1
    max_value = max(times) * n
    
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        
        if isTimeOk(mid, times) >= n:
            answer = mid
            max_value = mid - 1
        else:   
            min_value = mid + 1
            
    return answer

solution(6, [7, 10])