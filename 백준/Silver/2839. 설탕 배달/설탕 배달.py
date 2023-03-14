from sys import stdin

# input = stdin.readline

dp = [-1] * 5001


n = int(input())

dp[3] = 1
dp[4] = -1
dp[5] = 1

for i in range(6,5001):
    if dp[i-3] == -1 and dp[i-5] == -1:
        dp[i] = -1
    elif dp[i-3] != -1 and dp[i-5] == -1:
        dp[i] = dp[i-3] + 1
    elif dp[i-3] == -1 and dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[n])
