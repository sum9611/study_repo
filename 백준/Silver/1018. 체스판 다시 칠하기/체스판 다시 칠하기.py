from sys import stdin 

input = stdin.readline
board = []

n,m = map(int, input().split())


for i in range(n):
    board.append(input())

# 제일 첫 칸 색 지정 
colors = ['W', 'B']
cnt_list = []
cnt = 0

## 8x8로 나누는 모든 경우의 수 
for a in range(n-7):
    for b in range(m-7):
        
        for k in colors:
            start_color = k
            cnt = 0
            for i in range(a,8+a):
                # 행이 변화할때마다 시작색과 비교하며 변경 필요 
                color = start_color
                if i%2 == 1:
                    if color == 'W':
                        color = 'B'
                    elif color == 'B':
                        color = 'W' 
                # 열 비교                  
                for j in range(b, 8+b):
                    if board[i][j] != color:
                        cnt += 1
                    if color == 'W':
                        color = 'B'
                    elif color == 'B':
                        color = 'W'
            cnt_list.append(cnt)  
                
print(min(cnt_list))