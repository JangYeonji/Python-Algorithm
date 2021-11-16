'''입력예시
5 3
1 2 5 4 3
5 5 6 6 5
'''

import sys
n,k = map(int,input().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))