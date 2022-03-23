'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

def dfs(x,y,graph,n,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(x,y)])
    graph[x][y] = '1'
    while q:
        xx,yy = q.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if graph[nx][ny] == '0':
                    graph[nx][ny] = '1'
                    q.append((nx,ny))
    return graph


answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='0':
            graph = dfs(i,j,graph,n,m)
            answer += 1
            
print(answer)