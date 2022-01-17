def solution(participant, completion):
    player = {}
    ans = ''
    for c in completion :
        if c not in player :
            player[c] = 1
            continue
        player[c] += 1
    for p in participant :
        if p not in player :
            return p
        player[p] -= 1
    for k, v in player.items() :
        if v != 0 :
            ans = k
            break
    return ans