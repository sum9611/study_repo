from sys import stdin
from collections import deque
# input = stdin.readline

n, k = map(int,input().split())

mp = [-1 for _ in range(100001)]
mp[n] = 0
queue = [n]
# queue.append(n)
while True:
    x = queue.pop(0)
    
    if x-1 >= 0:
        if (mp[x-1] == -1):
            mp[x-1] = mp[x] + 1
            queue.append(x-1)

    if x+1 <= 100000:            
        if (mp[x+1] == -1):
            mp[x+1] = mp[x] + 1
            queue.append(x+1)
            
    if x*2 <= 100000:
        if (mp[x*2] == -1):
            mp[x*2] = mp[x] + 1
            queue.append(x*2)

    if mp[k] != -1:
        print(mp[k])
        break
        
    
    
