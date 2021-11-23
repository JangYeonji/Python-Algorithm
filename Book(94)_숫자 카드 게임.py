'''입력 예시
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''

n,m = map(int,input().split())
card = [[] for _ in range(n)]
for i in range(n):
	card[i] = list(map(int,input().split()))
result = 0
for i in card:
    if result < min(i):
        result = min(i)
print(result)