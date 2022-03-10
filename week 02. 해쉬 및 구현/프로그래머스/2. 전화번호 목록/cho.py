# wrong
def solution(phone_book):
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            if (prefix in phone_book) and prefix != phone_number:
                return False
    return True


# right
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return True


# hash
def solution(phone_book):
    Dict = {}
    
    for i in range(len(phone_book)):
        Dict[phone_book[i]] = 1
        
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            if prefix in Dict.keys() and prefix != phone_number:
                return False

    return True
