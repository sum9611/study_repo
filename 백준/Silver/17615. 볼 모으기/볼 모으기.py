n = int(input())
balls = list(input())

colors = ['R','B']
result = []

   

for color in colors:
    start = False
    cnt = 0
    for i in range(n-1,-1,-1):
        if balls[i] != color and not start:
            start = True
        elif start and balls[i] == color:   
            cnt += 1
    result.append(cnt)
print(min(result))

