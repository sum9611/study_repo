from sys import stdin

input = stdin.readline

n = int(input().rstrip())

dp = [0] * (n+3)

dp[1] = 0
dp[2] = 1
dp[3] = 1
if n <4:
    print(dp[n])

else:
    for i in range(4,n+1):
        dp[i] = dp[int(i-1)] +1
        if i%2 == 0:
            dp[i] = min(dp[int(i/2)] +1, dp[i])
        if i%3 == 0:
            dp[i] = min(dp[int(i/3)] +1, dp[i])
    print(dp[n])