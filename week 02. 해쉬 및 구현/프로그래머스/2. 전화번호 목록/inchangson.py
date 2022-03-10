def solution(phone_book):
    answer = True
    mem = set(phone_book)
    for num in phone_book :
        for i in range(1,len(num)):
            if num[:i] in mem :
                return False
    return answer