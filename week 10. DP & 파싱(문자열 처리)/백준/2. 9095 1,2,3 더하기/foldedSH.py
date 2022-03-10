t = int(input())
cases = [int(input()) for _ in range(t)]

for case in cases:
    dp = [0]*12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for num in range(4, case+1):
        dp[num] = dp[num-1]+dp[num-2]+dp[num-3]
    print(dp[case])