from sys import stdin

# input = stdin.readline

n = int(input().rstrip())
y_list = []
dp = [0]*(n)

for i in range(n):
    y_list.append(int(input()))

if n == 1:
    print(y_list[0])

elif n == 2:
    print(y_list[1] + y_list[0])    
else:
    dp[0] = y_list[0]
    dp[1] = y_list[1] + y_list[0]

    for i in range(2,n):
        dp[i] = max(y_list[i] + y_list[i-1] + dp[i-3], y_list[i] + dp[i-2],dp[i-1])

    print(max(dp))