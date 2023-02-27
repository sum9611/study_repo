from sys import stdin

# input = stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s_list = []
    s_list.append(list(map(int, input().split())))
    s_list.append(list(map(int, input().split())))

    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = s_list[0][0]
    dp[1][0] = s_list[1][0]


    for i in range(1,n):

        if i == 1:
            dp[0][1] = dp[1][0] + s_list[0][1]
            dp[1][1] = dp[0][0] + s_list[1][1]
        else:
            dp[0][i] = max(dp[1][i-1] + s_list[0][i], dp[1][i-2] + s_list[0][i])
            dp[1][i] = max(dp[0][i-1] + s_list[1][i], dp[0][i-2] + s_list[1][i])
    print(max(max(dp[0]), max(dp[1])))
