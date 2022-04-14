def solution(number, k):    
    numbers = []
    for num in number:
        while True:
            if numbers != [] and (int(num) > numbers[-1]) and k:
                numbers.pop()
                k -= 1
            else:
                break
        numbers.append(int(num))
        
    if k != 0:
        numbers = numbers[:len(number)-k]
    return ''.join(list(map(str, numbers)))