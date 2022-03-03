def solution(triangle):
    deep = len(triangle)
    memo = [[0 for _ in range(n)] for n in range(1, deep + 1)]
    
    for y in range(len(memo)):
        for x in range(len(memo[y])):
            if y == 0 and x == 0:
                num = triangle[y][x]
                memo[0][0] = num
            else:
                num = memo[y][x]
        
            try:
                if (triangle[y+1][x] + num) > memo[y+1][x]:
                    memo[y+1][x] = triangle[y+1][x] + num

                if (triangle[y+1][x+1] + num) > memo[y+1][x+1]:
                    memo[y+1][x+1] = triangle[y+1][x+1] + num
            except:
                pass            
    
    return max(memo[-1])