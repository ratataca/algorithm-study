def solution(genres, plays):
    total_Dict = {}
    Dict = {}
    answer = []
    for i in range(len(genres)):
        if not genres[i] in total_Dict:
            total_Dict[genres[i]]= plays[i]
            Dict[genres[i]] = [(plays[i],i)] 
        else:
            total_Dict[genres[i]] += plays[i]
            Dict[genres[i]].append((plays[i],i))

    for i in range(len(Dict)):
        max_key = max(total_Dict,key=total_Dict.get)
        if max_key in Dict:
            answer.append(Dict[max_key].pop(Dict[max_key].index(max(Dict[max_key], key=lambda x: (x[0],-x[1]))))[1])
        if Dict[max_key] != []:
            if max_key in Dict:
                answer.append(Dict[max_key].pop(Dict[max_key].index(max(Dict[max_key], key=lambda x: (x[0],-x[1]))))[1])
        del total_Dict[max_key]
        del Dict[max_key]

    
    return answer