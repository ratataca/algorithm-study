array = [1, 9, 4, 6, 11, 10, 3, 15, 2, 13]

for i in range(len(array)-1):
    min_idx = i
    for j in range(i, len(array)): # 최솟값 탐색
        if array[min_idx]>array[j]:
            min_idx = j
    
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)