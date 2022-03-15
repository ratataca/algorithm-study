def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        for i in range(len(tree)):
            alp = tree[i]
            idx = skill.find(alp)
            
            # 가능한 경우
            if idx == -1 or len(set(skill[:idx]) - set(tree[:i]))==0: 
                pass
            else:
                break
        else:
            answer+=1
                    
    return answer