def solution(routes):
    routes.sort(key = lambda x : x[1])
    
    camera_cnt = 0
    camera = -30000 - 1    
    for car in range(len(routes)):
        if routes[car][0] > camera:
            camera = routes[car][1]
            camera_cnt += 1
    
    answer = camera_cnt
    return answer