import heapq

def dijkstra(start,distance,graph):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
def solution(n, edge):
    answer = 0
    distance = [int(1e9)] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for i in edge:
        graph[i[0]].append((i[1],1))
        graph[i[1]].append((i[0],1))
        
    dijkstra(1,distance,graph)
    
    distance.pop(0)
    for i in distance:
        if i==max(distance):
            answer += 1
            
    return answer