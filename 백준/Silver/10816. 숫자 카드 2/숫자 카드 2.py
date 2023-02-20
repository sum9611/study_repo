from sys import stdin

input = stdin.readline


n = int(input())
card_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

card_list2 = {}
for i in card_list:
    if card_list2.get(i) != None:
        card_list2[i] = card_list2[i] + 1
    else:
        card_list2[i] = 1

for i in m_list:
    if card_list2.get(i) == None:
        print(0, end=' ')
    else:
        print(card_list2[i], end= ' ')
