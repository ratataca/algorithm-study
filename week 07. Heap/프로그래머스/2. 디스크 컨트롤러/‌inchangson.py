from heapq import *

class task:
    def __init__(self, request, process):
        self.request = request
        self.process = process
    def __lt__(self, other):#less than
        return self.process < other.process

def solution(jobs):
    answer = 0
    total = 0
    cur_time = 0
    completed = 0
    idx = 0
    jobs.sort()
    scheduler = []
    #print(jobs)
    while completed < len(jobs):
        if idx < len(jobs):
            if jobs[idx][0] > cur_time and len(scheduler) == 0:
                cur_time = jobs[idx][0]
                continue
            while idx < len(jobs) and jobs[idx][0] <= cur_time:
                #print('cur_time', cur_time, idx)
                heappush(scheduler, task(jobs[idx][0], jobs[idx][1]))
                idx += 1
        
        cur_task = heappop(scheduler)
        #print(cur_time, cur_task.request, cur_task.process)
        total += cur_time - cur_task.request + cur_task.process
        cur_time += cur_task.process
        completed += 1
        
        
    return total // len(jobs)