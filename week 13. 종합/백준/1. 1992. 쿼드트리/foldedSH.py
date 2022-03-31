import sys
sys.setrecursionlimit(10**9)

n = int(input())

video = []
for _ in range(n):
    nums = list(map(int, list(input())))
    video.append(nums)
    
result = []
def zip_video(video, x, y, length, result):
    base = video[x][y]

    for i in range(x, x+length):
        for j in range(y, y+length):
            if video[i][j] != base:
                break
        else: # 정상 동작
            continue
        break
    else: # 정상 동작
        result.append(base)
        return

    leng = length // 2
    result.append("(")
    for i in range(2):
        for j in range(2):
            zip_video(video, x+(i*leng), y+(j*leng), leng, result)
    result.append(")")
    
zip_video(video, 0, 0, n, result)
print(''.join(map(str, result)))