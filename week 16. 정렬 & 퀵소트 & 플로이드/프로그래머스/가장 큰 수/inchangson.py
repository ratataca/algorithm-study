import functools

def solution(numbers):
    def compare(n1, n2):
        n1n2, n2n1 = n1 + n2, n2 + n1
        
        if n1n2 < n2n1:
            return 1
        elif n1n2 > n2n1:
            return -1
        return 0
    
    strNumbers = list(map(str, numbers))
    
    strNumbers.sort(key = functools.cmp_to_key(compare))
    
    answer = ''.join(strNumbers) if strNumbers[0] != "0" else "0"
    return answer