import heapq

def solution(scoville, K):
    answer = 0
    compare = [K] * len(scoville)
    heapq.heapify(scoville)

    answer = 0
    while True:
        if len(scoville) < 2:
            return -1
        min_1st = heapq.heappop(scoville)
        min_2nd = heapq.heappop(scoville)

        heapq.heappush(scoville, min_1st+min_2nd*2)
        answer += 1

        if scoville >= compare:
            return answer