def solution(triangle):
    deep = len(triangle)
    map = [[0 for _ in range(n)] for n in range(1, deep + 1)]
    
    for y in range(len(map)):
        for x in range(len(map[y])):
            if y == 0 and x == 0:
                num = triangle[y][x]
                map[0][0] = num
            else:
                num = map[y][x]
        
            try:
                if (triangle[y+1][x] + num) > map[y+1][x]:
                    map[y+1][x] = triangle[y+1][x] + num

                if (triangle[y+1][x+1] + num) > map[y+1][x+1]:
                    map[y+1][x+1] = triangle[y+1][x+1] + num
            except:
                pass            
    
    return max(map[-1])