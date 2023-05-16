from sys import stdin
input = stdin.readline

n,m = map(int,input().split())

mp = []
for _ in range(n):
    mp.append(list(map(int,input().split())))

vis = [['0' for _ in range(m)] for _ in range(n)]

# 시작지점 찾기
for i in range(n):
    for j in range(m):
        if mp[i][j] == 2:
            sp = [i,j]
            
queue = [sp]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
vis[sp[0]][sp[1]] = 0
while queue:
    xy = queue.pop(0)
    x = xy[1]
    y = xy[0]
    num = int(vis[y][x])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < m and ny >=0 and ny < n:
            if mp[ny][nx] == 1:
                queue.append([ny,nx])
                vis[ny][nx] = num+1
                mp[ny][nx] = 2
            elif mp[ny][nx] == 0:
                vis[ny][nx] = 0
                
for i in range(n):
    for j in range(m):
        if vis[i][j] == '0' and mp[i][j] != 0:
            print(-1, end=' ')
        else:
            print(vis[i][j],end=' ')
    print('')

