def solution(n, costs):
    answer = 0
    INF = 987654321
    
    graph = []
    money = []
    visited = []
    pi = []
    key = []
    
    for _ in range(n):
        graph.append([])
        money.append([0] * n)
        visited.append(False)
        key.append(INF)
        pi.append(None)
        
    for cost in costs:
        graph[cost[0]].append(cost[1])
        graph[cost[1]].append(cost[0])
        money[cost[0]][cost[1]] = cost[2]
        money[cost[1]][cost[0]] = cost[2]
    
    s = 0
    key[s] = 0
    
    for _ in range(n - 1):
        cur_node = -1
        cur_cost = INF
        for node in range(n):
            if visited[node]:
                continue
                
            if key[node] < cur_cost:
                cur_node = node
                cur_cost = key[node]
        
        visited[cur_node] = True
        #
        for next_node in graph[cur_node]:
            next_cost = money[cur_node][next_node]
            if visited[next_node]:
                continue
                
            if key[next_node] > next_cost:
                key[next_node] = next_cost
                pi[next_node] = cur_node
    
    
    for i in range(n):
        if pi[i] != None:
            answer += money[i][pi[i]]
    
    return answer