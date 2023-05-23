from sys import stdin
input = stdin.readline
from collections import deque
n, l, r = map(int,input().split())
mp = []
for _ in range(n):
    mp.append(list(map(int,input().rstrip().split())))
    
def bfs(a,b,check):
    queue = deque([[a,b]])
    queue2 = [[a,b]]
    sum_p = 0
    # 연합의 총 인구수 구하기
    while queue:
        xy = queue.popleft()
        x,y = xy[0], xy[1]
        vis[x][y] = 1
        sum_p += mp[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
                gap = mp[x][y] - mp[nx][ny]
                if abs(gap) >=l and abs(gap) <= r and vis[nx][ny] != 1:
                    check += 1
                    queue.append([nx,ny])
                    queue2.append([nx,ny])
                    vis[nx][ny] = 1
    return queue2, check, sum_p

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
check = 0
while True:
    # 국경 개방때마다 방문횟수 초기화하기 
    vis = [[0 for _ in range(n)] for _ in range(n)]
    cnt += 1
    # print(f'{cnt}번째 국경 개방')
    
    check = 0

    # 연합만들기 for문
    for a in range(n):
        for b in range(n):
            if vis[a][b] == 0:
                queue2,check,sum_p = bfs(a,b,check)
                if len(queue2) > 1:
                    result_p = sum_p//len(queue2)
                    # 인구 이동시키기
                    for i in queue2:
                        mp[i[0]][i[1]] = result_p

    if check == 0:
        print(cnt - 1)
        break
                


                            

                            
                            
  