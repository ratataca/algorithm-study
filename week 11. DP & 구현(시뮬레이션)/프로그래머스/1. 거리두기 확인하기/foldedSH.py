from collections import deque

def bfs(graph, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[False]*5]*5

    queue = deque()
    queue.append((x, y, 0))
    
    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = True

        if cnt > 2: # 맨해튼 거리 2 이상이면 skip
            continue
        
        # 시작 노드가 아니면서 사람 있음 -> 안됨
        if cnt != 0 and graph[x][y] == "P" :
            return True

        # 거리 2가 아니면서 사람도 없음 -> 상하좌우
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 범위 밖 or 방문한 노드 or 파티션
            if (nx < 0 or nx >= 5 or ny < 0 or ny >= 5 
                or visited[nx][ny] or graph[nx][ny] == 'X'):
                continue

            queue.append((nx, ny, cnt+1))

def rules(graph):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == "P":
                if bfs(graph, i, j): # 사람 만나면
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if rules(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer