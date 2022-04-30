def is_work_done(word):
    for ch in word:
        if ch != 'A':
            return False
    return True

def get_char_diff(temp):
    cand1 = ord(temp) - ord('A')
    cand2 = 26 - cand1
    return min(cand1, cand2)

def get_next(cur_idx, step, word):
    
    for cnt in range(1, len(word)):
        next_idx = (cur_idx + cnt * step + len(word)) % len(word)        
        if word[next_idx] != 'A':
            return cnt, next_idx
    return 0, cur_idx

def change_word(cur_idx, word):
    if is_work_done(word):
        return 0
    
    temp = word[cur_idx]
    result = get_char_diff(temp)
    left_steps, left_idx = get_next(cur_idx, -1, word)
    right_steps, right_idx = get_next(cur_idx,  1, word)
    
    word[cur_idx] = 'A'
    cand1 = change_word(left_idx, word) + left_steps
    cand2 = change_word(right_idx, word) + right_steps
    word[cur_idx] = temp
    
    return result + min(cand1, cand2)

def solution(name):
    answer = 0
    word = list(name)
    answer = change_word(0, word)
    return answer