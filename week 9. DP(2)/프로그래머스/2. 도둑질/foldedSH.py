def solution(money):
    n = len(money)
    case1 = [0]*n
    case2 = [0]*n

    # 1번집 도둑질
    case1[0] = money[0]
    case1[1] = max(case1[0], money[1])
    for i in range(2, n-1): # 마지막집은 도둑질 불가능 - 1번집과 인접
        case1[i] = max(case1[i-1], case1[i-2]+money[i])

    # n번집 도둑질
    case2[1] = max(case2[0], money[1])
    for i in range(2, n):
        case2[i] = max(case2[i-1], case2[i-2]+money[i])

    answer = max(case1[n-2], case2[n-1])
    
    return answer