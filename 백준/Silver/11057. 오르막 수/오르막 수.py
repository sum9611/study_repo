from sys import stdin

# input = stdin.readline

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n)]

dp[0] = [1 for _ in range(10)]

for i in range(1,n):
    dp[i][0] = 1
    for j in range(1,10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
print(sum(dp[n-1])%10007)
