from collections import deque

def solution(places):
    SZ = 5
    answer = []
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    def check_distance(r, c, room):
        # bfs
        #visit = [[0]*5 for _ in range(5)]
        
        paths = deque()
        paths.append((r, c, 0))
        #visit[2][2] = 1
        
        while paths:
            cur_r, cur_c, cur_d = paths.popleft()
            if cur_d == 2:
                break
            for d in direction:
                next_r = cur_r + d[0]
                next_c = cur_c + d[1]
                if not (0 <= next_r < 5 and 0 <= next_c < 5):
                    continue
                if room[next_r][next_c] == 'X':
                    continue
                #if visit[next_r - r + 2][next_r - c + 2]:
                    #continue
                if (next_r, next_c) != (r, c) and room[next_r][next_c] == 'P':
                    #print('fail', r, c, next_r, next_c)
                    return False
                #visit[next_r - r + 2][next_c - c + 2] = 1
                paths.append((next_r, next_c, cur_d + 1) )
        return True
    
    def get_status(room):
        
        for r in range(SZ):
            for c in range(SZ):
                if room[r][c] == 'P':
                    if not check_distance(r, c, room):
                        return 0
        return 1
        
    for place in places:
        answer.append(get_status(place))
    
    return answer