def solution(people, limit):
    people.sort()
    right = len(people) - 1
    left = 0
    
    visited = [0] * len(people)
    cnt = 0
    while left < right:
        if people[left] + people[right] <= limit:
            visited[left] = 1
            visited[right] = 1
            left += 1
            right -= 1
            cnt += 1

        else:        
            if limit - people[left] > limit - people[right]:
                visited[right] = 1
                right -= 1
                cnt += 1
            else:
                visited[left] = 1
                left += 1
                cnt += 1
    return cnt