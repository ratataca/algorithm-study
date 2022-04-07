def bin_search(array, target, start, end):
    if start > end:
        return

    mid = (start+end)//2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return bin_search(array, target, start, mid - 1)

    else:
        return bin_search(array, target, mid + 1, end)
    
n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for num in m_list:
    result = bin_search(n_list, num, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)
 