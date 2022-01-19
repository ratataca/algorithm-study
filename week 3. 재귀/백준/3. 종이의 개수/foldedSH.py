def division(data, x, y, _length, cnt):
    # 종이 한 장
    base = data[x][y]
    for i in range(x, x+_length):
        for j in range(y, y+_length):
            if data[i][j] != base:
                break
        else: # 한 행 모두 같은 값일 경우 -> 다음 행 확인 
            continue
        break # 같은 값 X인 경우, 반복문 stop

    else:
        cnt[base] += 1
        return
    
    # 종이 9장 분할
    leng = _length // 3 # 종이의 가로, 세로 길이
    for i in range(3):
        for j in range(3):
            division(data, x+i*leng, y+j*leng, leng, cnt)
            

n = int(input())

papers = []
for _ in range(n):
    paper = list(map(int, input().split()))
    papers.append(paper)
    
cnt = [0,0,0] # 0, 1, -1
division(papers, 0, 0, n, cnt)

print(cnt[-1])
print(cnt[0])
print(cnt[1])