array = [1, 9, 4, 6, 11, 10, 3, 15, 2, 13]

for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j]>array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)