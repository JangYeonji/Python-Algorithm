def solution(relation):
    answer = 0
    reverse = [0]*len(relation[0])
    
    for r in relation:
        for i in range(len(r)):
            reverse[i].append(r[i])
    
    print(reverse)
    return answer