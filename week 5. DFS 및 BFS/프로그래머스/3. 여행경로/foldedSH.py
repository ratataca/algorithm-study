from collections import defaultdict

def solution(tickets):
    answer = []
    
    nodes = defaultdict(list)
    n = len(tickets)

    # 그래프 초기화
    for i in range(n):
        node = tickets[i][0]
        linked_node = tickets[i][1]
        nodes[node].append(linked_node)
        nodes[node].sort(reverse=True)
    
    start = ['ICN'] # 항상 "ICN" 공항에서 출발
    while len(answer) < (n+1):
        target = start[-1]
        print(target)

		# 해당 공항에서 출발하는 항공권이 없다면
        if nodes[target] == [] or target not in nodes:
            answer.append(start.pop())
        else:
            start.append(nodes[target].pop())
            
    return answer[::-1]