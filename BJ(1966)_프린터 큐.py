#36분 43초/25분
t = int(input())
for tt in range(t):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))
    idx = [i for i in range(n)]
    count = 0
    i = 0
    while queue:
        if max(queue)!=queue[0]:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))
        else:
            count += 1
            if idx[0]==m:
                print(count)
                break
            queue.pop(0)
            idx.pop(0)