def get_max_score(depth, step, memo, triangle):
    if depth == len(triangle):
        return 0
    if memo[depth][step] != -1:
        return memo[depth][step]
    
    cand1 = get_max_score(depth + 1, step, memo, triangle)
    cand2 = get_max_score(depth + 1, step + 1, memo, triangle)
    
    memo[depth][step] = max(cand1, cand2) + triangle[depth][step]

    return memo[depth][step]
    
def solution(triangle):
    answer = 0
    memo = []
    for depth in range(len(triangle)):
        memo.append([-1]*len(triangle[depth]))
    answer = get_max_score(0, 0, memo, triangle)
    return answer