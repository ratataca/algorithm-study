from collections import defaultdict, Counter

def show(arrs):
    for arr in arrs:
        for a in arr:
            print("\t", a, end="")
        print()
        
        
def solution(n, results):
    ranking = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, loss in results:
        ranking[win][loss] = 1
        ranking[loss][win]  = -1
    
    # show(ranking)
    
    for k in range(1, n + 1):                  
        for i in range(1, n + 1):              
            for j in range(1, n + 1):          
                if ranking[i][j] == 0:   
                    if ranking[i][k] == 1 and ranking[k][j] == 1:
                        ranking[i][j] = 1
                    elif ranking[i][k] == -1 and ranking[k][j] == -1:
                        ranking[i][j] = -1
    # print("="*60)
    # show(ranking)
    # 각 노드 점수판에 0이 하나(다른 노드들에 대해 승패가 모두 결정됨)인 경우만 셈
    answer = 0
    for i in range(n+1):
        if Counter(ranking[i])[0] == 2:
            answer += 1

    return answer