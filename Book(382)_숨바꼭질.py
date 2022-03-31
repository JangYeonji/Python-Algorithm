import heapq

n,m = map(int,input().split())
distance = [1e9]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m): 
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for j in graph[now]:
            cost = dist+j[1]
            if distance[j[0]]>cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost,j[0]))

print(distance.index(max(distance[1:])), max(distance[1:]), distance.count(max(distance[1:])))