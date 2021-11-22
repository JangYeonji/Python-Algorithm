'''입력 예시
5 8 3
2 4 5 4 6
'''

n,m,k = map(int,input().split())

li = list(map(int,input().split()))
li.sort(reverse=True)

result = []
for i in range(1,m+1):
    if i%(k+1)==0:
        result.append(li[1])
    else:
        result.append(li[0])

print(sum(result))