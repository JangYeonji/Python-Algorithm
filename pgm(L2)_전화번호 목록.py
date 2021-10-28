#3차시도 - 해시 제거
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        if i+1 == len(phone_book):
            break
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
            
    return answer