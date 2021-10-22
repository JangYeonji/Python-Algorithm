'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

import sys
input_data = sys.stdin.readline().rstrip()
n = int(input_data.split()[0])
m = int(input_data.split()[1])

graph = []
for i in range(2,n+2):
    graph.append(list(map(int,input_data.split()[i])))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result += 1
print(result)