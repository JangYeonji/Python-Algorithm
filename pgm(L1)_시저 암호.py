def solution(s, n):
    answer = ''
    #a 97 z 122
    #A 65 Z 90 
    for i in s:
        if i==' ':
            answer += ' '
        else:
            if ord(i) <= 90:     
                if 65<=ord(i)+n and 90>=ord(i)+n:
                    answer += chr(ord(i)+n)
                else: 
                    answer += chr(ord(i)+n - 91 + 65)   
            else:    
                if 97<=ord(i)+n and 122>=ord(i)+n:
                    answer += chr(ord(i)+n)
                else:
                    answer += chr(ord(i)+n - 123 + 97)
            
    return answer