'''
a1

c2
'''
s = input()

dx = [2,-2,1,-1]
dy = [1,1,2,2]

cnt = 0
for i in range(4):
    if ord(s[0]) + dx[i] <= ord('h') and ord(s[0]) + dx[i] >= ord('a') and int(s[1])+dy[i]<=8 and int(s[1])+dy[i]>=1:
        cnt += 1