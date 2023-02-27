from sys import stdin

# input = stdin.readline


dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
for i in range(5,1001):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[int(input())]%10007)