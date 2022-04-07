def cut_wood(arr, k):
    result = 0
    for w in arr:
        if w > k:
            result = result + (w - k)
    return result

def binary_sort(arr, M):
    min_value = 0
    max_value = max(arr)
    
    while min_value <= max_value:
        mid = (min_value + max_value) // 2

        result = cut_wood(arr, mid)
        if result >= M:
            min_value = mid + 1
        
        elif result < M:
            max_value = mid - 1

    return max_value


N, M = [int(n) for n in input().split()]
arr = [int(n) for n in input().split()]

print(binary_sort(arr, M))
