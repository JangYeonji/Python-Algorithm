'''입력예시
4
3
4
1
1

4
6
2
2
3
3
4
4
'''

g = int(input())
p = int(input())
gate = [0]*(g+1)
cnt = 0
for i in range(p):
    air = int(input())
    brk = 0
    for a in range(air, 0, -1):
        if gate[a] == 0:
            gate[a] = air
            cnt += 1
            break
        else:
            brk += 1
    if brk==air:
        break
print(cnt)