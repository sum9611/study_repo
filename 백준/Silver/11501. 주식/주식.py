t = int(input())

for _ in range(t):
    n = int(input())

    n_list = list(map(int,input().split()))
    mx = 0
    sum = 0

    for i in range(n-1,-1,-1):
        if n_list[i] > mx:
            mx = n_list[i]
        else:
            sum += mx - n_list[i]

    print(sum)


