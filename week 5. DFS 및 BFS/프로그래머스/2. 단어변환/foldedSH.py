def dfs(begin, target, words, visited):
    stack = [begin]
    cnt = 0
    while stack:
        visit = stack.pop()
        if visit == target:
            return cnt
        for v in range(len(words)):
            word = words[v]
            diff = 0
            for i in range(len(word)):
                alp = word[i]
                if alp != visit[i]:
                    diff += 1
            if diff == 1 and visited[v] == False:
                visited[v] = True
                stack.append(word)
        cnt += 1
    return cnt

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    answer = dfs(begin, target, words, visited)
    return answer