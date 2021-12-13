'''입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 4 1 5 0 2 3 0 6 1 2
'''

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    graph = []
    inp = list(map(int, input().split()))
    for j in range(n):
        graph.append(inp[0 + (j * m):m + (j * m)])
    maxx = 0
    for y in range(1, m):
        for x in range(n):
            if x == 0:
                graph[x][y] += max(graph[x][y - 1], graph[x + 1][y - 1])
            elif x == n - 1:
                graph[x][y] += max(graph[x - 1][y - 1], graph[x][y - 1])
            else:
                graph[x][y] += max(graph[x][y - 1], graph[x - 1][y - 1], graph[x + 1][y - 1])
            if y == m - 1:
                if maxx < graph[x][y]:
                    maxx = graph[x][y]
    print(maxx)