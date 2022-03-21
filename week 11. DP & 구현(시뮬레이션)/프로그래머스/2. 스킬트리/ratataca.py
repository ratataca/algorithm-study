
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

target = "CBD"	
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(target, skill_trees))


# def solution(target, skill_trees):
#     answer = 0
    
#     for tree in skill_trees:
#         if target in tree:
#             cnt += 1
#             break
        
#         idx = 0
#         find_idx = []

#         for i in range(idx, len(tree)):
#             for j, t in enumerate(target):     
#                 if t == tree[i]:
#                     find_idx.append(j)    
#                     idx = i + 1
#                     break
                    
#         if find_idx == sorted(find_idx):
#             answer += 1
    
#     return answer


