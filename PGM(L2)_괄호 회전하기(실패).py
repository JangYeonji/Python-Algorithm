from collections import deque

def check(strr):
    if '(' in strr and ')' in strr:
        if strr.index('(') > strr.index(')'):
            return False
    else:
        return False
    if '[' in strr and ']' in strr:
        if strr.index('[') > strr.index(']'):
            return False
    else:
        return False
    if '{' in strr and '}' in strr:
        if strr.index('{') > strr.index('}'):
            return False
    else:
        return False
    return True

def solution(s):
    answer = 0
    l = len(s)
    if check(s):
        answer += 1
    s = deque(s)
    for i in range(l-1):
        s.append(s.popleft())
        if check(s):
            answer += 1
        
    return answer