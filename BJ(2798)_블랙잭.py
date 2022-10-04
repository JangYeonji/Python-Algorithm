#10분 54초/20분
from itertools import combinations

n,m = map(int,input().split())
cards = list(map(int,input().split()))

combi = list(combinations(cards,3))
result = []

for i in combi:
    result.append(sum(i))
    
if m in result:
    print(m)
else:
    count = 1
    while True:
        if m-count in result:
            print(m-count)
            break
        else:
            count += 1