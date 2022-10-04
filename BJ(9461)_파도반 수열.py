t = int(input())
for i in range(t):
    n = int(input())
    p = [0]*101
    p[1]=1
    p[2]=1
    p[3]=1
    p[4]=2
    p[5]=2
    for index in range(6,101):
        p[index] = p[index-4]+p[index-1]
    print(p[n])