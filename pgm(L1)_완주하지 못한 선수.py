#mine - 성공
def solution(participant, completion):
    answer = ''
    dic = {x:0 for x in participant}
    
    for i in participant:
        dic[i] +=1
    for i in completion:
        dic[i] -=1    
    for k,v in dic.items():
        if v==1:
            answer = k
    return answer