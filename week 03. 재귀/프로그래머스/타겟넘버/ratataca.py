cnt = 0

def target_num(i, total, number, target):
    global cnt

    if total == target and len(number) == i:
        cnt += 1
        return True

    if len(number) == i:
        return False

    target_num(i + 1, total + number[i], number, target)
    target_num(i + 1, total - number[i], number, target)


def solution(numbers, target):
    total_sum = 0
    target_num(0, total_sum, numbers, target)

    return cnt