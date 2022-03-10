def solution(s):
    answerList = []
    if len(s) == 1:
        return 1
    for size in range(1, len(s) // 2 + 1):
        List = [s[i : i + size] for i in range(0, len(s), size)]
        count = 1
        answer = ""

        for i in range(1, len(List)):
            if List[i - 1] == List[i]:
                count += 1
            else:
                answer += (str(count) + List[i - 1]) if count > 1 else List[i - 1]
                count = 1
        answer += (str(count) + List[-1]) if count > 1 else List[-1]
        answerList.append(len(answer))
    return min(answerList)
