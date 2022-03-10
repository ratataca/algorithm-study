# wrong
def solution(participant, completion):
    for comp in completion:
        if comp in participant:
            participant.pop(participant.index(comp))
    answer = participant[0]
    return answer

# right
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] !=participant[i]:
            return participant[i]
    
    return participant[-1]

# hash
def solution(participant, completion):
    sumhash = 0
    Dict = {}
    for athlete in participant:
        Dict[hash(athlete)] = athlete
        sumhash += hash(athlete)
        
    for athlete in completion:
        sumhash -= hash(athlete)
    
    return Dict[sumhash]
