def test(place, i, j):
    one_distance = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for a in one_distance:
        if 0 <= (i + a[0]) < 5 and 0 <= (j + a[1]) < 5:
            if place[i + a[0]][j + a[1]] == 'P':
                return False

    two_distance = [[-2, 0], [2, 0], [0, -2], [0, 2]]
    for a in two_distance:
        if 0 <= (i + a[0]) < 5 and 0 <= (j + a[1]) < 5:
            if place[i + a[0]][j + a[1]] == 'P':
                if place[int((i + i + a[0])/2)][int((j + j + a[1])/2)] == 'O':
                    return False

    cross_distance = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    for a in cross_distance:
        if 0 <= (i + a[0]) < 5 and 0 <= (j + a[1]) < 5:
            if place[i + a[0]][j + a[1]] == 'P':
                if not (place[i+a[0]][j] == 'X' and place[i][j+a[1]] == 'X'):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        result = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result = test(place, i, j)
                if not result:
                    break
            if not result:
                break

        if result:
            answer.append(1)
        else:
            answer.append(0)
    return answer
