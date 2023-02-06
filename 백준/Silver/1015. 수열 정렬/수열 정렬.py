N = int(input())


temp_A = input().split()
list_A = []
list_A2 = []
list_P = []

for i in temp_A:
    list_A.append(int(i))
    list_A2.append(int(i))
    
list_A2.sort()
        

for i in list_A:
    list_P.append(list_A2.index(i))
    list_A2[list_A2.index(i)] = 0

for i in list_P:
    print(i, end= ' ')