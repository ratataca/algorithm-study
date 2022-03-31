def isCombinable(map, x_point, y_point, size):
    cur_char = map[y_point][x_point]
    for y in range(y_point, y_point + size):
        for x in range(x_point, x_point + size):
            if cur_char != map[y][x]:
                return False
    return True
            


def quad_tree(map, x_point, y_point, size):
    
    if isCombinable(map, x_point, y_point, size):
        print(map[y_point][x_point], end="")
        return 0
    
    half_size = size // 2
    print("(", end="")
    quad_tree(map, x_point, y_point, half_size)
    quad_tree(map, x_point + half_size, y_point, half_size)
    quad_tree(map, x_point, y_point + half_size, half_size)
    quad_tree(map, x_point + half_size, y_point + half_size, half_size)

    print(")", end="")
    return 0
    

# N × N 크기
N = int(input())
_map = []
for _ in range(N):
    _n = input()
    tmp = []
    for n in _n:
        tmp.append(n)
    _map.append(tmp)

quad_tree(_map, 0, 0, N)
