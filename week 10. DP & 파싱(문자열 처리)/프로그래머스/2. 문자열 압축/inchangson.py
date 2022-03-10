import sys
sys.setrecursionlimit(10**6)
def get_length(idx, unit, target):
    #print('1', idx, unit)
    if (idx + unit) > len(target):
        return len(target) - idx

    cnt = 0
    ref = target[idx:idx+unit]
    #print('loopstart', ref)
    while target[idx:idx+unit] == ref:
        #print(target[idx:idx+unit], ref)
        idx += unit
        cnt += 1

    ans = len(str(cnt)) if cnt > 1 else 0
    ans += unit + get_length(idx, unit, target)
    #print(idx, unit, ans, len(target))
    return ans

def solution(s):
    answer = len(s)
    target = s
    
    for leng in range(1, len(s)//2 + 1):
        #print('='*10)
        tmp = get_length(0, leng, target)
        if tmp < answer:
            answer = tmp
        #print('='*10)

    return answer