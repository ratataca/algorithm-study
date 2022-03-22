import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcut_list = [list(map(int, input().split())) for _ in range(N)]

def go_school(cur_pos):
    ret = D - cur_pos
    for shortcut in shortcut_list:
        begin, end, dist = shortcut
        if begin < cur_pos:
            continue
        if end <= D:
            cand = (begin - cur_pos) + dist + go_school(end)
            ret = min(ret, cand)
    return ret
    
print(go_school(0))