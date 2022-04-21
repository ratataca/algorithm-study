def solution(citations):
    answer = 0
    
    citations.sort()
    
    n = len(citations)
    idx = 0
    
    h = 0
    max_c = max(citations)
    while h <= max_c:
        over_h  = n - idx
        if over_h >= h:
            answer = h
        
        if idx < n and citations[idx] <= h:
            idx += 1
        else:
            h += 1
        
    return answer