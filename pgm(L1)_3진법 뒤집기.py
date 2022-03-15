def solution(n):
    answer = ''
    i=1
    three = [1]
    answer2 = 0
    
    while 3**i<=n:
        three.append(3**i)
        i += 1
    
    for i in three[::-1]:
        tmp = 0
        while i<=n:
            n -= i
            tmp += 1
        answer += str(tmp)
        
    for idx, i in enumerate(answer):
        answer2 += int(i) * (3**idx)    

    return answer2