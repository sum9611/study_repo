from sys import stdin

# input = stdin.readline

s = input().rstrip()
s_dict = {}
start = 0
plus = 1
while True:
    s_dict[s[start:start+plus]] = 1
    # print(s[start:start+plus])
    plus += 1
    if start+plus > len(s):
        plus = 1
        start += 1
    if start > len(s) -1:
        break 
print(len(s_dict))