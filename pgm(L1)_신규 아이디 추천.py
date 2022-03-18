import re
def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    
    #2
    prog = re.compile('[a-z0-9\.\-\_]')
    for i in new_id:
        if prog.match(i) == None:
            continue
        else:
            m = re.match('[a-z0-9\.\-\_]',i)
            answer += m.group(0)
    
    #3
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #4
    if answer=='.':
        answer = ''
    else:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #5
    if answer == '':
        answer = 'a' * 3
    
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:-1]
    
    #7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
            
    return answer