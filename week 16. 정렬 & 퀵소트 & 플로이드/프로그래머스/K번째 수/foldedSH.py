def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        idx1, idx2, k = commands[i]
        tmp_arr = array[(idx1-1):idx2]
        answer.append(sorted(tmp_arr)[k-1])
        
    return answer