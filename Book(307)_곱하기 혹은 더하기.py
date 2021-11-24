'''입력 예시
02984

567
'''

s = input()
def op(a,b):
    if a==0 or a==1 or b==0 or b==1:
        return a+b
    else:
        return a*b
answer = op(int(s[0]),int(s[1]))
for i in s[2:]:
    answer = op(answer,int(i))