'''
3 2 1
1 2 4
1 3 2
'''

import heapq
import sys
input = sys.stdin.readline
n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
INF = int(1e9)
visit = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    visit[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if visit[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<visit[i[0]]:
                visit[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(c)
cnt = 0
maxx = 0
for i in range(2,n+1):
    if visit[i]!=INF:
        cnt +=1
    if maxx<visit[i]:
        maxx = visit[i]

print(cnt,maxx)