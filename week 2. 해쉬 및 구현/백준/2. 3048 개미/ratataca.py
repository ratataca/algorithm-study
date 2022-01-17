len_f, len_s = [int(n) for n in input().split(" ")]

f_s = [i for i in input()][::-1]
s_s = [i for i in input()]
T = int(input())


# --
calc_f_idx = [0 for _ in range(len(f_s))]
calc_s_idx = [0 for _ in range(len(s_s))]

cnt = 1
while T > 0:
    for i in range(cnt):
        if calc_f_idx[i % len_f] < len_s:
            calc_f_idx[i % len_f] += 1

        if calc_s_idx[i % len_s] > len_f * -1:
            calc_s_idx[i % len_s] -= 1
    cnt += 1
    T -= 1

# 결과 값 만들기
calc_f_idx = calc_f_idx[::-1]
ants_idx = calc_f_idx + calc_s_idx

ants = [s for s in f_s + s_s]
result = ['' for _ in range(len_f + len_s)]

for idx, v in enumerate(ants_idx):
     result[idx + v] = ants[idx]

print("".join(result))