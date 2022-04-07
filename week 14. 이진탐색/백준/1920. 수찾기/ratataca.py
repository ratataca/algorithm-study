# arr1 안에 arr2의 숫자가 있나
N1 = int(input())
arr = [int(n) for n in input().split()]

N2 = int(input())
targets = [int(n) for n in input().split()]


def find_num(arr, n):
    min_num, max_num = 0, len(arr) - 1

    while min_num <= max_num:
        mid = (min_num + max_num) // 2

        if n > arr[mid]:
            min_num = mid + 1            
        elif n < arr[mid]:
            max_num = mid - 1         
        else:
            return 1
    
    return 0

arr = sorted(arr)
for target in targets:
    print(find_num(arr, target))