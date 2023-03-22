t = int(input())

for _ in range(t):
    team_score = [[] for _ in range(201)]
    n = int(input())
    score_list = list(map(int,input().split()))
    cnt = 0
    for i in score_list:
        if score_list.count(i) == 6:
            cnt += 1
            if len(team_score[i]) < 5:
                team_score[i].append(cnt)
    score = []
    for j in range(len(team_score)):
        if len(team_score[j]) == 5:
            score.append([j,sum(team_score[j][:4]), team_score[j][-1]])
    rank = [0,4000,0]
    for k in score:
        if k[1] < rank[1]:
            rank[0] = k[0]
            rank[1] = k[1]
            rank[2] = k[2]
        elif k[1] == rank[1]:
            if k[2] < rank[2]:
                rank[0] = k[0]
                rank[1] = k[1]
                rank[2] = k[2]
    print(rank[0])