from collections import defaultdict

def solution(genres, plays):
    # genres[i] : 고유 번호가 i인 노래 장르
    # plays[i] : 고유 번호가 i인 노래가 재생된 횟수
    answer = []

    playlist = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        playlist[g].append((i, p))

    playlist = dict(sorted(playlist.items(), key=lambda x: sum([_x[1] for _x in x[1]]), reverse=True))

    for key, value in playlist.items():
        value = sorted(value, key=lambda x: x[1], reverse=True)

        answer.append(value[0][0])

        if len(value) >= 2:
            answer.append(value[1][0])

    return answer