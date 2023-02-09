import heapq
N, L = map(int,input().split())
end = 0
cnt = 0
list1 = (list(map(int,input().split())))
list1.sort()


for i in list1:
    if i > end:
        end = i + L -1
        cnt += 1
print(cnt)

