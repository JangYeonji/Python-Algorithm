#답 확인 후 일주일 후 2차시도
def balance(p):
    cnt = 0
    for idx, i in enumerate(p):
        if i=='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt==0:
            return idx+1
def correct(w):
    if w[0]=='(':
        return True
    return False
def turn(w):
    a = ''
    for i in w:
        if i=='(':
            a+=')'
        else:
            a+='('
    return a

def solution(p):
    answer = ''
    if p=='':
        return ''
    idx = balance(p)
    u = p[:idx]
    v = p[idx:]
    if not correct(u):
        empty = '('
        empty += solution(v)
        empty += ')'
        empty += turn(u[1:-1])
        answer += empty
    else:
        answer += u
        answer += solution(v)
        
    return answer