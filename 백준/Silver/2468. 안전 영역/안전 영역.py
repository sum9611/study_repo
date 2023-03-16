from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**7)
# input = stdin.readline

n = int(input())

mp = []
for i in range(n):
    mp.append(list(map(int,input().split())))
    
    
# 방향설정
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx <= (n-1) and ny <= (n-1):
            if mp[nx][ny] != -1 and node[nx][ny] == 0:
                node[nx][ny] = 1
                DFS(nx,ny)

cnt_list = []

# 비의 높이 마다 반복 
for i in range(0,101):
    # 노드 초기화 
    node = [[0 for _ in range(n)] for _ in range(n)] 
    cnt = 0 
    # 높이에 따른 침수 지역 표시
    for j in range(n):
        for k in range(n):
            if mp[j][k] <= i:
                mp[j][k] = -1
    for a in range(n):
        for b in range(n):
            # 침수지역이 아닐경우
            if mp[a][b] != -1 and node[a][b] == 0:
                cnt += 1
                DFS(a,b)
    cnt_list.append(cnt)
print(max(cnt_list))
                        
