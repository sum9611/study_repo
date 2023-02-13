# from sys import stdin


n, m = map(int,input().split())
n_list = list(map(int,input().split()))
values_list = []
    


for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum_values = n_list[i] + n_list[j] + n_list[k]
            if sum_values <= m:
                values_list.append(sum_values)
            
print(max(values_list))
    

        
    
    
    