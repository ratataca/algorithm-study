def solution(array, commands):
    answer = []
    
    for c in commands:
        tmp = array[c[0] - 1: c[1]]
        tmp.sort()        
        answer.append(tmp[c[2] - 1])
        
    return answer