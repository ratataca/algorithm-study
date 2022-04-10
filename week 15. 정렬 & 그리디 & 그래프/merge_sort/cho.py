from collections import deque

arr = [21, 10, 12, 20, 25, 13, 15, 22]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())

    while len(left) > 0:
        result.append(left.popleft())

    while len(right) > 0:
        result.append(right.popleft())

    return result


print(merge_sort(arr))
