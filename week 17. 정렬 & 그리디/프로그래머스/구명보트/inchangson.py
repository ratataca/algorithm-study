def solution(people, limit):
    answer = 0
    
    people.sort()
    
    ptr_start = 0
    ptr_end = len(people) - 1
    
    cnt = 0
    while ptr_start <= ptr_end:
        if people[ptr_start] + people[ptr_end] <= limit:
            cnt += 1
            ptr_start += 1
            ptr_end -= 1
        else:
            cnt += 1
            ptr_end -= 1
    
    answer = cnt
    
    return answer