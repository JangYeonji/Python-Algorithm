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

import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int,input().split())
	graph[a].append((b,1))
distance = [INF] * (n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(x)
result = []

for i in range(1,n+1):
    if distance[i]==k:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)