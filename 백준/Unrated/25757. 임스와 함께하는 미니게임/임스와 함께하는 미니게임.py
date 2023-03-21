from sys import stdin
from collections import deque
# import sys
# sys.setrecursionlimit(10**7)
# input = stdin.readline


n, g= map(str,input().split())
player = []

for i in range(int(n)):
    player.append(input())

player = list(set(player))

if g == 'Y':
    print(len(player)//1)
elif g == 'F':
    print(len(player)//2)
elif g == 'O':
    print(len(player)//3)    