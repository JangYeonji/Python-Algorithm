g = int(input())
p = int(input())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [0]*(g+1)
for i in range(g+1):
    parent[i] = i
    
answer = 0

for _ in range(p):
    tmp = find_parent(parent, int(input()))
    if tmp == 0:
        break
    tmp = union_parent(parent, tmp, tmp - 1)
    answer += 1
    
print(answer)