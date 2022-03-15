def solution(skill, skill_trees):
    Dict = dict()
    for i in range(len(skill)):
        Dict[skill[i]] = i+1

    cnt = 0
    for skill_tree in skill_trees:
        tmp = 0
        for ele in skill_tree:
            if ele in skill:
                if Dict[ele] != tmp+1:
                    break
                else:
                    tmp = Dict[ele]
        else:
            cnt += 1
    return cnt
