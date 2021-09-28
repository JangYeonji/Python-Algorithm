#모의고사 (다시)

'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''

#mine --> 몇개의 테스트케이스 실패
def solution(answers):
    answer = []
    a1, a2, a3 = [],[],[]
    
    j=1
    for i in answers:
        if i==j:
            a1.append(i)
        if j==6:
            j=1
        j+=1
        
    j=1
    for idx, i in enumerate(answers):
        if idx%2==0:
            k=2
        else:
            k=j
            j+=1
        if i==k:
            a2.append(i)
      
    su3 = [3,3,1,1,2,2,4,4,5,5]
    if len(answers)>len(su3):
        len_ = len(answers) - len(su3)
        for a in range(0,len_):
            su3.append(su3[a])
    for idx, i in enumerate(answers):
        if i==su3[idx]:
            a3.append(i)
    
    #print("{}{}{}".format(a1,a2,a3))
    if len(a1)>len(a2) and len(a1)>len(a3):
        answer = [1]
    elif len(a2)>len(a1) and len(a2)>len(a3):
        answer = [2]
    elif len(a3)>len(a1) and len(a3)>len(a2):
        answer = [3]
    elif len(a1)==len(a2)==len(a3):
        answer = [1,2,3]
    elif len(a1)==len(a2):
        answer = [1,2]
    elif len(a1)==len(a3):
        answer = [1,3]
    elif len(a2)==len(a3):
        answer = [2,3]
    
    return answer

#ㄳ
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result