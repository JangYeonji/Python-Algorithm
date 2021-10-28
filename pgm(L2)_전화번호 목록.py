#접두어만 검색하도록 고침
#False 다음 break

#2차시도 - 효율성 3,4 실패
def solution(phone_book):
    answer = True
    dic = dict()
    for idx,i in enumerate(sorted(phone_book)):
        dic[i] = idx
        
    for i in range(len(dic)):
        if i+1 == len(dic):
            break
        if list(dic.keys())[i] in list(dic.keys())[i+1][:len(list(dic.keys())[i])]:
            answer = False
            break
            
    return answer