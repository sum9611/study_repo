from sys import stdin

# input = stdin.readline

n = int(input())
dp = [0] * (n+1)

if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4,n+1):
        if i%2 == 0 and i%3 == 0:
            dp[i] = min(dp[int(i/2)] + 1, dp[i-1] + 1, dp[int(i/3)] + 1)
        elif i%2 == 0:
            dp[i] = min(dp[int(i/2)] + 1, dp[i-1] + 1)
        elif i%3 == 0:
            dp[i] = min(dp[int(i/3)] + 1, dp[i-1] + 1)
        else:
            dp[i] = dp[i-1] + 1
    print(dp[n])
