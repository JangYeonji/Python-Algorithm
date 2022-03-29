n,m = map(int,input().split())
rc = list(map(int,input().split()))
rc.sort()

left = rc[0]
right = rc[-1]

while left<right:
    if (left+right)//2 != mid:
        mid = (left+right)//2
    else:
        print(mid)
        break
    tmp = 0
    for i in rc:
        if i>mid:
            tmp += i - mid
    if tmp==m:
        print(mid)
        break
    elif tmp<m:
        right = mid
    elif tmp>m:
        left = mid