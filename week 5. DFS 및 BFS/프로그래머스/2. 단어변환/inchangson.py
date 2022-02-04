from queue import Queue

def isPossible(word1, word2):
    cnt = 0
    for idx in range(len(word1)):        
        if word1[idx] != word2[idx]:
            cnt += 1
            if cnt > 1:
                return False
    return True

def solution(begin, target, words):
    answer = 0
    
    checked = [False]*len(words)
    
    history = Queue()
    history.put((begin, 0))
    
    while history.qsize():
        cur_word, cur_cnt = history.get()
        if cur_word == target:
            answer = cur_cnt
            break
        for next_word in words:
            next_word_idx = words.index(next_word)
            if checked[next_word_idx]:
                continue
            if isPossible(next_word, cur_word):
                checked[words.index(next_word)] = True
                history.put((next_word, cur_cnt + 1))
    return answer