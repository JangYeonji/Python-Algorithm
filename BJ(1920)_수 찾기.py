n = int(input())
a = set(map(int,input().split()))
n = int(input())
m = list(map(int,input().split()))

for mdata in m:
	if mdata in a:
		print(1)
	else:
		print(0)