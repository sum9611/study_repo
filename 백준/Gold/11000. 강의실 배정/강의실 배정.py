from sys import stdin
import heapq
input = stdin.readline

n = int(input())
n_list = []
for i in range(n):
    heapq.heappush(n_list,list(map(int,input().split())))

    
n_list.sort()


result_queue = []
heapq.heappush(result_queue, n_list[0][1])





for i in range(1,n):
    if n_list[i][0] < result_queue[0]:
        heapq.heappush(result_queue, n_list[i][1])
        
    else:
        heapq.heappop(result_queue)
        heapq.heappush(result_queue, n_list[i][1])
    
    
print(len(result_queue))

