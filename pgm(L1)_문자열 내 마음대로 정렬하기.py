def solution(strings, n):
    answer = []
    hashs = {}
    
    for i in strings:
        hashs[i] = i[n]
        
    hashs = dict(sorted(hashs.items(), key=lambda x:x[0]))
    hashs = dict(sorted(hashs.items(), key=lambda x:x[1]))
    
    for i in hashs.keys():
        answer.append(i)
        
    return answer