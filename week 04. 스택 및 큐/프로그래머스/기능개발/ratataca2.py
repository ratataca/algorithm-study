def solution(progresses, speeds):
    answer = []

    while True:
        if len(progresses) <= 0:
            break

        # 단위 시간을 한번 더하는 부분
        for idx, sp in enumerate(speeds):
            progresses[idx] += sp

        # 배포 되는 지 확인하는 부분
        cnt = 0
        for pr in progresses:
            if pr >= 100:
                cnt += 1
            else:
                break

        if cnt != 0:
            answer.append(cnt)
            del progresses[0:cnt]
            del speeds[0:cnt]

    return answer