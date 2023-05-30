n = int(input())
liq_list = list(map(int,input().split()))


left = 0
right = n-1

result = abs(liq_list[left] + liq_list[right])
result_left = left
result_right = right

while left < right:
    check = liq_list[left] + liq_list[right]

    if abs(check) < result:
        result_left = left
        result_right = right
        result = abs(check)
        if result == 0:
            break
    if check < 0:
        left += 1
    else: 
        right -= 1
print(liq_list[result_left], liq_list[result_right])