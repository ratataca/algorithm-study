def bubble_sort(arr):
    for end in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                
        if not swapped:
            break


arr = [4, 3, 5, 1, 2]
bubble_sort(arr)
print(arr)