from itertools import permutations

def op(a,b,opp):
    if opp=='+':
        return a+b
    elif opp=='-':
        return a-b
    elif opp=='*':
        return a*b
    elif opp=='/':
        return int(a/b)

n = int(input())
alist = list(map(int,input().split()))
option = list(map(int,input().split()))

pm = []

for idx, i in enumerate(option):
    for j in range(i):
        if idx==0:
            pm.append('+')
        elif idx==1:
            pm.append('-')
        elif idx==2:
            pm.append("*")
        elif idx==3:
            pm.append('/')

per = set(permutations(pm,n-1))

minn = 1e9
maxx = -1e9

for perpm in per:
    tmp = alist[0]
    for a,p in zip(alist[1:],perpm):
        tmp = op(tmp,a,p)
    if tmp < minn:
        minn = tmp
    if tmp > maxx:
        maxx = tmp

print(maxx)
print(minn)