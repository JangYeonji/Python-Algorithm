#패캠 답
import sys
input = sys.stdin.readline
import heapq

k,n = map(int,input().split())
data = list(map(int,input().split()))

heap = data.copy()
visited = set()
max_value = max(data)

heapq.heapify(heap)

for i in range(n-1):
    element = heapq.heappop(heap)
    for x in data:
        now = element * x
        if len(heap)>=n and max_value<now:
            continue
        if now not in visited:
            heapq.heappush(heap,now)
            max_value = max(max_value, now)
            visited.add(now)

print(heapq.heappop(heap))