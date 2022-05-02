def solution(name):
    cnt = 0
    
    # 좌우 이동 최대 횟수
    RL_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 상하 조이스틱 최소 횟수
        cnt += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        # 다음 알파벳 중 A 문자열이 아닌 문자의 위치
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        # 기존 값, 오른쪽으로 가다가 왼쪽으로 가는 값, 왼쪽으로 가다가 오른쪽으로 가는 값
        RL_move = min([RL_move, 2 *i + len(name) - next_idx, i + 2 * (len(name) -next_idx)])
        
    # 상하 이동+좌우 이동
    cnt += RL_move
    return cnt