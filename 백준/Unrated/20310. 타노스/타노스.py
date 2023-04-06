s = input()
zero = s.count('0')//2
one = s.count('1')//2
result = ''

for _ in range(zero):
    result += '0'
for _ in range(one):
    result += '1'
print(result)