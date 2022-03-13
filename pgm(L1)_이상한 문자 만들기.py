def solution(s):
    answer = ''
    count = 0
    
    for idx, i in enumerate(s):
        if i==' ':
            count = 0
            answer += ' '
        elif count%2==0:
            answer += s[idx].upper()
            count += 1
        else:
            answer += s[idx].lower()
            count += 1
            
    return answer