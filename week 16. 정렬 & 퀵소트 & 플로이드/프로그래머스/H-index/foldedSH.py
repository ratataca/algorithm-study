def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for h in range(citations[0], -1, -1):
        h_gte = len([c for c in citations if c >= h])

        if h_gte>=h:
            break
    return h