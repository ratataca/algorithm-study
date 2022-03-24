import heapq

n, d = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append((b, c))

for i in range(d):
    graph[i].append((i+1, 1))
    
    
start = 0
q = []

heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist+i[1]
        # if i[0]>d:
        #     continue
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[d])