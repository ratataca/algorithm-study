#import sys
#input = sys.stdin.readline


a = input()

N, D = map(int, input().split())

shortcut_list = [map(int, input().split()) for _ in range(N)]

print(shortcut_list)

def go_school(cur_pos):
    ret = D - cur_pos
    for shortcut in shortcut_list:
        begin, end, dist = shortcut
        if begin < cur_pos:
            continue
        cand = (begin - cur_pos) + go_school(end)
        ret = max(ret, cand)
    return ret

print(go_school(0))