from collections import deque

def solution(number, k):
    answer = ''
    cnt = 0
    tmp = []
    
    idx = 0
    
    while idx < len(number):
        top = tmp[-1] if tmp else '9'
        
        if cnt < k and top < number[idx]:
            tmp.pop()
            cnt += 1
        else:
            tmp.append(number[idx])
            idx += 1
            
    answer = ''.join(tmp[:len(number) - k])
    return answer