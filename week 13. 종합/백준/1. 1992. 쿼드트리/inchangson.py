# 11286
import sys
input = sys.stdin.readline

n = int(input())

# 숫자 아니다
board = [input() for _ in range(n)]

def solve(r, c, sz):
    if sz == 1:
        return board[r][c]
    sub_sz = sz // 2
    v1 = solve(r, c, sub_sz)
    v2 = solve(r, c + sub_sz, sub_sz)
    v3 = solve(r + sub_sz, c, sub_sz)
    v4 = solve(r + sub_sz, c + sub_sz, sub_sz)

    ret = (v1+v2+v3+v4)
    if ret == "1111":
        return "1"
    elif ret == "0000":
        return "0"
    else:
        return "(" + ret + ")"
    

print(solve(0, 0, n))