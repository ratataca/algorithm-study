def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    
    if min_move < 0:
        return answer
        
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + (i + len(name)) - next)
    answer += min_move
    return answer