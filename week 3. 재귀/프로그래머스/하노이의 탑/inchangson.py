def makeTower(cur, dest, cnt):
    if cnt == 1:
        answer.append([cur, dest])
        return
    
    stopover = 6 - cur - dest
    
    makeTower(cur, stopover, cnt - 1)
    makeTower(cur, dest, 1)
    makeTower(stopover, dest, cnt - 1)

def solution(n):
    global answer
    answer = []
    makeTower(1, 3, n)
    return answer