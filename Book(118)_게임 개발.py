#220325
n,m = map(int,input().split())

a,b,d = map(int,input().split())
#0:북, 1:동, 2:남, 3:서

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def direction(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2
    
answer = 1

def turn(d,x,y):
    if d==0:
        return x-1,y
    elif d==1:
        return x,y+1
    elif d==2:
        return x+1,y
    elif d==3:
        return x,y-1


def back(d,x,y):
    if d==0:
        return x + 1,y
    elif d == 1:
        return x, y - 1
    elif d == 2:
        return x - 1, y
    elif d == 3:
        return x, y + 1

graph[a][b] = 2

while True:
    if graph[a][b]==1:
        break
    for i in range(4):
        d = direction(d)
        x,y = turn(d,a,b)
        if x>=0 and y>=0 and x<m and y<n:
            if graph[x][y]==0:
                graph[x][y] = 2
                a,b = x,y
                answer += 1
                break
        if i==3:
            a,b = back(d,a,b)