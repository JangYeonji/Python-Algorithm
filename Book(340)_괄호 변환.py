#1차시도 - 테스트 2,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
def solution(p):
    answer = ''
    w=""
    for i in p:
        w += i
        if '()' in w:
            w=w.replace('()','')
    if w=='':
        answer = p
    else:
        for i in p[::-1]:
            answer += i
    return answer