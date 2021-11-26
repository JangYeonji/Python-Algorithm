from itertools import combinations

n,m = map(int,input().split())
k = list(map(int,input().split()))

com = list(combinations(k,2))
result = len(com)

for i in com:
	if i[0]==i[1]:
        result -= 1
print(result)