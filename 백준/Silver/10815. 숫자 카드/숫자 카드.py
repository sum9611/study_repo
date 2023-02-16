from sys import stdin 

input = stdin.readline

n = int(input())

n_list = list(map(int,input().split()))

m = int(input())

m_list = list(map(int,input().split()))

n_list.sort()
    
   
def check(n_list, i, start, end):
    
    # 해당값이 없을경우 탈출하는 로직 
    if start > end :
        return print(0, end = ' ')
    center = (start + end) //2
    
    # 값을 찾은경우     
    if n_list[center] == i:
        return print(1, end = ' ')

    # i 값이 중간값보다 작은경우 end 값 변경
    elif n_list[center] > i:
        return check(n_list, i, start, center - 1)

    # i 값이 중간값보다 큰 경우 start 값 변경 
    else:
        return check(n_list, i , center +1 , end)    
    

for i in m_list:
    
    check(n_list, i, 0, n-1)

