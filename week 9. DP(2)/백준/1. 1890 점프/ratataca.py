# N = int(input())
# map = [[int(n) for n in input().split()] for _ in range(N)]

N = 4
map = [[2, 3, 3, 1], [1, 2, 1, 3], [1, 2, 3, 1], [3, 1, 1, 0]]
# print(map)``

node = map[0][0]
cnt = 0

def search_next_node(x, y, cnt):
    if x >= N or y >= N:
            return 0

    if x == N - 1 and y == N - 1:
        cnt =+ 1
        return 1
    
    node = map[y][x]
    nx, ny = x + node, y + node 
    
    search_next_node(x, ny, cnt)    
    search_next_node(nx, y, cnt)

    return cnt



print(search_next_node(0, 0, cnt))
print(cnt)

"""
3개는 나오지만 글로벌 변수가 이를 해결하지 못하는 것 같음
"""