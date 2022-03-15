def solution(target, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        if target in tree:
            cnt += 1
            break
        
        idx = 0
        find_idx = []
        for t in target: 
            for i in range(idx, len(tree)):
                if t == tree[i]:
                    find_idx.append(i)    
                    idx = i + 1
                    break
                    
        if find_idx == sorted(find_idx):
            answer += 1
    
    return answer


target = "CBD"	
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(target, skill_trees))
