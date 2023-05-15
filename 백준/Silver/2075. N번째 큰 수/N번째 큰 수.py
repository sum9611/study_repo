import heapq

n = int(input())
n_list = []
for i in range(n):
    for j in list(map(int,input().split())):
        if len(n_list) < n:
            heapq.heappush(n_list,j)
        else:
            heapq.heappushpop(n_list,j)
print(heapq.heappop(n_list))