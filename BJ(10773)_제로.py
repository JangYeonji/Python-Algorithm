#2분17초/20분
k = int(input())
stack = []
for i in range(k):
    a = int(input())
    if a!=0:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))