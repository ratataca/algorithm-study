def solution(clothes):
    answer = 0
    spyItems = {}
    for c in clothes :
        if c[1] in spyItems :
            spyItems[c[1]] += 1
        else:
            spyItems[c[1]] = 2
    
    total = 1
    for v in spyItems.values() :
        total *= v
    answer = total - 1
    
    return answer