#결과는 맞지만 틀림
'''
6
10
20
15
25
10
20
'''

import itertools

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
cnt = int((n-1)/2)
sum_ = sum(arr)
iter = list(itertools.permutations(arr[:-1],2))
maxx=0

for i in iter:
    for idx in range(len(arr)):
        if idx==len(arr)-1:
            break
        if arr[idx] in i and arr[idx+1] in i:
            iter.remove(i)

for i in iter:
    a = sum_ - sum(i)
    if a>maxx:
        maxx = a
print(maxx)