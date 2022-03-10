def solution(s):
    _min = len(s)
    for i in range(1, len(s)//2+1):
        start = 0
        end = start+i

        while True:
            base = s[start:end]

            # 문자열을 넘어가거나 맨 앞이 잘리지 않는 경우
            start += i
            end += i
            if end > len(s): # or base != s[start:end]:
                break

            # 문자열 탐색
            new_str = ''
            cnt = 1
            for _ in range(len(s)//i+1):
                if base != s[start:end]:
                    if cnt != 1:
                        new_str += f'{cnt}{base}'
                    else:
                        new_str += base
                    base = s[start:end]
                    cnt = 1
                else:
                    cnt += 1
                start += i
                end += i
            if len(new_str) < _min:
                _min = len(new_str)
    return _min