def solution(people, limit):
    people.sort()

    cnt = 0
    i, j = 0, len(people)-1
    while i<=j:
        if people[i]+people[j] <= limit:
            i+=1
        cnt+=1
        j-=1
    return cnt