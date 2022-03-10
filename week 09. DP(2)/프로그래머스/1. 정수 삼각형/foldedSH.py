def solution(triangle):
    answer = 0
    results = [[0]*len(row) for row in triangle]
    results[0] = triangle[0]
    
    for y in range(1, len(triangle)):
        end_x = len(triangle[y])
        for x in range(end_x):
            if x == 0: # 삼각형 가장자리(왼쪽)
                results[y][x] = results[y-1][x] + triangle[y][x]
            elif x == (end_x-1): # 삼각형 가장자리(오른쪽)
                results[y][x] = results[y-1][x-1] + triangle[y][x]
            else: # 삼각형 내부
                results[y][x] = max(results[y-1][x-1] + triangle[y][x], 
																					results[y-1][x] + triangle[y][x])
            if answer < results[y][x]: # 최대값
                answer = results[y][x]

    return answer