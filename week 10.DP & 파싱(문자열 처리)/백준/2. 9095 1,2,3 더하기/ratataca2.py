'''
    1 + dp[3] : 방법 4가지
    2 + dp[2] : 방법 2가지
    3 + dp[1] : 방법 1가지
'''

N = int(input())
cases = [int(input()) for _ in range(N)]

memo = [0] * 11

memo[1] = 1
memo[2] = 2
memo[3] = 4

for i in range(4, 11):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        print(memo)

for case in cases:
    print(memo[case])