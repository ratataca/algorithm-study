def solution(m, n, puddles):
    PUDDLE = -1
        
    ### 전처리
    # MAP 만들기
    map = [[0 for _ in range(m + 1)] for col in range(n + 1)]
            
    # 웅덩이
    for x, y in puddles:
        map[y][x] = PUDDLE
    
    
    # x축 웅덩이 전까지
    for x in range(1, m + 1):
        if map[1][x] == PUDDLE:
            break
        map[1][x] = 1
        
    # y축 웅덩이 전까지
    for y in range(1, n + 1):
        if map[y][1] == PUDDLE:
            break
        map[y][1] = 1
        
    ### 계산
    for y in range(2, n + 1):
        for x in range(2, m + 1):
            # 웅덩이인 경우
            if map[y][x] == PUDDLE:
                continue
            
            if map[y][x - 1] == PUDDLE:
                map[y][x] = map[y - 1][x]
            elif map[y - 1][x] == PUDDLE:
                map[y][x] = map[y][x - 1]
            else:
                map[y][x] = map[y][x - 1] + map[y - 1][x]
    
    return map[n][m] %  1000000007