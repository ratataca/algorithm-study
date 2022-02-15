from heapq import *
def solution(scoville, K):
    answer = 0
    food_heap = scoville.copy()
    heapify(food_heap)
    
    food1 = heappop(food_heap)
    while food1 < K:
        if len(food_heap) == 0:
            return -1
        food2 = heappop(food_heap)
        new_food = food1 + 2*food2
        heappush(food_heap, new_food)
        food1 = heappop(food_heap)
        answer += 1
    
    print(scoville)
    return answer