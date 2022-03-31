from collections import deque

def solution(board):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(graph, dir):
        price = [[int(1e9)]*len(graph) for _ in range(len(graph))] # 지점별 최소비용

        queue = deque()
        queue.append((0, 0, 0, dir)) # 좌표와 비용, 방향

        while queue:
            x, y, money, direct = queue.popleft() # 현재 좌표, 현재 비용, 진행 방향

            if (x, y) == (len(graph)-1, len(graph)-1): # 마지막 좌표 = stop
                continue

						# 상하좌우 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 밖 or 벽
                if (nx < 0 or nx >= len(graph) or 
                    ny < 0 or ny >= len(graph) or graph[nx][ny] == 1):
                    continue

                if i == direct: # 같은 방향 - 직선
                    cur_money = money + 100

                else: # 다른 방향 - 커브
                    cur_money = money + 600

                if cur_money < price[nx][ny]: # 새로운 경우 vs 이전 경우
                    price[nx][ny] = cur_money
                    queue.append((nx, ny, cur_money, i))

        return price[-1][-1]

    answer = min(bfs(board, 1), bfs(board, 3)) # 아래 vs 오른쪽
    return answer