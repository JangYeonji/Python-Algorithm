#info : 개발언어 직군 경력 소울푸드 점수
#query : 개발언어 and 직군 and 경력 and 소울푸드 X
def solution(info, query):
    answer = [0]*len(query)

    for qdx, q in enumerate(query):
        tmp = q.split('and')
        for i in info:
            for idx in range(4):
                if idx>=3:
                    if i.split(' ')[3] != tmp[idx].split(' ')[0]:
                        continue
                    if i.split(' ')[4] != tmp[idx].split(' ')[1]:
                        continue
                if i.split(' ')[idx] != tmp[idx][:-1]:
                    continue
                else:
                    answer[qdx] += 1
        
    return answer