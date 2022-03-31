from collections import deque


def show(matrix):
    print("-" * 30)
    for i in matrix:
        for j in i:
            print("{0:<5}".format(j), end=" ")
        print()


def solution(board):
    show(board)
    dx = [-1, 1, 0, 0]  # 왼 오 위 아래
    dy = [0, 0, -1, 1]
    length = len(board)
    costMap = [[0 for _ in range(length)] for _ in range(length)]
    costMap[0][0] = 100
    queue = deque()
    queue.append((0, 0, 0, 0))

    while queue:

        x, y, cost, cur_dir = queue.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length or board[ny][nx] == 1:
                continue

            if x == 0 and y == 0:
                new_cost = cost + 100
            else:
                if cur_dir == i:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600

            if costMap[ny][nx] == 0:
                costMap[ny][nx] = new_cost
                queue.append((nx, ny, new_cost, i))
            else:
                if costMap[ny][nx] >= new_cost:
                    costMap[ny][nx] = new_cost
                    queue.append((nx, ny, new_cost, i))
    show(costMap)
    return costMap[-1][-1]


solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
