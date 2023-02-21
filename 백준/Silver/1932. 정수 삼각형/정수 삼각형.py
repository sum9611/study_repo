from sys import stdin

input = stdin.readline

n = int(input())
t_list = []
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    t_list.append(list(map(int,input().split())))

dp[0][0] = t_list[0][0]


for i in range(1,n):
    for j in range(len(t_list[i])):
        dp[i][j] = max(t_list[i][j] + dp[i-1][j], t_list[i][j] + dp[i-1][j-1])
print(max(dp[n-1]))
