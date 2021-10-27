'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''

import sys
input_data = sys.stdin.readline().rstrip()
n,k = map(int,input_data.split()[0:2])
graph = []
for i in range(n):
    graph.append(list(map(int, input_data.split()[2+(i*3):5+(i*3)])))
s,x,y = map(int, input_data.split()[-3:])
xx = [-1,1,0,0]
yy = [0,0,-1,1]

def virus(a,b):
    for i in range(4):
        nx = a + xx[i]
        ny = b + yy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b]

for i in range(s):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                x1, y1 = i, j
            if graph[i][j] == 2:
                x2, y2 = i, j
            if graph[i][j] == 3:
                x3, y3 = i, j
    virus(x1,y1)
    virus(x2,y2)
    virus(x3,y3)

print(graph[x-1][y-1])