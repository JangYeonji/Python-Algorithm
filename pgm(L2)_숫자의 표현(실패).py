def solution(n):
    answer = 0
    for i in range(1,n//2):
        if n%i==0:
            answer += 1
        elif n%i==1:
            answer += 1
    return answer