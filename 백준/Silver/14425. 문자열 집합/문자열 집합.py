from sys import stdin 

input = stdin.readline

n,m = map(int,input().split())

n_list = []
m_list = []


for i in range(n):
    n_list.append(input())

for i in range(m):
    m_list.append(input())
n_list.sort()    
    
def check(n_list, i, start, end):
    # print(' ')
    if start > end:
        # print('없음! 종료합니다.')
        return 0
    center = (start + end) // 2
    # print('비교값 : ', n_list[center])
    if n_list[center] > i :
        # print('작습니다. end값 변경')
        return check(n_list, i, start, center -1)
    elif n_list[center] == i :
        # print('찾음 종료합니다!')
        return 1
    else:
        # print('큽니다. start값 변경')
        return check(n_list,i, center +1, end)    
    

cnt = 0
 
for i in m_list:
    cnt += check(n_list, i, 0 , n-1)
    

print(cnt)

