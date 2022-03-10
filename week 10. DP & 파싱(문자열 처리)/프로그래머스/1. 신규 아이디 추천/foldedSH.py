import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub('[^-_.a-zA-Z0-9]', '', new_id) # 2단계
    new_id = re.sub('\.+', '.', new_id) # 3단계
    new_id = re.sub('^\.|\.$', '', new_id) # 4단계
    new_id = 'a' if len(new_id) == 0 else new_id # 5단계
    new_id = new_id[:15] # 6단계
    new_id = re.sub('^\.|\.$', '', new_id) # 4단계
    new_id = new_id.ljust(3, new_id[-1]) if len(new_id) <= 2 else new_id # 7단계
    
    return new_id