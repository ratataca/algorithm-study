from collections import defaultdict

def solution(tickets):
    List = defaultdict(list)
    
    for i in tickets:
        List[i[0]].append(i[1])

    for i in List:
        List[i].sort(reverse=True)
    
    stack = ['ICN']
    answer = []

    while stack:
        
        if List[stack[-1]] == []:
            answer.append(stack.pop())
        else:
            stack.append(List[stack[-1]].pop())
    answer.reverse()
    return answer