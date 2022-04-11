from collections import deque

MX = 987654321
def solution(n, edge):
    answer = 0
    
    m = n + 1
    
    dist = [MX] * m
    
    graph = [[] for _ in range(m)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    q = deque()
    
    q.append((1, 0))
    dist[1] = 0
    
    mx_dist = 0
    while q:
        cur_node, cur_dist = q.popleft()
        mx_dist = cur_dist
        
        next_dist = cur_dist + 1
        for next_node in graph[cur_node]:
            if dist[next_node] != MX:
                continue
                
            dist[next_node] = next_dist
            q.append((next_node, next_dist))
        
    for d in dist:
        answer += int(d == mx_dist)
    
    return answer