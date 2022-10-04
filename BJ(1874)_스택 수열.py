#30분/30분
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
    
s = []
result = []

for i in range(1,n+1):
    s.append(i)
    result.append("+")
    while l and s != []:
        if s[-1]==l[0]:
            s.pop()
            l.pop(0)
            result.append("-")
        else:
            break
            
if l != []:
    print("NO")
else:
    for r in result:
        print(r)