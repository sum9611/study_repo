from sys import stdin

# input = stdin.readline

n, m, k = map(int,input().split())

map_list = []
count_point = [0,0]
dice_north = 2
dice_south = 5
dice_west = 4
dice_east = 3
dice_center = 6
direct = 'e'


for i in range(n):
    map_list.append(list(map(int,input().split())))
    
    
d_list = ['e','s','w','n']
direct = d_list[0]

def moving(direct,count_point):
    
    #동쪽이동
    if direct == 'e':
        if count_point[1] == (m-1):
            direct = 'w'
            count_point[1] = count_point[1] - 1
        else:
            count_point[1] = count_point[1] + 1

    #서쪽이동
    elif direct == 'w':
        if count_point[1] == 0:
            direct = 'e'
            count_point[1] = count_point[1] + 1 
        else:
            count_point[1] = count_point[1] -1

    #남쪽이동 
    elif direct == 's':
        if count_point[0] == (n-1):
            direct = 'n'
            count_point[0] = count_point[0] -1 
        else:
            count_point[0] = count_point[0] + 1

    #북쪽이동
    elif direct == 'n':
        if count_point[0] == 0:
            direct = 's'
            count_point[0] = count_point[0] +1
        else:
            count_point[0] = count_point[0] -1 

    return direct, count_point

def dice_setting(direct, dice_center, dice_east, dice_north, dice_south, dice_west):
    
    #동쪽인경우 
    if direct == 'e':
        dice_west = dice_center
        dice_center = dice_east
        dice_east = (7 - dice_west)
    
    #서쪽인경우 
    if direct == 'w':
        dice_east = dice_center
        dice_center = dice_west
        dice_west = (7 - dice_east)
    
    #북쪽인경우
    if direct == 'n':
        dice_south = dice_center
        dice_center = dice_north
        dice_north = (7 - dice_south)

    #남쪽인경우
    if direct == 's':
        dice_north = dice_center
        dice_center = dice_south
        dice_south = (7 - dice_north)

    return dice_center, dice_east, dice_north, dice_south, dice_west

def sum_point(count_point):
    
    point = map_list[count_point[0]][count_point[1]]
    vis = [[0 for _ in range(m)] for _ in range(n)]
    queue = [[count_point[0], count_point[1]]]
    s_point = point
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        vis[x][y] = 1
        del queue[0]
        #상하좌우
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx <=(n-1) and ny >= 0 and ny <= (m-1):
                if map_list[nx][ny] == point:
                    if vis[nx][ny] != 1:
                        vis[nx][ny] = 1
                        s_point += point
                        queue.append([nx,ny])
    return s_point

total = 0
for i in range(k):
    
    # 방향이동
    direct, count_point = moving(direct, count_point)
    
    # 주사위이동
    dice_center, dice_east, dice_north, dice_south, dice_west = dice_setting(direct, dice_center, dice_east, dice_north, dice_south, dice_west)

    # 점수 획득 
    total += sum_point(count_point)


    # 비교단계
    # 주사위아랫면이 칸의 정수보다 큰 경우 시계방향 90도 회전
    if dice_center > map_list[count_point[0]][count_point[1]] :
        direct = d_list[(d_list.index(direct) + 1)%4]

    # 주사위아랫면이 칸의 정수보다 작은 경우 반시계방향 90도 회전
    elif dice_center < map_list[count_point[0]][count_point[1]]:
        direct = d_list[d_list.index(direct) - 1]

    # 같은경우 그대로     
    else:
        direct = d_list[d_list.index(direct)]

print(total)

     

    