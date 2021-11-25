#1차시도 -> 효율성 테스트 1,2,3,4 실패

import re
def solution(words, queries):
    answer = [0] * len(queries)
    words = sorted(words)
    p = [0] * len(queries)
    
    for i in range(len(queries)):
        queries[i] = queries[i].replace("?",".")
    for i in range(len(queries)):
        p[i] = re.compile(queries[i])
    
    for j in range(len(queries)):
        for i in words:
            if p[j].findall(i) == []:
                continue
            else:
                if p[j].findall(i)[0] == i:
                    answer[j] += 1
    return answer