def solution(n):
    answer = 0
    if n==1:
        return 1
    
    for i in range(1,n):
        if n//i < i:
            break
        elif n//i == i and n%i==0:
            answer += i
            break
        if n%i==0:
            answer += i
            answer += n//i
        
    
    return answer