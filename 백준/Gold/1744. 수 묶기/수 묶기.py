from sys import stdin 
import heapq

N = int(stdin.readline())
result = 0

## 1보다 큰경우 
list1 = []

## 0보다 작은경우
list2 = []

## 0과 1인 경우
list3 = []

for i in range(N):
    temp_num = (int(stdin.readline()) * -1)
    if temp_num < -1:
        heapq.heappush(list1,temp_num)
    elif (temp_num == 0) or (temp_num == -1):
        heapq.heappush(list3,(temp_num*-1))
    else:
        heapq.heappush(list2,(temp_num*-1))
    

while len(list1) > 1:
    a = heapq.heappop(list1)
    b = heapq.heappop(list1)
    result += a*b
    
    if len(list1) == 1:
        result += heapq.heappop(list1) * -1
        break
    
while len(list2)> 1:
    a = heapq.heappop(list2)
    b = heapq.heappop(list2)
    result += a*b
    
    if len(list2) == 1:
        break

for i in range(list3.count(0)):
    if len(list2) == 0:
        break
    heapq.heappop(list2)        
        
print(result + sum(list2) + sum(list3) + (sum(list1)*-1))
