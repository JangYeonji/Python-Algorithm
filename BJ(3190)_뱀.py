'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''

#220325
n = int(input())
k = int(input())

graph = [[0]*(n) for i in range(n)]
for i in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
l = int(input())
snake = []
for i in range(l):
    snake.append(input().split())

def direction(d,x,y):
    if d=='R':
        return x,y+1
    elif d=='L':
        return x,y-1
    elif d=='U':
        return x-1,y
    elif d=='D':
        return x+1,y

x,y = 0,0
d = 'R'
answer = 0
idx = 0
graph[x][y] = 9

while True:
    xx,yy = direction(d, x, y)
    if xx>=0 and yy>=0 and xx<n and yy<n:
        answer += 1
        if graph[xx][yy] == 0:
            graph[x][y] = 0
            x,y = xx,yy
        elif graph[x][y]==9:
            break
        graph[xx][yy] = 9
        if idx<l and int(snake[idx][0])==answer:
            d = snake[idx][1]
            idx += 1
    else:
        break