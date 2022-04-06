def measure_the_distance(rocks, target):
    remove = 0
    prev_rock = 0

    gap = int(1e9) 
    for rock in rocks:
        cur_gap = rock - prev_rock
        if cur_gap < target:
            remove += 1
        else:
            gap = min(gap, cur_gap) 
        prev_rock = rock
    return [remove, gap]
    

def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    min_value = 0
    max_value = distance
    
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        
        remove, gap = measure_the_distance(rocks, mid)
        if remove >= n:
            answer = gap
            max_value = mid - 1
        else:
            answer = gap
            min_value = mid + 1    
    
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]	
n = 2

print(solution(distance, rocks, n))