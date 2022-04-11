def countLose(cur, checked, n, relation):
    #print(checked, 'l')
    ret = 0    
    for post in range(n):
        if checked[post]:
            continue
        if relation[cur][post] == -1:
            checked[post] = True
            ret += countLose(post, checked, n, relation) + 1
            #checked[post] = False

    #print('lose', cur, ret)
    
    return ret

def countWin(cur, checked, n, relation):
    ret = 0    
    for post in range(n):
        if checked[post]:
            continue
        if relation[cur][post] == 1:
            checked[post] = True
            ret += countWin(post, checked, n, relation) + 1
            #checked[post] = False
    
    #print('win', cur, ret)
    return ret


def solution(m, results):
    answer = 0
    n = m + 1
    relation = [[0 for i in range(n)] for j in range(n)] 
    
    for w, l in results:
        relation[w][l] = 1
        relation[l][w] = -1
        
    for player in range(n):
        
        checked = [False] * n
        checked[player] = True
        loseCnt = countLose(player, checked, n, relation)
        
        checked = [False] * n
        checked[player] = True
        winCnt = countWin(player, checked, n, relation)

        #print(player, loseCnt, winCnt)
        if loseCnt + winCnt + 1 == m:
            answer += 1
            
    return answer