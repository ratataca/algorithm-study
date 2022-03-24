def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    answer = ''
    for id in new_id:
        if id in "abcdefghijklmnopqrstuvwxyz-_.0123456789":
            answer += id
    
    # 3단계
    while True:
        if ".." in answer:
            answer = answer.replace("..", '.')
        else:
            break
    
    # 4단계
    try:
        if answer[0] == '.':
            answer = answer[1:]
    except:
        pass
    
    try:
        if answer[-1] == '.':
            answer = answer[:-1]
    except:
        pass
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
        
    # 7단계
    if len(answer) < 3:
        answer = answer + (answer[-1] * (3 - len(answer)))    
    return answer