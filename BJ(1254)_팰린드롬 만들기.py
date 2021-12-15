def pal(ss):
    half = len(ss)//2
    for i in range(half):
        if s[i] != s[-(i+1)]:
            return False 
    return True
tmp = ''

s = input()
leng = len(s)
if fel(s)==False:
    for i in range(leng):
        tmp += s[i]
        s += tmp[::-1]
        if pal(s)==True:
            break
        for i in range(len(tmp)):
            s = s[:leng]

print(len(s))