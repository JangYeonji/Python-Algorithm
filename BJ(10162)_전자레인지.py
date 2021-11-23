'''입력 예제
100

189
'''

t = int(input())

result = [0]*3

while t > 0:
    if t<10:
        break
    while t >= 300:
        t -= 300
        result[0] += 1
    while t >= 60:
        t -= 60
        result[1] += 1
    while t >= 10:
        t -= 10
        result[2] += 1

if t==0:
    for i in result:
        print(i, end=' ')
else:
    print(-1)