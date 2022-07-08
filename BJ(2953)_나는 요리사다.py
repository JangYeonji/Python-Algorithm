#2분51초/10분
result = []
for i in range(5):
    tmp = list(map(int,input().split()))
    result.append(sum(tmp))
    
print(result.index(max(result))+1, max(result))