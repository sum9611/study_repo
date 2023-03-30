from collections import deque

n, k = map(int,input().split())
ph_list = deque(list(input()))
cnt = 0
while ph_list:
    target = ph_list.popleft()

    if not ph_list:
        break

    if target == 'H':
        for i in range(min(k,len(ph_list))):
            if ph_list[i] == 'P':
                ph_list[i] = '-'
                cnt += 1 
                break
    elif target == 'P':
        for i in range(min(k,len(ph_list))):
            if ph_list[i] == 'H':
                ph_list[i] = '-'
                cnt += 1 
                break

print(cnt)
        