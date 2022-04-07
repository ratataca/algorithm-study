# 2805
import sys
input = sys.stdin.readline

g_n, g_m = map(int, input().split())
trees = list(map(int, input().split()))

def get_total_leng(cut_height):
    global trees
    leng = 0
    for tree in trees:
        if tree < cut_height:
            continue
        leng += tree-cut_height
    return leng

def solve():
    l = 0
    h = 1000000000
    ret = -1
    
    while l <= h:
        m = (l+h)//2
        total = get_total_leng(m)

        if total < g_m:
            h = m - 1
        else:
            l = m + 1
            ret = m
            
    return ret

print(solve())