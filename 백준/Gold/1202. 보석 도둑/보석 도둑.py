from sys import stdin
import heapq
# N == 보석의 개수, K == 가방의 개수
N_list = []
K_list = []
N_list_temp = []
result = 0
N,K = map(int,stdin.readline().split())


for i in range(N):
    heapq.heappush(N_list, list(map(int,stdin.readline().split())))
    
for i in range(K):
    K_list.append(int(stdin.readline()))

K_list.sort()


for i in K_list:
    while N_list:
        if i >= N_list[0][0]:
            heapq.heappush(N_list_temp, -N_list[0][1])
            heapq.heappop(N_list)
        else:
            break
        
    if N_list_temp:
        result -= heapq.heappop(N_list_temp)
    else:
        if not N_list:
            break
print(result)