def solution() :
    #input
    n1, n2 = map(int, input().split())
    g1 = input()[::-1]
    g2 = input()
    sec = int(input())
    
    #solve
    if sec < n1 :
        i1 = n1 - 1 - sec
        i2 = 0
        rslt = g1[:i1]
    else :
        i1 = 0
        i2 = sec - n1 + 1
        rslt = g2[:i2]
    
    cond1 = cond2 = True
    while cond1 or cond2 :
        cond1 = i1 < n1
        cond2 = i2 < n2
        if cond1 and cond2 :
            rslt += g1[i1] + g2[i2]
            i1 += 1
            i2 += 1
            continue
        if cond1 :
            rslt += g1[i1:]
        if cond2 :
            rslt += g2[i2:]
        break
    print(rslt)
solution()