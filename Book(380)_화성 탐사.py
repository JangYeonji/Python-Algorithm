'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
import sys
import heapq

t = int(input())
n = [0]*t
tc = []
for i in range(t):
    n[i] = int(input())
    for i in range(n[i]):
        tc.append(sys.stdin.readline().rstrip().split())

INF = int(1e9)
visit = [0] * (t+1)
for i in range(1,t+1):
    visit[i] = [INF]*n[i-1]

tc2 = [0]*(t+1)
for i in range(1,t+1):
    tc2[i] = [0]*(n[i-1]+1)


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    visit