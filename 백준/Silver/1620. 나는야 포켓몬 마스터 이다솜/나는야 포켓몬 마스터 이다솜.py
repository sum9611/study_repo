from sys import stdin 

input = stdin.readline

n,m = map(int,input().split())

n_list_id = {}
n_list_name = {}

for i in range(1,n+1):
    input_n = input().rstrip()
    n_list_id[i] = input_n
    n_list_name[input_n] = i

for _ in range(m):
    input_m = input().rstrip()
    if input_m.isdigit():
        print(n_list_id[int(input_m)])
    else:
        print(n_list_name[input_m])
