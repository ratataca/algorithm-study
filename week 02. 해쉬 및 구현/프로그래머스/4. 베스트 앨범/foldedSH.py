def solution(genres, plays):
    answer = []
    
		# 장르별 재생 총 횟수
    genres_cnt = dict(zip(set(genres), [0]*len(set(genres))))
    for idx in range(len(genres)):
        g = genres[idx]
        p = plays[idx]

        genres_cnt[g] += p

    genre_plays = sorted(list(enumerate(zip(genres, plays))),  key = lambda x : x[1], reverse=True)
    genres_order = sorted(genres_cnt, key = lambda x : genres_cnt[x], reverse = True)
    for g in genres_order:
        tmp = list(filter(lambda x : x[1][0] == g, genre_plays))
        tmp = [i[0] for i in tmp]
        answer.append(tmp[0]) 
        if len(tmp) >= 2:
            answer.append(tmp[1])
        
    return answer