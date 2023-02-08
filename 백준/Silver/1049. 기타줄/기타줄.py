from sys import stdin

## N == 끊어진 기타줄의 개수
## M == 기타줄 브랜드
## P1 == 패키지가격, P2 == 낱개 가격
N, M = map(int, stdin.readline().split())
p1_list = []
p2_list = []

for i in range(M):
    P1, P2 = map(int, stdin.readline().split())
    p1_list.append(P1)
    p2_list.append(P2)

if min(p1_list) < min(p2_list)*(N%6):
    result = ((N//6+1) * min(p1_list))
elif min(p2_list)*6 < min(p1_list):
    result = N * min(p2_list)
else:
    result = (N//6 * min(p1_list)) + (N%6 * min(p2_list))
print(result)