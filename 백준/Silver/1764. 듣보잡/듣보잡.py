from sys import stdin

input = stdin.readline

n, m = map(int,input().split())
nm_dic = {}
cnt = 0
for i in range(n):
    name = input().rstrip()
    nm_dic[name] = 1

for i in range(m):
    name = input().rstrip()
    if nm_dic.get(name) == None:
        nm_dic[name] = 1
    else:
        nm_dic[name] = 2
        cnt += 1
nm_dic= dict(sorted(nm_dic.items()))
print(cnt)
for i in nm_dic:
    if nm_dic[i] == 2:
        print(i)