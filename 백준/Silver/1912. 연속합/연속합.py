from sys import stdin

input = stdin.readline

n = int(input())

n_list = list(map(int,input().split()))

result_set = [0] * (n)

result_set[0] = n_list[0]

for i in range(1,n):
    result_set[i] = max(n_list[i], result_set[i-1] + n_list[i])
print(max(result_set))


