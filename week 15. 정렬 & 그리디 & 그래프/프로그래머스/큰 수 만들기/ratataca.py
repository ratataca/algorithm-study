def solution(number, k):
    
    stack = []
    for i in range(len(number)):
        while len(stack) > 0 and stack[-1] < number[i] and k > 0:
            stack.pop()
            k = k - 1
        
        if k == 0:
            stack += number[i:]
            break
            
        stack.append(number[i])
            
    return ''.join(stack[:len(stack) - k])