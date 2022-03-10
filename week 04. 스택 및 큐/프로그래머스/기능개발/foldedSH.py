def solution(progresses, speeds):
    import math
    
    release_day =[math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    _max = release_day[0]
    answer = [1]; idx = 0
    for i in range(1, len(release_day)):
        if _max >= release_day[i]:
            answer[idx]+=1
        else:
            _max = release_day[i]
            answer.append(1)
            idx += 1

    return answer