import sys
input = sys.stdin.readline

_ = int(input())

arr = list(map(int, input().split()))
arr.sort()

_ = int(input())

targets = list(map(int, input().split()))

def find_k(k):
    l = 0;
    h = len(arr) - 1

    while l <= h:
        m = (l+h)//2
        if k == arr[m]:
            return 1
        elif k < arr[m]:
            h = m - 1
        else:
            l = m + 1
    return 0

for k in targets:
    if find_k(k):
        print(1)
    else:
        print(0)