def solution(x, n):
    answer = []
    if x==0 and n==0:
        return [0]
    elif x==0:
        return [0]*n
    elif n==0:
        return [0]
    
    for i in range(1,n+1):
        answer.append(x*i)
    return answer