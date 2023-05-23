s = list(input())
t = list(input())
queue = [t]
check = False
while queue:
    target = queue.pop(0)
    if target == s:
        print(1)
        check = True
        break
    if target[-1] == 'A' and len(target) > 1:
        queue.append(target[:-1])
    if target[0] == 'B' and len(target) > 1:
        queue.append(target[1:][::-1])

if not check:
    print(0) 