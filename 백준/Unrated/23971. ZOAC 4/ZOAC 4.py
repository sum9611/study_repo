from sys import stdin
# from collections import deque
# import sys
# sys.setrecursionlimit(10**7)
# input = stdin.readline


h,w,n,m = map(int,input().split())
cnt = 0
for i in range(0,h,n+1):
    for j in range(0,w,m+1):
        cnt += 1
print(cnt)
    