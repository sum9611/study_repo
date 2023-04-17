from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
memo = {}

for i in range(n):
    memo[input().rstrip()] = 0
for j in range(m):
    key_word = input().rstrip().split(',')
    for k in key_word:
        if k in memo:
            if memo[k] == 0:
                n -= 1
                memo[k] = memo[k]+1
    print(n) 