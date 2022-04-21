import heapq

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i < citations[i]:
            answer += 1
        
    return answer