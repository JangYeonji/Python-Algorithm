import heapq

def dikjstra(start,distance,graph):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    dikjstra(1,distance,graph)
    for i in range(1,N+1):
        if distance[i]<=K:
            answer += 1

    return answer