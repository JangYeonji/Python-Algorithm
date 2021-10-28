#1차시도 - 테스트 13 실패, 효율성 1,2,3,4 실패
def solution(phone_book):
    answer = True
    dic = dict()
    for idx,i in enumerate(sorted(phone_book)):
        dic[i] = idx
        
    for i in range(len(dic)):
        if i+1 == len(dic):
            break
        if list(dic.keys())[i] in list(dic.keys())[i+1]:
            answer = False
            
    return answer