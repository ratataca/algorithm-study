import sys
input = sys.stdin.readline

N, goal = map(int, input().split())
graph = [[] for _ in range(10001)]

for _ in range(N):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

distance = [i for i in range(goal+1)]

for i in range(goal+1):
    if  i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)

    for e, w in graph[i]:
        if e <= goal and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]

print(distance[goal])