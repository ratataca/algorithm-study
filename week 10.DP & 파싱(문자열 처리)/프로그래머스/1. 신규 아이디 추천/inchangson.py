import re

cnt = 0
def myprint(s):
    global cnt
    #print(cnt, s)
    #cnt += 1
    pass

def solution(new_id):
    answer = ''
    myprint(new_id)
    # step 1 : 소문자 고치기
    new_id = new_id.lower()
    myprint(new_id)
    
    # step 2 : 소문자, 숫자, 빼기, 밑줄, 마침표 외 문자 제거
    new_id = re.sub(r'[^a-z0-9_.-]','',new_id)
    myprint(new_id)
    
    # step 3 : 마침표 두 번 이상이면 하나로 줄이기
    new_id = re.sub(r'[.]+','.',new_id)
    myprint(new_id)
    
    # step 4 : 마침표가 처음이나 끝이면 제거
    new_id = new_id.strip('.')
    myprint(new_id)
    
    # step 5 : 빈문자열이면 a로 대체
    if not new_id:
        new_id = "a"
    myprint(new_id)
    
    # step 6a: 길이가 16자 이상이면, 15개의 문자를 제외한 나머지 모두 제거
    new_id = new_id[0:15]
    myprint(new_id)
    
    # step 6b: a의 결과 문자열의 끝이 마침표라면 해당 마침표 제거
    new_id = new_id.rstrip('.')
    
    # step 7 : 2자 이하면 길이가 3이 될 때까지 마지막 문자 반복
    if len(new_id) <= 2:
        new_id = new_id + (new_id[-1])*(3-len(new_id))
    myprint(new_id)
    
    answer = new_id
    
    return answer