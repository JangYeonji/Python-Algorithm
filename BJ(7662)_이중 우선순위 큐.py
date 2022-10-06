#40분/60분
#문제 파악 오류
import sys
import heapq

input = sys.stdin.readline

t = int(input())

for tt in range(t):
    k = int(input())
    queue = []
    s = set()

    for i in range(k):
        a, b = input().split()
        
        if a == 'I':
            if b in s:
                continue
            heapq.heappush(queue,int(b))
        else:
            if queue == []:
                continue
            if b=='-1':
                heapq.heappop(queue)
            else:
                queue.pop()
        s.add(b)

    if queue == []:
        print("EMPTY")
    else:
        print(max(queue), min(queue))
