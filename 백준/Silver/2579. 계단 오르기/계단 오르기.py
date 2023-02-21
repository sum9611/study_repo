from sys import stdin

# input = stdin.readline

n = int(input())

s_list = []

for i in range(n):
    s_list.append(int(input()))
dp = [0] * n

if n == 1 :
    print(s_list[0])
elif n == 2:
    print(s_list[0] + s_list[1]) 
elif n == 3:
    print(max(s_list[1] + s_list[2], s_list[0] + s_list[2]))
else:

    dp[0]= s_list[0]
    dp[1] = s_list[0] + s_list[1]
    dp[2] = max(s_list[1] + s_list[2], s_list[0] + s_list[2])
    for i in range(3,n):
        dp[i] = max(dp[i-3] + s_list[i-1] + s_list[i],
            dp[i-2] + s_list[i])
    print(dp[n-1])    