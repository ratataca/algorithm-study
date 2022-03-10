def getCompleteDay(left, speed):
    if left % speed:
        return left//speed + 1
    return left//speed

def solution(progresses, speeds):
    answer = [1]
    releaseDay = getCompleteDay(100 - progresses[0], speeds[0])
    for idx in range(1, len(progresses)):
        completeDay = getCompleteDay(100 - progresses[idx], speeds[idx])
        if releaseDay < completeDay:
            answer.append(1)
            releaseDay = completeDay
        else:
            answer[-1] += 1
    
    return answer