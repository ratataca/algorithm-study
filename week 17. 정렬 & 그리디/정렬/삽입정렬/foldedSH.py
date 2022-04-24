array = [1, 9, 4, 6, 11, 10, 3, 15, 2, 13]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1]>array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            
print(array)