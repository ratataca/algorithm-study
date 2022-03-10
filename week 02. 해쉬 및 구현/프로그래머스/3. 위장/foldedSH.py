from itertools import combinations 

def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    for val, key in clothes:
        if clothes_dict.get(key):
            clothes_dict[key].append(val)
        else:
            clothes_dict[key] = [val]
    
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key])+1
    answer -= 1
    
    return answer