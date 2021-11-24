'''입력 예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [int(1e9)] * (n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

result = [0]*3

result[1] = max(distance[1:])
result[2] = distance.count(result[1])
for i in range(len(distance)):
    if distance[i]==result[1]:
        result[0] = i
        break
for i in result:
    print(i, end=' ')