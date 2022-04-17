def solution(array, commands):
    answer = []
    for command in commands:
        sorted_arr = array[(command[0] - 1) : (command[1])]
        sorted_arr.sort()
        answer.append(sorted_arr[command[2] - 1])
    return answer
