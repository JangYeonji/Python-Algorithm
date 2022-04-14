def solution(n):
    answer = 0
    cnt = str(bin(n)).count('1')
    
    for i in range(n+1,1000000):
        if cnt == str(bin(i)).count('1'):
            return i