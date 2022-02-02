def solution(n, computers):
    List = [[]] * len(computers)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j :
                if not List[i]:
                    List[i] = [j]
                else:
                    List[i].append(j)
    cnt = 0
    visited = []
    for i in range(n):
        if i not in visited:
            cnt+=1
            need_visit = []
            need_visit.append(i)
            while need_visit:
                node = need_visit.pop(0)
                if node not in visited:
                    visited.append(node)
                    need_visit.extend(List[node]) 
                
    return cnt
