#mine

import sys
from collections import deque

read = sys.stdin.readline()
com = int(read.split()[0])
pair = int(read.split()[1])
graph = [[0]*(com+1) for _ in range(com+1)]
for i in range(pair):
    a,b = map(int,read.split()[2+(2*i):4+(2*i)])
    graph[a][b] = graph[b][a] = 1
visit = [False] * (com+1)

def virus2(graph, start, visit):
    cnt = 0
    visit[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in range(1, com+1):
            if visit[i]==False and graph[v][i]:
                queue.append(i)
                visit[i] = True
    return cnt-1

print(virus2(graph,1,visit))

#ㄳ

from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
bfs(1, dic)
print(len(visited)-1)