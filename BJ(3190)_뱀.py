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

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1][y - 1] = 1
l = int(input())
xc = []
for i in range(l):
    x,c = sys.stdin.readline().split()
    xc.append((x,c))

snake = 9
cnt = 0
graph[0][0] = snake

for x,c in xc:
    for i in range(1,int(x)+1):
        graph[i][0] = snake
        graph[i-1][0] = 0
        cnt += 1
    if c=='D':