'''입력예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

parent = [0]*n
for i in range(n):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            union_parent(parent,i,j)

travel = list(map(int,input().split()))

answer = [0]*len(travel)
for i in range(len(travel)):
    answer[i] = parent[travel[i]-1]

if len(set(answer))==1:
    print('YES')
else:
    print('NO')