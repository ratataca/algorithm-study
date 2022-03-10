def solution(clothes):
    Dict = {}
    for i in clothes:
        if i[1] in Dict:
            Dict[i[1]] += 1
        else:
            Dict[i[1]] = 1
    a = Dict.values()
    
    answer = 1
    for i in a:
        answer *= i+1
    return answer-1