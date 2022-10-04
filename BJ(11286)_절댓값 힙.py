#17분/40분

import heapq
import sys

input = sys.stdin.readline
result = []
queue = []

n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(queue,[abs(x),x//abs(x)])
    else:
        if queue==[]:
            print(0)
        else:
            result = heapq.heappop(queue)
            print(result[0]*result[1])