import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        cnt += 1
        if len(scoville) == 1 and a + b * 2 < K:
            return -1
    
    return cnt