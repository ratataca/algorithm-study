def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])

    return pivot_sort(left) + [pivot] + pivot_sort(right)


arr = [21, 10, 10, 12, 20, 25, 26, 25, 13, 15, 22]

print(pivot_sort(arr))
