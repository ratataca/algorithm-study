#n으로 표현

def make_num(cnt, memo, N, num):
    if cnt == 9:
        return -1
    temp = set()
    temp.add(int(str(N)*cnt))
    
    for n1 in range(1, cnt):
        n2 = cnt - n1
        if n2 == 0:
            break
        for i1 in range(len(memo[n1])):
            for i2 in range(len(memo[n2])):
                temp.add(memo[n1][i1] + memo[n2][i2])
                temp.add(memo[n1][i1] - memo[n2][i2])
                temp.add(memo[n1][i1] * memo[n2][i2])
                if memo[n2][i2]:
                    temp.add(memo[n1][i1] // memo[n2][i2])

    if num in temp:
        return cnt
    else:
        memo[cnt] = list(temp)
        return make_num(cnt + 1, memo, N, num)

def solution(N, number):
    answer = 0
    if N == number:
        return 1
    memo = [[] for _ in range(9)]
    answer = make_num(1, memo, N, number)
    
    return answer