def solution(distance, rocks, n):
    answer = -1
    rocks.append(0)
    rocks.append(distance)

    
    rocks.sort()
    #print(rocks)
    def get_removed_cnt(stride: int):
        #print("get_removed_cnt(stride %d)=============" % (stride))
        cnt = 0
        pre = rocks[0]
        for i in range(1, len(rocks)):
            cur = rocks[i]
            
            if cur - pre < stride:
                #print("pre %d cur %d" % (pre, cur))
                cnt += 1
            else:
                pre = cur
        #print("="*10)
        return cnt
    
    l = 0
    h = distance
    
    while l <= h:
        m = (l + h)//2
        
        tmp = get_removed_cnt(m)
        #print("l %d m %d h %d => tmp %d" % (l, m, h, tmp))
        if tmp > n:
            h = m - 1
        elif tmp <= n:
            l = m + 1
            answer = m
            
    return answer