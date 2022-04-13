from collections import deque, defaultdict, Counter

def show(arrs):
    for arr in arrs:
        for a in arr:
            print("\t", a, end="")
        print()
        
#  1번 노드에서 가장 멀리 떨어진 노드의 갯수
def solution(n, edge):
    visited = [0] * (n + 1)
    graph = [[] for i in range(n+1)]
    
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    q = deque()
    q.append(1)
    visited[1] = 1
            
    answer = []
    while q:
        cur_node = q.popleft()
        cnt = 0
        for idx in graph[cur_node]:
            if visited[idx] == 0:
                q.append(idx)
                visited[idx] = visited[cur_node] + 1
        
    answer = Counter(visited)
    return answer[max(answer.keys())]