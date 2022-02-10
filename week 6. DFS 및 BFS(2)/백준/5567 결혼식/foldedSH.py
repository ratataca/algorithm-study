n = int(input())
m = int(input())
nodes = [[] for _ in range(n + 1)]

for _ in range(m):
	x, y = list(map(int, input().split()))
	nodes[y].append(x)
	nodes[x].append(y)

visited = [False]*(n+1)

visited[1] = True
for i in nodes[1]:
    visited[i] = True
    for j in nodes[i]:
        visited[j] = True

print(sum(visited)-1)