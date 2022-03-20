'''입력 예시
5
2 3 1 2 2
'''

n = int(input())
scared = list(map(int, input().split()))
answer = 0
adict = {}
for i in range(n):
    adict[scared[i]] = 0

for i in range(n):
    adict[scared[i]] += 1
    
for k,v in adict.items():
    answer += int(v//k)

print(answer)