# BFS 
# 인접 리스트를 활용.
from collections import deque
from collections import defaultdict

def bfs(q, rd, visited, cnt):
    while q:
        node, depth = q.popleft()
        
        for n in rd[node]:
            if visited[n] == False and depth < 2:
                q.append([n, depth + 1])
                visited[n] = True
                cnt += 1
    return cnt

N = int(input())
M = int(input())
relation = []

for _ in range(M):
    relation.append([int(n) for n in input().split()])

cnt = 0
rd = defaultdict(list)
for r1, r2 in relation:
    rd[r1].append(r2)  
    rd[r2].append(r1)

visited = [False] * (len(rd) + 1)

# Definition of Queue
q = deque([])
visited[1] = True
for n in rd[1]:
    q.append([n, 1])
    visited[n] = True
    cnt += 1

if not q:
    print(0)
else: 
    print(bfs(q, rd, visited, cnt))