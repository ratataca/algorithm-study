import heapq

def solution(scoville, K):
    minHeap = scoville
    heapq.heapify(minHeap)
    
    mixing_cnt = 0
    
    while True:
        min1 = heapq.heappop(minHeap)

        if min1 >= K:
            break

        min2 = heapq.heappop(minHeap)
        mixing_food = min1 + min2 * 2
        heapq.heappush(minHeap, mixing_food)

        mixing_cnt += 1
        
        if len(minHeap) == 1 and mixing_food < K:
            return -1

    return mixing_cnt