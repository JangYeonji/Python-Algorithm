'''입력 예시
26
'''

x = int(input())


if x%5==0:
	x/=5
elif x%3==0:
	x/=3
elif x%2==0:
	x/=2
else:
	x-=1
