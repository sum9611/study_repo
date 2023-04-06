tc = int(input())


for _ in range(tc):
    n, k, t, m = map(int,input().split())
    n_list = [[0 for _ in range(k+2)]for _ in range(n)]
    for i in range(m):
        id, qn, s = map(int,input().split())
        n_list[id-1][qn-1] = max(s,n_list[id-1][qn-1])
        n_list[id-1][-2] += 1
        n_list[id-1][-1] = i+1

    team_total, team_cnt, team_last = sum(n_list[t-1][:-2]), n_list[t-1][-2], n_list[t-1][-1]
    cnt = 1
    for i in range(len(n_list)):


        if i == t-1 :
            continue
        elif sum(n_list[i][:-2]) > team_total :

            cnt += 1
        elif sum(n_list[i][:-2]) == team_total and n_list[i][-2] < team_cnt:

            cnt += 1
        elif sum(n_list[i][:-2]) == team_total and n_list[i][-2] == team_cnt and n_list[i][-1] < team_last:

            cnt += 1
    print(cnt)



