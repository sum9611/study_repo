from sys import stdin 

input = stdin.readline

n = int(input())

xy_list = []



for i in range(n):
    x, y = (map(int,input().split()))
    
    xy_list.append([x,y])



rank_list = []

for i in range(len(xy_list)):
    x = xy_list[i][0]
    y = xy_list[i][1]
    rank = 1    

    for j in range(len(xy_list)):

        if (xy_list[j][0] > x) and (xy_list[j][1] > y):
            rank += 1
    rank_list.append(rank)

for i in rank_list:
    print(i, end=' ')