from itertools import combinations

n = int(input())
money = list(map(int,input().split()))

result = {i:0 for i in range(1,1000000+1)}

for i in range(1,n+1):
    tmp = set(combinations(money, i))
    for j in tmp:
        result[sum(j)] += 1

print(sorted(result.items(), key=lambda x:x[1])[0][0])