def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def solution(n, computers):
	# 인접 행렬 -> 인접 리스트
    nodes = []
    for i in range(n):
        computer = computers[i]
        nodes.append([])
        for j in range(n):
            if i == j or computer[j] == 0:
                continue
            nodes[i].append(j)

    # 방문 기록        
    visited = [False] * n

    cnt = 1
    start = 0
    while True:
        dfs(nodes, start, visited) # 연결된 노드 check
        if sum(visited) == n:
            break

        start = visited.index(False)
        cnt += 1

    return cnt