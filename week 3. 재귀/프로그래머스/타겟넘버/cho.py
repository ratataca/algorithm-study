
def recursive(arr, m, operators_list):
    if m == len(arr):
        operators_list.append(list(arr))
        return 
    
    arr.append('+')
    recursive(arr, m, operators_list)
    arr.pop()
    arr.append('-')
    recursive(arr, m, operators_list)
    arr.pop()
    
def solution(numbers, target):
    answer = 0
    operators_list = []
    recursive([], len(numbers), operators_list)
    for operators in operators_list:
        result = 0
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i]
            else:
                result -= numbers[i]
        if result == target:
            answer += 1
    return answer
    



