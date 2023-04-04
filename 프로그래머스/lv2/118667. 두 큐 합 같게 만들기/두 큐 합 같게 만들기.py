from collections import deque

def solution(queue1, queue2):
    queue_1 = deque([])
    queue_2 = deque([])
    for i,j in zip(queue1, queue2):
        queue_1.append(i)
        queue_2.append(j)
        
    
    answer = 0
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    if (sum_1+sum_2)%2 == 1:
        return -1
    
    while sum_1 != sum_2:
        
        if sum_1 == 0 or sum_2 == 0:
            return -1
        if answer >= 600000:
            return -1
        
        if sum_1 > sum_2:
            p = queue_1.popleft()
            sum_1 -= p
            
            queue_2.append(p)
            sum_2 += p
            
            answer += 1
        elif sum_2 > sum_1:
            p = queue_2.popleft()
            sum_2 -= p
            
            queue_1.append(p)
            sum_1 += p
            answer += 1
            
    return answer
    
    