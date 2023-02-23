from sys import stdin
import heapq 

input = stdin.readline
n = int(input())
n_list = []
for i in range(n):
    heapq.heappush(n_list, int(input()))


for i in range(n):
    print(heapq.heappop(n_list))
