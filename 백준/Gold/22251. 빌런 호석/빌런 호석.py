n, k, p, x = map(int,input().split())
num_list = [[1,1,1,0,1,1,1],
            [0,0,1,0,0,0,1],
            [0,1,1,1,1,1,0],
            [0,1,1,1,0,1,1],
            [1,0,1,1,0,0,1],
            [1,1,0,1,0,1,1],
            [1,1,0,1,1,1,1],
            [0,1,1,0,0,0,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,0,1,1]
            ]
num_info = [num_list[int(i)] for i in str(x).zfill(k)]

result = 0
for i in range(1,n+1):
    target = str(i).zfill(k)
    target_info  = [num_list[int(j)] for j in target]
    cnt = 0
    
    for K in range(k):
        for l in range(7):
            if target_info[K][l] != num_info[K][l]:
                cnt += 1
    if cnt <= p:
        result += 1 
print(result-1)