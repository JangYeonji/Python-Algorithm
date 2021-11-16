'''
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
'''

import sys
input_data = sys.stdin.readline().rstrip()

n,m,k,x = map(int, input_data.split()[0:4])
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input_data.split()[4+(2*i):6+(2*i)])
    graph[a][b] = graph[b][a] = 1

visit = [False] * (n+1)

def gg(n,m,k,x,graph,visit):
    visit[x] = True
    for j in range(1, k+1):
        for i in range(1,n+1):
            if graph[j][i]==1 and visit[i]==False:
                graph[j][i] = 1+j
                visit[i] = True

gg(n,m,k,x,graph,visit)

for i in range(1,n+1):
    if graph[k][i]==1+k:
        print(i)