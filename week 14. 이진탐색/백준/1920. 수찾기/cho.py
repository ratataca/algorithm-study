# 이진탐색 풀이
n = int(input())

n_arr = list(map(int, input().split()))
length = n

m = int(input())

m_arr = list(map(int, input().split()))

n_arr.sort()


def b_search(a):
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2

        if n_arr[mid] == a:
            return True
        elif n_arr[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    return False


for ele in m_arr:
    if b_search(ele):
        print(1)
    else:
        print(0)


# 좀 더 많이 쉬운 풀이
n = int(input())

n_arr = set(map(int, input().split()))

m = int(input())

m_arr = list(map(int, input().split()))
for i in m_arr:
    if i in n_arr:
        print(1)
    else:
        print(0)
