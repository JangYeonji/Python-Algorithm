#40분/60분
#문제 파악 오류
import sys
import heapq

input = sys.stdin.readline

t = int(input())

for tt in range(t):
    k = int(input())
    queue = []

    for i in range(k):
        a, b = input().split()
        if a == 'I':
            heapq.heappush(queue,int(b))
        else:
            if queue == []:
                continue
            if b=='-1':
                heapq.heappop(queue)
            else:
                queue.pop()
            
    if queue == []:
        print("EMPTY")
    else:
        print(max(queue), min(queue))
