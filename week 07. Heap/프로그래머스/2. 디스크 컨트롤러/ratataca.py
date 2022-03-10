import heapq

def solution(jobs):
    minHeap = []
    time, cnt = 0, 0
    start = -1
    result = 0
    
    jobs = sorted(jobs)
    
    len_jobs = len(jobs)
    

    while cnt < len_jobs:
        # 지금 시간 보다 작은 job를 heapq 넣기
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(minHeap, [job[1], job[0]])

        # 최신에 대한 1개에 대한 연산진행
        if len(minHeap) > 0:
            # 연산 끝난거 heapq 제거
            cur = heapq.heappop(minHeap)
            start = time
            time += cur[0]  # run_time
            result += time - cur[1]
            cnt += 1
        else:
            time += 1
        
    
    return result // len_jobs