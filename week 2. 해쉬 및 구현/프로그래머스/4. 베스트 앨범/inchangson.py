def getTopTwo(args):
    if len(args) == 1 :
        return [args[0][1]]
    else :
        ret1 = ret2 = (-1, 0)
        #ret2 = (-1, 0)
        for cnt, no in args :
            if ret1[0] < cnt :
                ret2 = ret1
                ret1 = (cnt, no)
            elif ret2[0] < cnt :
                ret2 = (cnt, no)
        return [ret1[1], ret2[1]]

def genreCmp(tList):
    total = 0
    for t in tList[1] :
        total += t[0]
    return total

def solution(genres, plays):
    answer = []
    playList = {}
    
    for i in range(len(genres)) :
        if genres[i] in playList :
            playList[genres[i]].append((plays[i], i))
        else :
            playList[genres[i]] = [(plays[i], i)]
    
    playList = {k: v for k, v in sorted(playList.items(), key = genreCmp, reverse = True)}
    
    for genre in playList.values() :
        answer += getTopTwo(genre)
    
    print(playList)
    
    
    return answer