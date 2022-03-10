from collections import deque

CHANGEABLE = 1
VISITED = 2


def isChange(word, target):
    cnt = 0
    for w, t in zip(word, target):
        if w != t:
            cnt += 1

    if cnt == 1:
        return True
    return False


def bfs(words, target, map, q):
    while q:
        idx, cnt = q.popleft()

        # 종료 조건
        if words[idx] == target:
            return cnt

        for i, value in enumerate(map[idx]):
            if map[idx][i] == CHANGEABLE:
                q.append([i, cnt + 1])
                map[value][idx] = VISITED
                map[idx][value] = VISITED

    return cnt


def solution(begin, target, words):
    answer = 0

    # words 안에 target이 없는 경우
    if target not in words:
        return 0

    words = [begin] + words

    # 인접행렬 만들기
    map = array = [[0] * len(words) for _ in range(len(words))]

    for y, w1 in enumerate(words):
        for x, w2 in enumerate(words):
            if y != x and isChange(w1, w2):
                map[y][x] = 1

    # Definition of Queue
    q = deque([])
    for idx, value in enumerate(map[0]):
        if value == CHANGEABLE:
            q.append([0, 0])

    answer = bfs(words, target, map, q)
    return answer