N, time = [int(n) for n in input().split()]

# 단원별 예상 공부 시간, 그 단원의 문제 배점
info = [[int(n) for n in input().split()] for _ in range(N)]


# 최대 점수 
#   - (점수, 남은 시간 양)
# memo = [[0, time]]
memo = [[0 for _ in range(n)] for n in range(1, N + 1)]
print(memo)


for need, score in info:
    pass
