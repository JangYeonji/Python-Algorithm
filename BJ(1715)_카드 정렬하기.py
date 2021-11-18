'''입력예시
3
10
20
40
'''

n = int(input())
card=[]
for i in range(n):
	card.append(int(input()))
card.sort()

two = card[0]+card[1]
result = two
for i in range(2, len(card)):
    two += card[i]
    result += two
print(result)