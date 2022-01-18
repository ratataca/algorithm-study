def makeNumber(curIdx, curNum, numbers, target):
    ret = 0
    if curIdx == len(numbers):
        if curNum == target:
            ret = 1
        return ret
    
    ret += makeNumber(curIdx + 1, curNum + numbers[curIdx], numbers, target)
    ret += makeNumber(curIdx + 1, curNum - numbers[curIdx], numbers, target)
    return ret

def solution(numbers, target):
    answer = makeNumber(0, 0, numbers, target)
    return answer