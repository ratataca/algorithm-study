def solution(progresses, speeds):
    answer = []
    need_day = []
    cnt = 1

    for i in range(len(progresses)):
        tmp = int((100 - progresses[i]) / speeds[i] + 0.9)
        need_day.append(tmp)

    f_work = need_day.pop(0)
    while True:
        s_work = need_day.pop(0)

        if f_work < s_work:
            answer.append(cnt)
            f_work = s_work
            cnt = 0

        cnt += 1
        if len(need_day) < 1:
            break

    if len(need_day) < 1 and f_work >= s_work:
        answer.append(cnt)

    return answer