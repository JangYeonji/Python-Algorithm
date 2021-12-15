'''입력 예시
11

10

4
'''

n = int(input())

d[1] = 1
for i in range(1001):
    if i%2==0 or i%3==0 or i%5==0:
        d[i] = i

for i in range(2,1001):
    if i%2==0:
        if d[i//2]==0:
            d[i] = 0
    if i%3==0:
        if d[i//3]==0:
            d[i] = 0
    if i%5==0:
        if d[i//5]==0:
            d[i] = 0

count = 0
for i in range(1,1001):
    if d[i]!=0:
        count += 1
    if count == n:
        print(d[i])
        break