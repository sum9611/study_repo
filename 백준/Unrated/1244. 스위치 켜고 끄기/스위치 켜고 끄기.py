n = int(input())

switch = list(map(int,input().split()))

m = int(input())

student = []
for _ in range(m):
    student.append(list(map(int,input().split())))


for i in student:

    #남자일경우 
    if i[0] == 1:
        default = i[1]
        switch_num = i[1]
        while True:
            #전원변경
            if switch[switch_num-1] == 1:
                switch[switch_num-1] = 0
            elif switch[switch_num-1] == 0:
                switch[switch_num-1] = 1
            switch_num += default
            if switch_num > n:
                break
    #여자일경우
    if i[0] == 2:
        switch_num = i[1] -1
        cnt = 1
        if switch[switch_num] == 1:
            switch[switch_num] = 0
        elif switch[switch_num] == 0:
            switch[switch_num] = 1

        while True:

            if (switch_num + cnt) >= n or (switch_num - cnt) < 0:
                break

            if switch[switch_num+cnt] == switch[switch_num-cnt]:
                for j in [switch_num+cnt,switch_num-cnt]:
                    if switch[j] == 1:
                        switch[j] = 0
                    elif switch[j] == 0:
                        switch[j] = 1
                cnt += 1
            else: break
cnt = 0
for i in range(n):
    cnt += 1
    print(switch[i], end = " ")
    if cnt == 20 :
        print()
        cnt = 0