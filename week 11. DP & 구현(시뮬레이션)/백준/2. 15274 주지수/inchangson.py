import sys

def init_presum(presum):
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            presum[y][x] += presum[y - 1][x] + presum[y][x - 1] - presum[y-1][x-1]

            
def get_population(x1, y1, x2, y2):
    return presum[y2][x2] - presum[y1 - 1][x2] - presum[y2][x1 - 1] + presum[y1-1][x1-1]

n, m = map(int, sys.stdin.readline().split())
town = [[0]*(m+1)]
for _ in range(n):
    town.append([0] + list(map(int, sys.stdin.readline().split())))

presum = town
init_presum(presum)


k = int(input())
for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(get_population(x1, y1, x2, y2))