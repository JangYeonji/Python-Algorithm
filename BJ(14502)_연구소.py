n,m = map(int,input().split())

graph = []
zero = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            zero.append((i, j))
            
from itertools import combinations

combi = list(combinations(zero,3))

def safe(change, graph2):
    q = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    result = 0
    for x, y in change:
        graph2[x][y] = 1
    for nn in range(n):
        for mm in range(m):
            if graph2[nn][mm] == 2:
                q.append((nn, mm))
                while q:
                    xx, yy = q.pop()
                    for i in range(4):
                        nx = xx + dx[i]
                        ny = yy + dy[i]
                        if nx >= 0 and ny >= 0 and nx < n and ny < m:
                            if graph2[nx][ny] == 0:
                                graph2[nx][ny] = 2
                                q.append((nx, ny))
    for k in range(n):
        result += graph2[k].count(0)
    return result

import copy

answer = 0
for i in list(combinations(zero,3)):
    tmp = safe(i, copy.deepcopy(graph))
    if answer < tmp:
        answer = tmp

print(answer)