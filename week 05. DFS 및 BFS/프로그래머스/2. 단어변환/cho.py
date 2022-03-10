def find_friends(x, words):
    friends_list = []
    for word in words:
        cnt = 0
        for i in range(len(word)):
            if word[i] != x[i]:
                cnt += 1
            if cnt > 1:
                continue
        if cnt == 1:
            friends_list.append(word)
    return friends_list
    
def solution(begin, target, words):
    List = {}
    words.append(begin)
    for word in words:
        List[word] = find_friends(word, words)
        
    visited = []
    need_visit = [(begin, 0)]
    while need_visit:
        node, depth = need_visit.pop(0)
        if node == target:
            return depth
        if node not in visited:
            visited.append(node)
            for a in List[node]:
                need_visit.append((a, depth+1))
    return 0