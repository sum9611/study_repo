from sys import stdin

input = stdin.readline
n = int(input())
a_list = list(map(int,input().split()))
a_list.sort(reverse=True)

result_list = []
check = True
cnt = 0
for i in range(n):
    if check:
        check = False
        result_list.append(a_list[cnt])
        cnt += 1
    else:
        check = True
        result_list.append(a_list[n-cnt])
        
score = result_list[0]

for i in range(1,len(result_list)):
    score += max(0, result_list[i] - result_list[i-1])

print(score)

