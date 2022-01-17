def solution(participant, completion):
    p_dict = {}
    for name in participant: # 참가자 dictionary 생성
        if p_dict.get(name):
            p_dict[name] += 1
        else:
            p_dict[name] = 1
          
  
    for _fin in completion: # 완주자 체크
        p_dict[_fin] -= 1
    
		# 미완주자
    idx = list(p_dict.values()).index(1)
    answer = list(p_dict.keys())[idx]

    return answer