def solution(s):
    for i in s:
        if i.isalpha() or len(s)!=4 and len(s)!=6:
            return False
    return True