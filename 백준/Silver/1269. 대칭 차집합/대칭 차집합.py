from sys import stdin

input = stdin.readline

a,b = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
ab_dict = {}
cnt = 0
for i in a_list:
    ab_dict[i] = 2

for i in b_list:
    if ab_dict.get(i) == None:
        ab_dict[i] = 2
    else:
        ab_dict[i] = 1

for i in ab_dict:
    if ab_dict[i] == 2:
        cnt += 1
print(cnt)

