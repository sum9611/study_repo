from sys import stdin
from collections import deque
# import sys
# sys.setrecursionlimit(10**7)
input = stdin.readline


n = int(input())
mp = []
node = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    mp.append(list(map(int,input().split())))
queue = deque()
queue.append([0,1,'r'])

while queue:
    point = queue.pop()
    x = point[0]
    y = point[1]
    d = point[2]

    # 오른쪽방향인경우 
    if d == 'r':
        # 오른쪽탐색
        nx = x
        ny = y+1
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'r'])
        # 대각 탐색
        nx = x+1
        ny = y+1
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0 and mp[nx-1][ny] == 0 and mp[nx][ny-1] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'rd'])

    # 아래방향인경우
    if d == 'd':
        # 아래쪽 탐색
        nx = x+1
        ny = y
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'d'])
        # 대각 탐색
        nx = x+1
        ny = y+1
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0 and mp[nx-1][ny] == 0 and mp[nx][ny-1] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'rd'])

    # 대각방향인경우
    if d == 'rd':
        # 아래쪽 탐색
        nx = x+1
        ny = y
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'d'])
        # 오른쪽탐색
        nx = x
        ny = y+1
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'r'])
        # 대각 탐색
        nx = x+1
        ny = y+1
        if nx < n and ny < n and nx > -1 and ny >-1 and mp[nx][ny] == 0 and mp[nx-1][ny] == 0 and mp[nx][ny-1] == 0:
            node[nx][ny] += 1
            queue.append([nx,ny,'rd'])

print(node[n-1][n-1])




    