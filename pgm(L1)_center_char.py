#가운데 글자 가져오기
'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
'''

#mine
def solution(s):
    answer = ''
    cnt = 0
    if len(s)%2==1:
        cnt = int(len(s)/2)
        answer = s[cnt]
    else:
        cnt = int(len(s)/2)
        answer = s[(cnt-1):(cnt+1)]
    return answer

#ㄳ
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
                #(5-1)//2 : (5)//2 +1 -> 2:3
                #(4-1)//2 : (4)//2 +1 -> 1:3