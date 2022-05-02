def solution(routes):
    answer = 1
    
    routes.sort(reverse=True)
    camera = max([row[0] for row in routes])
    for car in routes:
        if car[1] < camera:
            camera = car[0]
            answer+=1
    return answer